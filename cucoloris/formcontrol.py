"""Defines a text input, equivalent to Boostrap's form-control class.

In addition to standard text input functionality, the FormControl
widget also supports markup text, i.e. the user can use BBCode markup
commands like [b]my text[/b] to make it bold or [i]my text[/i] to make
the text italic. Details about the markup commands are provided in
Kivy's documentation:
https://kivy.org/doc/stable/api-kivy.core.text.markup.html
"""

from os.path import dirname as _dirname
from typing import Optional as _Optional

from kivy.lang.builder import Builder as _Builder
from kivy.properties import ListProperty as _ListProperty
from kivy.properties import ObjectProperty as _ObjectProperty
from kivy.properties import NumericProperty as _NumericProperty
from kivy.properties import StringProperty as _StringProperty
from kivy.properties import BooleanProperty as _BooleanProperty

from ._box import Box as _Box
from ._settings import Settings as _Settings


_Builder.load_file(_dirname(__file__) + '\\formcontrol.kv')

class FormControl(_Box):
    """Text input widget similar to Bootstrap's form-control class.

    In addition to standard text input functionality, the FormControl
    widget also supports markup text, i.e. the user can use BBCode
    markup commands like [b]my text[/b] to make it bold or
    [i]my text[/i] to make the text italic. Details about the markup
    commands are provided in Kivy's documentation:
    https://kivy.org/doc/stable/api-kivy.core.text.markup.html
    """
    text_color              = _ListProperty()
    """The color of the text.

    The color has to be given as a list of RGBA values between 0 and 1.
    """

    border_color_focus      = _ListProperty()
    """The color of the border on focus.

    The color has to be given as a list of RGBA values between 0 and 1.
    """

    border_color_normal     = _ListProperty()
    """The color of the border without focus.

    The color has to be given as a list of RGBA values between 0 and 1.
    """

    text                    = _StringProperty()
    """The text displayed in the widget.

    The text may contain markup commands as described in the Kivy
    documentation:
    https://kivy.org/doc/stable/api-kivy.core.text.markup.html
    """

    padding                 = _ListProperty([12, 7])
    """ The text padding in pixels.

    The text is padded to give it some space inside the box shape it
    resides in. The padding is given in pixels.
    """

    scroll_bar_width        = _NumericProperty()
    """The width of the scroll bar in pixels.

    The width of the scroll bar can be set to taste. It is given in
    pixels.
    """

    num_lines               = _NumericProperty()
    """The number of lines the FomControl widget shall display.

    This is the number of lines that are shown simultaneously without
    the need for scrolling. This attribute also determines the size of
    the widget, i.e. the widget's size attribute is set depending on
    the value of this attribute.
    """

    line_spacing            = _NumericProperty()
    """Space between two consecutive lines.

    More space increases clarity but also requires a larger widget to
    display the same number of lines.
    """

    selection_color         = _ListProperty()
    """The color of text selection.

    The selection indication is drawn on top of the text. Therefore, the
    color should always have an alpha component. The color is given as
    RGBA values between 0 and 1.
    """

    hint_color              = _ListProperty()
    """Color of text hints.

    Text hints can be shown to indicate what the user should type. The
    color is given as a list of RGBA values between 0 and 1.
    """

    bar_fill_color          = _ListProperty()
    """Fill color of the scroll bar.

    The color is given as a list of RGBA values between 0 and 1.
    """

    bar_border_color        = _ListProperty()
    """Color of the scroll bar's border.

    The color is given as a list of RGBA values between 0 and 1.
    """

    hint_text               = _StringProperty()
    """The hint text to be shown to the user.

    Hint texts are used to indicate what the user is supposed to type.
    It can be used as an alternative to other element labels.
    """

    font_size               = _StringProperty()
    """The font size to use for the FormControl widget.

    The font size is given in pixels.
    """

    suggestion_text         = _StringProperty()
    """Suggestion text to display to the user.

    Suggestion texts can be used to increase typing speed by indicating
    what the user might want to type in advance. It can also act as a
    technique to remove dropdowns by displaying the closest values the
    FormControl widget is able to accept.
    """

    markup                  = _BooleanProperty()
    """Determines, whether markup is recognized or not.

    If you want to allow for text formating using markup commands as
    described in the Kivy documentation
    (https://kivy.org/doc/stable/api-kivy.core.text.markup.html),
    you can set this attribute to True. If you want the FormControl
    widget to accept plain text only, set the value to False.
    """

    _input                  = _ObjectProperty()
    """Private attribute for the actual text input widget."""

    _scroll                 = _ObjectProperty()
    """Private attribute for the scroll area widget."""

    _textoffset             = _NumericProperty()
    """Vertical offset depending on the font used in pixels.

    Some fonts may have a weired baseline like Segoe UI for Windows
    devices. This is corrected by this text offset. It is pulled from
    the configuration depending on which font is currently in use, which
    in turn depends on the machine the application is running on.
    """

    def __init__(self, text:_Optional[str] = None, hint_text:_Optional[str] = None,
                 suggestion_text:_Optional[str] = None, markup:bool = True,
                 font_size:_Optional[str] = None, num_lines:_Optional[int] = None, **kwargs):
        """Initialization method of the class.

        Args:
            text: The text to display in the widget.
            hint_text: The hint text to indicate what the user is
            supposed to type.
            suggestion_text: Suggestive text to indicate what the user
            might want to type next.
            markup: Set to True, if you want to allow text formatting
            using a BBCode like syntax described in
            https://kivy.org/doc/stable/api-kivy.core.text.markup.html.
            Set to False, if you want the FormControl widget to accept
            plain text only.
            font_size: The size of the font used in the widget given in
            pixels, e.g. '16sp'.
            num_lines: The number of lines to display without the need
            for scrolling. This parameter also determines the size of
            the FormControl widget.
            **kwargs: Keyed parameters passed on to the base class.
        """

        self.text               = text if text else self.text
        self.hint_text          = hint_text if hint_text else self.hint_text
        self.suggestion_text    = suggestion_text if suggestion_text else self.suggestion_text
        self.markup             = markup
        self.font_size          = font_size if font_size else self.font_size
        self.num_lines          = num_lines if num_lines else self.num_lines

        super(FormControl, self).__init__(**kwargs)

    def on_border_color_normal(self, _, color):
        """
        Sets the border color, if the nominal color is changed.

        Args:
            color: The new nominal color of the border.
        """
        self.border_color = color

    def on__input(self, _, __):
        """Set the font according to the current platform.

        There is a vertical offset for the Windows system font Segoe UI.
        Although the text input might be centered, the font still is
        not. For that reason, the padding option for Kivy's
        textinput widget was not used. Instead, the whole textinput
        is moved slightly up or down depending on the current platform.
        """
        self._input.font_name   = _Settings.get_font_name()
        self._textoffset        = _Settings.get_font_baseline_offset()
        self._input._edit.bind( focus       = self.on_edit_focus,
                                cursor_row  = self.on_cursor_row)

    def on__scroll(self, _, __):
        """Callback for scroll events.
        """
        self._scroll.scroll_distance    = _Settings.get_scroll_threshold()
        self._scroll.scroll_type        = _Settings.get_scroll_type()

    def on_edit_focus(self, _, value):
        """Callback for touching the Focusable.

        Args:
            widget: The widget the method was called from.
            value: Value 1, if the widget has focus, 0 otherwise.
        """
        if value:
            self.border_color = self.border_color_focus
            self.show_shadow()
        else:
            self.border_color = self.border_color_normal
            self.hide_shadow()

    def on_cursor_row(self, _, __):
        """Callback for automatic scrolling.

        In a multi-line textinput, the ScrollView will not automatically
        scroll down if the user's text becomes too long. Using this
        callback, the textinput is automatically scrolled down or
        upwards, always keeping the cursor within the viewport.
        """
        # Is the textinput completly inside the viewport? If so, there is nothing to do.
        if self._input.height <= self._scroll.height:
            return

        cursor_top      = self._input._edit.cursor_pos[1]
        cursor_bottom   = self._input._edit.cursor_pos[1] - self._input.line_height
        viewport_bottom = self._scroll.scroll_y * (self._input.height - self._scroll.height)
        viewport_top    = viewport_bottom + self._scroll.height

        dytop           = cursor_top - viewport_top + self._input.padding[1]
        dybottom        = cursor_bottom - viewport_bottom - self._input.padding[1]

        if dytop >= 0:
            # Cursor left viewport to the top.
            self._scroll.scroll_y = self._scroll.scroll_y + \
                                    self._scroll.convert_distance_to_scroll(0, dytop)[1]
        elif dybottom <= 0:
            # Cursor left viewport to the bottom.
            self._scroll.scroll_y = self._scroll.scroll_y + \
                                    self._scroll.convert_distance_to_scroll(0, dybottom)[1]
        # Ensure that scroll_y stays within 0 and 1.0.
        self._scroll.scroll_y = max(min(self._scroll.scroll_y, 1.0), 0.0)
