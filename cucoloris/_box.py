"""Module for a basic box shape.

This module defines a basic box with optional shadow. It has separate
shadow, border and fill colors as well as rounded corners.
The box is composed of three ColorArea widgets which are set up as
public attributes so that they can be accessed and modified
individually.
"""

# Import of built-in Python modules.
from os.path import dirname as _dirname
from typing import List as _List

# Inport of third-party modules
from kivy.core.window import Window as _Window
from kivy.input.motionevent import MotionEvent as _MotionEvent
from kivy.lang.builder import Builder as _Builder
from kivy.properties import ListProperty as _ListProperty
from kivy.properties import NumericProperty as _NumericProperty
from kivy.properties import ObjectProperty as _ObjectProperty
from kivy.uix.widget import Widget as _Widget


_Builder.load_file(_dirname(__file__) + '\\_box.kv')

class Box(_Widget):
    """Widget for a basic box shape.

    The widget represents a basic box with optional shadow. It has
    separate shadow, border and fill colors as well as rounded corners.
    The box is composed of three ColorArea widgets which are set up as
    public attributes so that they can be accessed and modified
    individually. Since each child is a ColorArea widget, the box
    supports smooth color transitions and size changes for each
    child widget.

    The box can detect touch and hover events that can be used to
    trigger custom color transitions and size changes from any derived
    class.
    """

    # Geometry
    radius              = _ListProperty()
    """The radius of each corner of the widget in pixels.

    The Box widget is a rounded rectangle. Each of the four
    corners may have a different radius given in pixels, e.g.
    [2, 4, 3, 8].
    """

    border_width        = _NumericProperty()
    """The width of the widget's border.

    There is a solid border drawn around the widget. The width of that
    border can be set using this attribute.
    """

    shadow_width        = _NumericProperty()
    """The width of the widget's shadow.

    The widget can be highlighted by a shadow in order to indicate
    focus or to give the widget a three-dimensional look. The width of
    that shadow can be adjusted by this attribute.
    """

    # Color
    fill_color          = _ListProperty()
    """The fill color of the widget.

    The widget is composed of three ColorArea widgets. The color of the
    innermost ColorArea can be set by this attribute. It represents the
    fill color of the Box widget.
    """

    border_color        = _ListProperty()
    """The color of the widget's border.

    There is a solid border drawn around the widget. The color of that
    border can be set using this attribute.
    """

    shadow_color        = _ListProperty()
    """The color of the widget's shadow.

    The widget can be highlighted by a shadow in order to indicate
    focus or to give the widget a three-dimensional look. The color of
    that shadow can be adjusted by this attribute.
    """

    # Animation
    transition          = _NumericProperty()
    """Transition time in seconds.

    The box widget can be highlighted by a shadow in order to indicate
    focus. The shadow smoothly appears from behind the widget. The time
    it takes for the shadow to reach its final size is determined by
    this attribute. The attribute is also the speed with which each
    component can transition to another color, if needed.
    """

    # Child Widgets
    fill                = _ObjectProperty()
    """The ColorArea widget representing the fill color.

    The widget is composed of three ColorArea widgets. The innermost
    one represents the fill color. It can be accessed directly through
    this attribute for more control.
    """

    border              = _ObjectProperty()
    """The ColorArea widget representing the border.

    The widget is composed of three ColorArea widgets. The one on the
    middle layer represents the border color. It can be accessed
    directly through this attribute for more control.
    """

    shadow              = _ObjectProperty()
    """The ColorArea widget representing the shadow.

    The widget is composed of three ColorArea widgets. The outermost
    widget represents the shadow. It can be accessed directly through
    this attribute for more control.
    """

    def __init__(self, *args, **kwargs):
        """Initialization function of the widget.

        The __init__ method is typically called without arguments. Any
        arguments given are passed on the the base class Widget.

        Args:
            *args: Positional arguments passed on to the base class.
            **kwargs: Keyed arguments passed on to the base class.
        """
        super(Box, self).__init__(*args, **kwargs)
        _Window.bind(mouse_pos = self.on_mouse_pos)
        self._inside      = False
        self._pressed     = False
        self.callbacks    = {   'on_enter': None,
                                'on_leave': None,
                                'on_press': None,
                                'on_release': None,
                                'on_drag': None}

    def bind(self, **kwargs):
        """Bind a callback function to one an event.

        The Box widget can react to multiple events and call a specified
        callback function whenever such an event occurs. The following
        events are available:
        * on_enter: The mouse enters the widget space.
        * on_leave: The mouse leaves the widget space.
        * on_down: There is a touch or click on the widget.
        * on_release: The touch or click is released.
        * on_drag: There was a touch or click on the widget and the
        input device is now moved without releasing the touch or click.

        Args:
            **kwargs: Keyed argument list to be passed on to the bound
            callback function.
        """
        for key in kwargs:
            if not key in self.callbacks:
                Exception("Event " + key + " is unknwon.")
            self.callbacks[key] = kwargs[key]

    def show_shadow(self):
        """Highlights the widget by a shadow.

        The box widget can be highlighted by a shadow in order to
        indicate focus. The shadow smoothly appears from behind the
        widget. If focus is lost, the shadow can disappear.
        This method highlights the widget by a shadow.
        """
        self.shadow.resize(self.size)

    def hide_shadow(self):
        """Hides the shadow of the widget.

        The box widget can be highlighted by a shadow in order to
        indicate focus. The shadow smoothly appears from behind the
        widget. If focus is lost, the shadow can be hidden by using
        this method.
        """
        self.shadow.resize(self.border.size, self.border.radius)

    def ispressed(self):
        """Returns, whether the Box is currently touched.

        The method will return true, if the Box widget is currently
        touched, i.e. the touch occured within or on the widget's border
        (the shadow is ignored) and has not yet been released. The
        method will also return true, if the touch device leaves the
        widget without releasing the touch (dragging).

        Returns:
            bool: True, if the widget is currently touched. False,
            otherwise.
        """
        return self._pressed

    def ishover(self):
        """ Returns, whether the cursor is hovering over the widget.

        The method will return true, if the cursor is currently hovering
        on or within the widget's border (the shadow is ignored).

        Returns:
            bool: True, if the cursor is currently hovering over the
            widget. False, otherwise.
        """
        return self._inside

    def on_mouse_pos(self, _, pos:_List[int]):
        """Callback function for detecting mouse movements.

        The method is called for each cursor movement. It is used to
        detect, whether the cursor hovers over the box. If the cursor
        starts to hover over or leaves the Box, then the callback
        functions for 'on_enter' or 'on_leave' are called, respectively.
        Note that the user must have bound a callback functions to those
        events prior to the event's occurrence. Otherwise, nothing
        happens.

        Args:
            pos: The new position value.
        """
        if not self.callbacks['on_enter'] and not self.callbacks['on_leave']:
            return

        if self.collide_point(*pos):
            if not self._inside and self.callbacks['on_enter']:
                self.callbacks['on_enter'](True)
            self._inside = True
        else:
            if self._inside and self.callbacks['on_leave']:
                self.callbacks['on_leave'](False)
            self._inside = False

    def on_touch_down(self, touch:_MotionEvent):
        """Callback function for detecting touches.

        The method is called for each touch / click from the user. The
        method checks whether the touch was performed on or within
        the border of the Box (the shadow is ignored). If so, it calls a
        callback function that was bound to the event 'on_press' using
        the bind() method of this class.

        Args:
            touch: Information about the touch.
        """
        if self.collide_point(*touch.pos):
            self._pressed = True
            if self.callbacks['on_press']:
                self.callbacks['on_press'](touch)

        super(Box, self).on_touch_down(touch)
        return False

    def on_touch_up(self, touch:_MotionEvent):
        """Callback function for detecting touch or click releases.

        The method is called whenever a prior touch / click is released.
        If so, it calls the callback function that was bound to the
        event 'on_press' using the bind() method of this class.

        Args:
            touch: Information about the touch.
        """
        self._pressed = False
        if self.callbacks['on_release']:
            self.callbacks['on_release'](touch)

        super(Box, self).on_touch_up(touch)
        return False

    def on_touch_move(self, touch:_MotionEvent):
        """Callback function for detecting a dragging movement.

        The method is called whenever the input devices moves. It
        checks whether there was a touch or click on the Box before
        which corresponds to dragging the Box. If so, the methods calls
        the callback function that was bound to the event 'on_drag'
        using the bind() method of this class.

        Args:
            touch: Information about the touch.
        """

        if self._pressed and self.callbacks['on_drag']:
            self.callbacks['on_drag'](touch)

        super(Box, self).on_touch_move(touch)
        return False
