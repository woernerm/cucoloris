"""Defines a label that can change color.

The color shift is animated. This can be used for link-style text.
"""

from os.path import dirname as _dirname
from math import modf as _modf
from typing import Optional as _Optional

from kivy.animation import Animation as _Animation
from kivy.graphics import Color as _Color
from kivy.lang.builder import Builder as _Builder
from kivy.properties import ListProperty as _ListProperty
from kivy.properties import NumericProperty as _NumericProperty
from kivy.properties import StringProperty as _StringProperty
from kivy.uix.label import Label as _Label


_Builder.load_file(_dirname(__file__) + '\\_colorlabel.kv')

class ColorLabel(_Label):
    """Label widget that can shift its color.

    The color shift is animated. This can be used for link-style text.
    """

    nominal_color   = _ListProperty([0,0,0,0])
    """Nominal, i.e. unmodied color of the label.

    The color must be given as RGBA values, each between 0 and 1.
    """

    transition      = _NumericProperty()
    """Transition time in seconds.

    The ColorLabel widget transitions smoothly between colors. The time
    it shall take from one color state to another can be set using this
    attribute.
    """

    text            = _StringProperty()
    """The text of the label."""

    _hsv            = _ListProperty()
    """Private parameter representing the current color in HSV-space."""

    def __init__(self, text:_Optional[str] = None, nominal_color:_Optional[list] = None,
                 transition:_Optional[int] = None, **kwargs):
        """Initialization method of the class.

        Args:
            text: The text of the label.
            nominal_color: The nominal, i.e. unmodified color of the
            transition: The time it takes to transition from one color
            to another.
        """
        super(ColorLabel, self).__init__(**kwargs)
        self.text           = text if text else self.text
        self.nominal_color  = nominal_color if nominal_color else self.nominal_color
        self.transition     = transition if transition else self.transition

        self.size_hint      = [None, None]
        self._hsv           = _Color(*self.color).hsv

    def on_nominal_color(self, _, color):
        """Callback for changing the color.

        This callback method changes the nominal, i.e. unmodified
        color of the widget.

        Args:
            color: The new color value.
        """
        self.color  = color
        self._hsv   = _Color(*self.color).hsv

    def on__hsv(self, _, hsv):
        """Callback for animating the color modification in hsv space.

        The color modification takes place in hue, saturation, value
        space in order to avoid weird red color shifts moving through
        several different hues instead of just the brightness (value)
        component of the color.

        Args:
            widget: The widget the method was called from.
            hsv: The new hsv value.
        """
        hcolor      = _Color(*self.nominal_color)
        hcolor.hsv  = hsv
        self.color  = hcolor.rgba

    def modify(self, hsv):
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

        # Since hue is the angle on a color wheel, there is no minimum
        # or maximum value. Hue values larger than one describe multiple
        # revolutions around the color wheel.
        targethue       = _modf(_Color(*self.nominal_color).h + hsv[0])[0]
        targethue       = targethue if targethue > 0 else 1 - targethue
        refsaturation   = _Color(*self.nominal_color).s
        refvalue        = _Color(*self.nominal_color).v
        target          = [ targethue,
                            max(min(refsaturation + hsv[1], 1),0),
                            max(min(refvalue + hsv[2], 1),0)]
        _Animation(_hsv = target, duration = self.transition, t='linear').start(self)

    def recolor(self, color):
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
        _Animation(nominal_color = color, duration = self.transition, t='linear').start(self)
