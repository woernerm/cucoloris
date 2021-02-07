"""Defines solid and outline button widgets.

This file defines button widgets for solid and outline buttons similar
to the Bootstrap classes btn-primary, btn-secondary,
btn-outline-primary, btn-outline-secondary, etc.
"""

from os.path import dirname as _dirname
from typing import List as _List

from kivy.lang.builder import Builder as _Builder
from kivy.properties import ListProperty as _ListProperty
from kivy.properties import ObjectProperty as _ObjectProperty
from kivy.properties import StringProperty as _StringProperty
from kivy.properties import BooleanProperty as _BooleanProperty
from kivy.uix.behaviors.focus import FocusBehavior as _FocusBehaviour
from kivy.input.motionevent import MotionEvent as _MotionEvent

from ._box import Box as _Box
from ._settings import Settings as _Settings


_Builder.load_file(_dirname(__file__) + '\\button.kv')

class Btn(_FocusBehaviour, _Box):
    """Widget for drawing a touchable / clickable button.

    This widget is the base class of a button that has similar behavior
    to the btn class of Bootstrap. From this base class the classes
    SolidButton and OutlineButton are derived modelling buttons similar
    to the btn and btn-outline classes of Bootstrap.
    """

    padding         = _ListProperty([0,0])
    """Padding of the button's label in pixels.

    Buttons use the system fonts available on the device. Some fonts may
    have slightly weird baselines, e.g. Segoe Ui on Windows. Therefore,
    the padding is adjusted based on the font used.
    """

    font_size       = _StringProperty()
    """The font size used for the button's label in pixels."""

    underline       = _BooleanProperty()
    """Determines, whether the button's label text is underlined.

    An underline is typically used for hyperlinks. The value can be
    either True (text will be underlined) or False (text will not be
    underlined).
    """

    hover_fill      = _ListProperty()
    """HSV-color fill offsets used for hovering.

    If the cursor hovers over the button, its fill color is slightly
    modified. More precisely, its hue, saturation and brightness values
    are shifted by the amount specified with this attribute. Note that
    the values range from 0 to 1.
    """

    press_fill      = _ListProperty()
    """HSV-color fill offsets used, if the button is pressed.

    If the button is pressed, its fill color is slightly
    modified. More precisely, its hue, saturation and brightness values
    are shifted by the amount specified with this attribute. Note that
    the values range from 0 to 1.
    """

    hover_text      = _ListProperty()
    """HSV-color text offsets used for hovering.

    If the cursor hovers over the button, its text color is slightly
    modified. More precisely, its hue, saturation and brightness values
    are shifted by the amount specified with this attribute. Note that
    the values range from 0 to 1.
    """

    press_text      = _ListProperty()
    """HSV-color text offsets used, if the button is pressed.

    If the button is pressed, its text color is slightly
    modified. More precisely, its hue, saturation and brightness values
    are shifted by the amount specified with this attribute. Note that
    the values range from 0 to 1.
    """

    text_color      = _ListProperty()
    """The default color of the button text.

    The color of the button text needs to be specified as RGBA values
    between 0 and 1.
    """

    text            = _StringProperty()
    """The text with which the button is labeled.

    The button text also determines the button's overall size.
    """

    _label          = _ObjectProperty()
    """Private attribute for the button's label object."""

    def __init__(self, text:str = None, font_size:str = None, text_color:_List = None,
                 underline:bool=False, **kwargs):
        """Initialization method of the class.

        Args:
            text: The text of the button.
            font_size: The font size of the button text in pixels.
            text_color: The color of the button text as RGBA values
            between 0 and 1.
            underline: Set to True to underline the button text. False,
            otherwise.
            **kwargs: Keyed arguments passed on to the base classes.
        """

        self.text       = text if text else self.text
        self.font_size  = font_size if font_size else self.font_size
        self.text_color = text_color if text_color else self.text_color
        self.underline  = underline


        super(Btn, self).__init__(**kwargs)
        self.bind( on_enter     = self.on_enter,
                   on_leave     = self.on_leave,
                   on_press     = self.on_press,
                   on_release   = self.on_release)

    def on_enter(self, _):
        """Callback for cursor hover events.

        If the cursor enters the button area and hovers over it, this
        callback method is called. It can be used to modify the
        button's colors.
        """

    def on_leave(self, _):
        """Callback for end of hover events.

        If the cursor leaves the button area and stops to hovers over
        it, this callback method is called. It can be used to modify
        the button's colors.
        """

    def on_release(self, _):
        """Callback for button release events.

        If the button is released, this callback method is called.
        """

    def on_press(self, _):
        """Callback for button press events.

        If the button is pressed, this callback method is called.
        """

    def on_focus(self, _, value:bool):
        """Callback for button focus events.

        If the button gets focus, this callback method is called. One
        can focus on the button by either pressing it or pressing tab
        until the button is focused on.
        """
        if value:
            self.show_shadow()
        else:
            self.hide_shadow()

    def on__label(self, _, __):
        """Callback method for initializing the label.

        If the button label is initialized, this method is called. It
        is used to set the default font, font_size and padding depending
        on the host device and selected color scheme.
        """
        self._label.font_name = _Settings.get_font_name()


class SolidBtn(Btn):
    """This widget represents a button with solid fill color.

    The widget represents a button similar to the typical Bootstrap
    buttons btn-primary, btn-secondary, etc. It can shift its color
    while the cursor is hovering over it or the button is pressed.
    There is also a shadow surrounding the button to indicate focus.
    """

    def on_enter(self, hover:bool):
        """Callback for cursor hover events.

        If the cursor enters the button area and hovers over it, this
        callback method is called. It can be used to modify the
        button's colors.

        Args:
            hover: True, if the cursor hovers over the button. False,
            otherwise.
        """
        super(SolidBtn, self).on_enter(hover)
        self.fill.modify(self.hover_fill)
        self.border.modify(self.hover_fill)
        self._label.modify(self.hover_text)

    def on_leave(self, hover:bool):
        """Callback for end of hover events.

        If the cursor leaves the button area and stops to hovers over
        it, this callback method is called. It can be used to modify
        the button's colors.

        Args:
            hover: True, if the cursor hovers over the button. False,
            otherwise.
        """
        super(SolidBtn, self).on_leave(hover)
        if not self.ispressed() and not self.focus:
            self.fill.modify([0, 0, 0])
            self.border.modify([0, 0, 0])
            self._label.modify([0, 0, 0])

    def on_release(self, touch:_MotionEvent):
        """Callback for button release events.

        If the button is released, this callback method is called.

        Args:
            touch: Motion event with more information about the release.
        """
        super(SolidBtn, self).on_release(touch)
        if self.ishover():
            self.fill.modify(self.hover_fill)
            self.border.modify(self.hover_fill)
            self._label.modify(self.hover_text)
        elif self.focus:
            self.fill.modify(self.hover_fill)
            self.border.modify(self.hover_fill)

    def on_focus(self, _, value:bool):
        """Callback for button focus events.

        If the button gets focus, this callback method is called. One
        can focus on the button by either pressing it or pressing tab
        until the button is focused on.

        Args:
            value: True, if the button has focus. False, otherwise.
        """
        if value:
            self.show_shadow()
            self.fill.modify(self.hover_fill)
            self.border.modify(self.hover_fill)
            self._label.modify(self.hover_text)
        else:
            self.hide_shadow()
            if not self.ishover():
                self.fill.modify([0, 0, 0])
                self.border.modify([0, 0, 0])
                self._label.modify([0, 0, 0])

    def on_press(self, touch:_MotionEvent):
        """Callback for button press events.

        If the button is pressed, this callback method is called.

        Args:
            touch: Motion event with more information about the release.
        """
        super(SolidBtn, self).on_press(touch)
        self.fill.modify(self.press_fill)
        self.border.modify(self.press_fill)
        self._label.modify(self.press_text)


class SolidLinkBtn(SolidBtn):
    """A button with a solid fill color for links.

    The solid link button has a similar hover animation to SolidBtn.
    However, the color transition is applied to the link text only.
    """

    def on_leave(self, hover:bool):
        """Callback for end of hover events.

        If the cursor leaves the button area and stops to hovers over
        it, this callback method is called. It can be used to modify
        the button's colors.

        Args:
            hover: True, if the cursor hovers over the button. False,
            otherwise.
        """
        self.fill.modify([0, 0, 0])
        self.border.modify([0, 0, 0])
        self._label.modify([0, 0, 0])


class OutlineBtn(Btn):
    """Button widget with no fill color.

    The outline button has a hover animation that transitions its fill
    color from background color to the border color while often
    switching the text color from border color to white. It is similar
    to the Bootstrap button classes btn-outline-primary,
    btn-outline-secondary, etc.
    """

    def on_enter(self, _):
        """Callback for cursor hover events.

        If the cursor enters the button area and hovers over it, this
        callback method is called. It can be used to modify the
        button's colors.
        """
        self.fill.recolor(self.hover_fill)
        self._label.recolor(self.hover_text)

    def on_leave(self, _):
        """Callback for end of hover events.

        If the cursor leaves the button area and stops to hovers over
        it, this callback method is called. It can be used to modify
        the button's colors.
        """
        self.fill.recolor(self.fill_color)
        self._label.recolor(self.text_color)

    def on_release(self, _):
        """Callback for button release events.

        If the button is released, this callback method is called.
        """
        if self.ishover():
            self.fill.recolor(self.hover_fill)
            self._label.recolor(self.hover_text)

    def on_focus(self, _, value:bool):
        """Callback for button focus events.

        If the button gets focus, this callback method is called. One
        can focus on the button by either pressing it or pressing tab
        until the button is focused on.

        Args:
            value: True, if the button has focus. False, otherwise.
        """
        if value:
            self.show_shadow()
            self.fill.recolor(self.hover_fill)
            self._label.recolor(self.hover_text)
        else:
            self.hide_shadow()
            if not self.ishover():
                self.fill.recolor(self.fill_color)
                self._label.recolor(self.text_color)

    def on_press(self, touch:_MotionEvent):
        """Callback for button press events.

        If the button is pressed, this callback method is called.

        Args:
            touch: Motion event with more information about the release.
        """
        super(OutlineBtn, self).on_press(touch)
        self.fill.recolor(self.press_fill)
        self._label.recolor(self.press_text)
