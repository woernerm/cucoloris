"""Module for a color changing rectangle.

This module defines the most basic shape that almost all other
widgets are composed of. It is a rectangle with rounded corners that can
smoothly transition to another color or resize itself. A widget that
directly builds upon that functionality is RectangleElement. It is
composed of two ColorArea classes to define a filled rectangle, i.e. one
separate border and fill colors each of which inherit the smooth color
transition functionality.
"""

# Import of built-in Python modules.
from math import modf as _modf
from typing import List as _List
from typing import Union as _Optional

# Inport of third-party modules.
from kivy.animation import Animation as _Animation
from kivy.graphics import Color as _Color
from kivy.properties import ListProperty as _ListProperty
from kivy.properties import NumericProperty as _NumericProperty
from kivy.graphics import RoundedRectangle as _RoundedRectangle
from kivy.uix.widget import Widget as _Widget


class ColorArea(_Widget):
    """Rounded rectangle with animated color transitions.

    The ColorArea widget is a rectangle with rounded corners that can
    smoothly change color. The user of this class can do this using
    two methods:

    * modify: The nominal color of the widget is modified in HSV-space
    (hue, saturation and value) using a smooth color transition. The
    values given are not absolute ones but differences to the current
    nominal color. The modification can be easily undone by calling the
    function with zero values for all HSV-components.

    * recolor: Changes the nominal color by smoothly transitioning to
    the given color in RGBA-space (red, green, blue, alpha).
    """

    color           = _ListProperty([0.4, 0.2, 0.5, 1])
    """The nominal color of the widget in RGBA-space.

    The color is described as a list of float values between 0 and 1. It
    is interpreted in RGBA-space, i.e. [red, green, blue, alpha].
    """

    radius          = _ListProperty([4, 4, 4, 4])
    """The radius of each corner of the widget in pixels.

    The ColorArea widget is a rounded rectangle. Each of the four
    corners may have a different radius given in pixels, e.g.
    [2, 4, 3, 8].
    """

    transition      = _NumericProperty(0.15)
    """Transition time in seconds.

    The ColorArea widget transitions smoothly between colors. The time
    it shall take from one color state to another can be set using this
    attribute.
    """

    _hsv            = _ListProperty()
    """Private parameter representing the current color in HSV-space."""

    def __init__(self, size:_Optional[_List[int]] = None, radius:_Optional[_List[int]] = None,
                 color:_Optional[_List[float]] = None, transition:_Optional[float] = None,
                 **kwargs):
        """Initialization method of the class.

        The initialization method initializes the base class and creates
        a rounded rectangle on the widget's canvas. Other parameter
        that shall be passed on to the base class may be given using the
        *args and **kwargs parameters.

        Args:
            *args: Any positional arguments that shall be passed on to
            the base class (Widget).
            **kwargs: Any keyed arguments that shall be passed on to the
            base class (Widget).
        """

        super(ColorArea, self).__init__(**kwargs)

        self.size       = size if size else self.size
        self.radius     = radius if radius else self.radius
        self.color      = color if color else self.color
        self.transition = transition if transition else self.transition
        self.size_hint = [None, None]

        with self.canvas:
            self.canvas_color   = _Color(*self.color)
            self._hsv           = self.canvas_color.hsv
            self.canvas_shape   = _RoundedRectangle(radius  = self.radius,
                                                    pos     = self.pos,
                                                    size    = self.size)

    def on_size(self, _, size:int):
        """Callback for size change events.

        Whenever the size of the widget is changed, the canvas needs to
        be updated. This is done in this method. Note that this method
        is not meant to be called by the user.

        Args:
            widget: The widget the method was called from.
            size: The new size value.
        """
        if self.canvas and self.canvas.length() > 0:
            self.canvas_shape.size = size

    def on_radius(self, _, radius:_List[int]):
        """Callback for radius change events.

        Whenever the radius of at least one of the widget's corners is
        changed, the canvas needs to be updated. This is done in this
        method. Note that this method is not meant to be called by the
        user.

        Args:
            widget: The widget the method was called from.
            radius: The new radius value.
        """
        if self.canvas and self.canvas.length() > 0:
            self.canvas_shape.radius = radius

    def on_pos(self, _, pos:_List[int]):
        """Callback for position change events.

        Whenever the position of the widget is changed, the canvas
        needs to be updated. This is done in this method. Note that
        this method is not meant to be called by the user.

        Args:
            widget: The widget the method was called from.
            pos: The new position value.
        """
        if self.canvas and self.canvas.length() > 0:
            self.canvas_shape.pos = pos

    def on_color(self, _, color:_List[float]):
        """Callback for changing the nominal (unmodified) color.

        Whenever a color transition is performed using the recolor()
        method, this callback-method is called by Kivy's Animation class
        whenever there is a change in color. Note that this method is
        not meant to be called by the user.

        Args:
            widget: The widget the method was called from.
            color: The new color value.
        """
        if self.canvas and self.canvas.length() > 0:
            self.canvas_color.rgba  = color
            self._hsv = self.canvas_color.hsv

    def on__hsv(self, _, hsv:_List[float]):
        """Callback for animating the color modification in hsv space.

        In order to avoid weired looking color transitions, a
        modification of the widget's color is done in HSV-space.
        Therefore, this method is called whenever Kivy's Animation
        class calls it. Note that this method is not meant to be called
        by the user.

        Args:
            widget: The widget the method was called from.
            hsv: The new hsv value.
        """
        self.canvas_color.hsv = hsv

    def modify(self, hsv:_List[float]):
        """Shifts the widget's color in HSV-space.

        Modifies the nominal color of the widget in HSV-space (hue,
        saturation and value) using a smooth color transition. The
        given values are not absolute ones but differences to the
        current nominal color. For example, to make a widget with name
        myWidget slightly darker, one may call
        ```py
        myWidget.modify([0, 0, -0.2])
        ```
        to reduce the widget's value (meaning brightness) by 0.2.
        The modification can be easily undone by calling the function
        with zero values for all HSV-components, e.g.:
        ```py
        myWidget.modify([0, 0, 0])
        ```

        Args:
            hsv: List of hue, saturation, and value (brightness) values
            to shift the color of the widget.
        """
        targethue       = _modf(_Color(*self.color).h + hsv[0])[0]
        targethue       = targethue if targethue > 0 else 1 - targethue
        refsaturation   = _Color(*self.color).s
        refvalue        = _Color(*self.color).v
        target          = [ targethue,
                            max(min(refsaturation + hsv[1], 1),0),
                            max(min(refvalue + hsv[2], 1),0)]
        _Animation(_hsv = target, duration = self.transition, t='linear').start(self)

    def recolor(self, rgba:_List[float]):
        """Changes the nominal color of the widget.

        Changes the nominal color by smoothly transitioning to the given
        color. The color to transition to is given as a list of float
        values between 0 and 1 in RGBA-space, i.e. [red, green, blue,
        alpha]. Unlike the modify-method, the change cannot be undone
        just as easily. For that, the user needs to store the old color
        in another variable and call recolor with that variable again.

        Args:
            rgba: The new color as a list in RGBA-space to transition
            to. Each list component is a float value between 0 and 1.
        """
        _Animation(color = rgba, duration = self.transition, t='linear').start(self)

    def resize(self, targetsize:_List[int], targetradius:_Optional[_List[int]] = None):
        """Starts an animated change of the widget's size and radius.

        The method smoothly resizes the widget relative to its center.
        Both, the widget size and its radius are transformed.

        Args:
            targetsize: List of the size in pixels in x- and y-direction
            to grow or shrink the widget to.
            targetradius: List of radii in pixels for each of the four
            corners to grow or shrink to. The parameter is optional. If
            not given, the radius of each corner will be automatically
            scaled according to the given targetsize. However, it is
            recommended to explicitly provide a radius every once in
            a while (if the method is used multiple times) to avoid
            a summation of rounding errors.
        """
        delta       = [self.size[0] - targetsize[0], self.size[1] - targetsize[1]]
        newradius   = targetradius
        if not targetradius:
            mpl       = min(targetsize[0] / self.size[0], targetsize[1] / self.size[1])
            newradius = [   self.radius[0]*mpl, self.radius[1]*mpl,
                            self.radius[2]*mpl, self.radius[3]*mpl]

        _Animation( size     = targetsize,
                    radius   = newradius,
                    pos      = [self.pos[0] + delta[0] / 2, self.pos[1] + delta[1] / 2],
                    duration = self.transition, t='linear').start(self)
