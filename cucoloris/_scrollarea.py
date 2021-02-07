"""Defines a ScrollArea widget.

Kivy's ScrollView widget has a scroll bar with sharp corners.
However, that does not fit the rounded Bootstrap shapes well.
Therefore, this widget has the same functionality as the original
ScrollView but uses the ScrollBar widget, a scroll bar with rounded
edges.
"""

from os.path import dirname as _dirname
from typing import List as _List

from kivy.lang.builder import Builder as _Builder
from kivy.properties import ListProperty as _ListProperty
from kivy.properties import ObjectProperty as _ObjectProperty
from kivy.uix.widget import Widget as _Widget
from kivy.input.motionevent import MotionEvent as _MotionEvent

_Builder.load_file(_dirname(__file__) + '\\_scrollarea.kv')


class ScrollArea(_Widget):
    """Replacement for Kivy's ScrollView widget.

    Kivy's ScrollView widget has a scroll bar with sharp corners.
    However, that does not fit the rounded Bootstrap shapes well.
    Therefore, this widget has the same functionality as the original
    ScrollView but uses the ScrollBar widget, a scroll bar with rounded
    edges.
    """

    bar_fill_color      = _ListProperty()
    """The fill color of the scroll bar.

    The color must be given as RGBA values, each between 0 and 1.
    """

    bar_border_color    = _ListProperty()
    """The border color of the scroll bar.

    The color must be given as RGBA values, each between 0 and 1.
    """

    bar_radius          = _ListProperty()
    """The radius of the scroll bar's corners.

    The scroll bar can have rounded corners. The list values
    correspond to the corners as follows:
    [upper left, upper right, lower right, lower left]
    """

    _scroll             = _ObjectProperty()
    """Private attribute for the scroll view child widget."""

    @property
    def scroll_x(self):
        """Returns the scroll_x value of the ScrollView child."""
        return self._scroll.scroll_x

    @property
    def scroll_y(self):
        """Returns the scroll_y value of the ScrollView child."""
        return self._scroll.scroll_y

    @property
    def vbar(self):
        """Returns the vbar value of the ScrollView child."""
        return self._scroll.vbar

    @property
    def smooth_scroll_end(self):
        """Returns value smooth_scroll_end of the ScrollView child."""
        return self._scroll.smooth_scroll_end

    @property
    def viewport_size(self):
        """Returns the viewport_size value of the ScrollView child."""
        return self._scroll.viewport_size

    @property
    def scroll_wheel_distance(self):
        """Returns scroll_wheel_distance of the ScrollView child."""
        return self._scroll.scroll_wheel_distance

    @property
    def scroll_type(self):
        """Returns the scroll_type value of the ScrollView child."""
        return self._scroll.scroll_type

    @property
    def scroll_timeout(self):
        """Returns the scroll_timeout value of the ScrollView child."""
        return self._scroll.scroll_timeout

    @property
    def scroll_distance(self):
        """Returns the scroll_distance value of the ScrollView child."""
        return self._scroll.scroll_distance

    @property
    def hbar(self):
        """Returns the hbar value of the ScrollView child."""
        return self._scroll.hbar

    @property
    def effect_y(self):
        """Returns the effect_y value of the ScrollView child."""
        return self._scroll.effect_y

    @property
    def effect_x(self):
        """Returns the effect_x value of the ScrollView child."""
        return self._scroll.effect_x

    @property
    def effect_cls(self):
        """Returns the effect_cls value of the ScrollView child."""
        return self._scroll.effect_cls

    @property
    def bar_pos_y(self):
        """Returns the bar_pos_y value of the ScrollView child."""
        return self._scroll.bar_pos_y

    @property
    def bar_pos_x(self):
        """Returns the bar_pos_x value of the ScrollView child."""
        return self._scroll.bar_pos_x

    @property
    def bar_pos(self):
        """Returns the bar_pos value of the ScrollView child."""
        return self._scroll.bar_pos

    @property
    def bar_margin(self):
        """Returns the bar_margin value of the ScrollView child."""
        return self._scroll.bar_margin

    @property
    def always_overscroll(self):
        """Returns always_overscroll value of the ScrollView child."""
        return self._scroll.always_overscroll

    @property
    def do_scroll_y(self):
        """Returns the do_scroll_y value of the ScrollView child."""
        return self._scroll.do_scroll_y

    @property
    def do_scroll_x(self):
        """Returns the do_scroll_x value of the ScrollView child."""
        return self._scroll.do_scroll_x

    @property
    def bar_width(self):
        """Returns the bar_width value of the ScrollView child."""
        return self._scroll.bar_width

    @scroll_x.setter
    def scroll_x(self, valuex):
        """Sets the scroll_x value of the ScrollView child.

        Args:
            valuex: The value to be set for the x-direction.
        """
        self._scroll.scroll_x = valuex

    @scroll_y.setter
    def scroll_y(self, valuey):
        """Sets the scroll_y value of the ScrollView child.

        Args:
            valuey: The value to be set for the y-direction.
        """
        self._scroll.scroll_y = valuey

    @vbar.setter
    def vbar(self, value):
        """Sets the vbar value of the ScrollView child.

        Args:
            value: The value to be set for vbar.
        """
        self._scroll.vbar = value

    @smooth_scroll_end.setter
    def smooth_scroll_end(self, value):
        """Sets the smooth_scroll_end value of the ScrollView child.

        Args:
            value: The value to be set for smooth_scroll_end.
        """
        self._scroll.smooth_scroll_end = value

    @viewport_size.setter
    def viewport_size(self, value):
        """Sets the viewport_size value of the ScrollView child.

        Args:
            value: The value to be set for viewport_size.
        """
        self._scroll.viewport_size = value

    @scroll_wheel_distance.setter
    def scroll_wheel_distance(self, value):
        """Sets the scroll_wheel_distance value of the ScrollView child.

        Args:
            value: The value to be set for scroll_wheel_distance.
        """
        self._scroll.scroll_wheel_distance = value

    @scroll_type.setter
    def scroll_type(self, value):
        """Sets the scroll_type value of the ScrollView child.

        Args:
            value: The value to be set for scroll_type.
        """
        self._scroll.scroll_type = value

    @scroll_timeout.setter
    def scroll_timeout(self, value):
        """Sets the scroll_timeout value of the ScrollView child.

        Args:
            value: The value to be set for scroll_timeout.
        """
        self._scroll.scroll_timeout = value

    @scroll_distance.setter
    def scroll_distance(self, value):
        """Sets the scroll_distance value of the ScrollView child.

        Args:
            value: The value to be set for scroll_distance.
        """
        self._scroll.scroll_distance = value

    @hbar.setter
    def hbar(self, value):
        """Sets the hbar value of the ScrollView child.

        Args:
            value: The value to be set for hbar.
        """
        self._scroll.hbar = value

    @effect_y.setter
    def effect_y(self, value):
        """Sets the effect_y value of the ScrollView child.

        Args:
            value: The value to be set for effect_y.
        """
        self._scroll.effect_y = value

    @effect_x.setter
    def effect_x(self, value):
        """Sets the effect_x value of the ScrollView child.

        Args:
            value: The value to be set for effect_x.
        """
        self._scroll.effect_x = value

    @effect_cls.setter
    def effect_cls(self, value):
        """Sets the effect_cls value of the ScrollView child.

        Args:
            value: The value to be set for effect_cls.
        """
        self._scroll.effect_cls = value

    @bar_pos_y.setter
    def bar_pos_y(self, value):
        """Sets the bar_pos_y value of the ScrollView child.

        Args:
            value: The value to be set for bar_pos_y.
        """
        self._scroll.bar_pos_y = value

    @bar_pos_x.setter
    def bar_pos_x(self, value):
        """Sets the bar_pos_x value of the ScrollView child.

        Args:
            value: The value to be set for bar_pos_x.
        """
        self._scroll.bar_pos_x = value

    @bar_pos.setter
    def bar_pos(self, value):
        """Sets the bar_pos value of the ScrollView child.

        Args:
            value: The value to be set for bar_pos.
        """
        self._scroll.bar_pos = value

    @bar_margin.setter
    def bar_margin(self, value):
        """Sets the bar_margin value of the ScrollView child.

        Args:
            value: The value to be set for bar_margin.
        """
        self._scroll.bar_margin = value

    @always_overscroll.setter
    def always_overscroll(self, value):
        """Sets the always_overscroll value of the ScrollView child.

        Args:
            value: The value to be set for always_overscroll.
        """
        self._scroll.always_overscroll = value

    @do_scroll_y.setter
    def do_scroll_y(self, value):
        """Sets the do_scroll_y value of the ScrollView child.

        Args:
            value: The value to be set for do_scroll_y.
        """
        self._scroll.do_scroll_y = value

    @do_scroll_x.setter
    def do_scroll_x(self, value):
        """Sets the do_scroll_x value of the ScrollView child.

        Args:
            value: The value to be set for do_scroll_x.
        """
        self._scroll.do_scroll_x = value

    @bar_width.setter
    def bar_width(self, value):
        """Sets the bar_width value of the ScrollView child.

        Args:
            value: The value to be set for bar_width.
        """
        self._scroll.bar_width = value

    def add_widget(self, widget:_List, index:int = 0, canvas=None):
        """Passes on the given child to the ScrollView widget.

        During initialization of the widget's own child, i.e. the
        ScrollView and the ScrollBar widgets, the given widgets are
        added as children of the ScrollArea widget. After initialization
        is complete a widget added from outside the ScrollArea widget
        will be passed on to the ScrollView widget and added there.

        Args:
            widget: The widget to be added as child.
            index: The position in the widget tree. Zero means that
            later widgets will be drawn on top of widgets added earlier.
            See Kivy's documentation for details.
        """
        if not self._scroll:
            super(ScrollArea, self).add_widget(widget, index, canvas)
        else:
            self._scroll.add_widget(widget, index)

    def remove_widget(self, widget:_Widget):
        """Removes a child widget from ScrollArea or ScrollView widget.

        After initialization, the command is passed on to the ScrollView
        widget. Before initialization, the command is applied to the
        ScrollArea widget itself.

        Args:
            widget: The widget to be removed.
        """
        if not self._scroll:
            super(ScrollArea, self).remove_widget(widget)
        else:
            self._scroll.remove_widget(widget)

    def clear_widgets(self, children:_List = None):
        """Removes all children from ScrollArea or ScrollView widget.

        After intialization, the command is passed on to the ScrollView
        widget. Before initialization, the command is applied to the
        ScrollArea widget itself.

        Args:
            children: A list of the current widget's child widgets.
        """
        if not self._scroll:
            super(ScrollArea, self).clear_widgets(children)
        else:
            self._scroll.clear_widgets(children)

    def convert_distance_to_scroll(self, deltax:int, deltay:int):
        """Converts a distance in pixels to a scroll distance.

        This method provides direct access to the interface of the
        ScrollView child widget. For functional details see Kivy's
        documentation.
        """
        return self._scroll.convert_distance_to_scroll(deltax, deltay)

    def scroll_to(self, widget:_Widget, padding:int = 10,
                  animate:bool = True):
        """Scrolls the viewport to the given widget.

        This method provides direct access to the interface of the
        ScrollView child widget. For functional details see Kivy's
        documentation.

        Args:
            widget: The widget to scroll to.
            padding: The padding around the widget to scroll to.
            animate: Set to True for a scroll animation. False
            otherwise.
        """
        return self._scroll.scroll_to(widget, padding, animate)

    def update_from_scroll(self, *largs):
        """Reposition the content according to scroll_x and scroll_y.

        This method provides direct access to the interface of the
        ScrollView child widget. For functional details see Kivy's
        documentation.

        """
        return self._scroll.update_from_scroll(*largs)

    def on_touch_down(self, touch:_MotionEvent):
        """Callback method for touch / click events.

        If the application detects a touch or click, this method is
        called. It passes on the given touch motion event information
        to the ScrollView widget child.

        Args:
            touch: Motion event with details about the touch event.
        """
        return self._scroll.on_touch_down(touch)

    def on_touch_move(self, touch:_MotionEvent):
        """Callback method for touch / cursor motion events.

        If the application detects a cursor or touch motion, this method
        is called. It passes on the given motion event information
        to the ScrollView widget child.

        Args:
            touch: Motion event with details.
        """
        return self._scroll.on_touch_move(touch)

    def on_touch_up(self, touch:_MotionEvent):
        """Callback method for touch / cursor release events.

        If the application detects a cursor or touch release, this
        method is called. It passes on the given release event
        information to the ScrollView widget child.

        Args:
            touch: Motion event with details.
        """
        return self._scroll.on_touch_up(touch)
