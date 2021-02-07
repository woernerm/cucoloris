"""Defines a text input widget with markup support."""

from os.path import dirname as _dirname

from kivy.lang.builder import Builder as _Builder
from kivy.properties import ObjectProperty as _ObjectProperty
from kivy.properties import StringProperty as _StringProperty
from kivy.properties import BooleanProperty as _BooleanProperty
from kivy.properties import ListProperty as _ListProperty
from kivy.properties import NumericProperty as _NumericProperty
from kivy.uix.widget import Widget as _Widget

_Builder.load_file(_dirname(__file__) + '\\markupinput.kv')

class MarkupInput(_Widget):
    """A text input widget with markup support.

    Kivy's standard text input field has some bugs at the time of this
    writing (version 2.0). For example, the caret may leave the text
    input area, if text is pasted inside the input. Therefore, Cucoloris
    offers improved replacements, one with the addition of markup
    support. If the text field has focus, the text can be edited in
    plain text mode. Markup as described in
    https://kivy.org/doc/stable/api-kivy.core.text.markup.html. Markup
    commands can be mixed with other text. Once focus is lost, the text
    field is displayed with all markup formatting applied. This is done
    by overlaying a TextField widget with a Label widget. Opacity of the
    two is toggled between zero and one depending on whether to display
    plain or formatted text.
    """

    text                    = _StringProperty()
    """The text in the widget."""

    _edit                   = _ObjectProperty()
    """Private attribute for the actual text input."""

    _display                = _ObjectProperty()
    """Private attribute for the label to display markup."""

    markup                  = _BooleanProperty()
    """Switch to enable or disable markup support.

    Set to True if you want the widget to support markup commands.
    False, otherwise.
    """

    foreground_color        = _ListProperty()
    """Color of the text.

    The color is given as a list of RGBA values between 0 and 1.
    """

    cursor_color            = _ListProperty()
    """Color of the caret inside the text input.

    The color is given as a list of RGBA values between 0 and 1.
    """

    selection_color         = _ListProperty()
    """Color of the text selection.

    Note that the text selection is drawn on top of the text. Therefore,
    the selection color should have an alpha value. The color is given
    as a list of RGBA values between 0 and 1.
    """

    hint_text_color         = _ListProperty()
    """Color of the hint text.

    The hint text is shown to the user to indicate what to type into
    the text input. The color is given as a list of RGBA values between
    0 and 1.
    """

    hint_text               = _StringProperty()
    """The hint text to be shown to the user.

    Hint texts are used to indicate what the user is supposed to type.
    It can be used as an alternative to other element labels.
    """

    suggestion_text         = _StringProperty()
    """Suggestion text to display to the user.

    Suggestion texts can be used to increase typing speed by indicating
    what the user might want to type in advance. It can also act as a
    technique to remove dropdowns by displaying the closest values the
    FormControl widget is able to accept.
    """

    background_color        = _ListProperty()
    """The background color of the text input.

    The color is given as a list of RGBA values between 0 and 1.
    """

    multiline               = _BooleanProperty()
    """Switch to enable or disable multiline text.

    Set to True, if you want the widget to support multiple lines of
    text. Set to False, otherwise.
    """

    write_tab               = _BooleanProperty()
    """Switch for either writing tabs or switching between widgets.

    You may select, whether a tab should lead to a loss of focus on the
    widget (True) or the tab is written as text into the text input
    (False).
    """

    line_spacing            = _NumericProperty()
    """Space between two consecutive lines.

    More space increases clarity but also requires a larger widget to
    display the same number of lines.
    """

    def on__edit(self, _, __):
        """Toggle opacity on focus.

        Binds a callback method to a focus event of the TextField widget
        to toggle the opacity whenever the widget acquires or loses
        focus.
        """
        self._edit.bind(focus = self.on_focus)
        self._edit.opacity = 0 if self.text and self.markup else 1

    def on_focus(self, _, infocus):
        """Focus callback.

        The focus callback toggles the opacity between the PlainInput
        and the label widget.
        """
        if not self.markup:
            return

        if infocus:
            self._edit.opacity          = 1
            self._display.opacity       = 0
        elif self._edit.text:
            self._display.opacity       = 1
            self._edit.opacity          = 0

    def on_markup(self, _, __):
        """Callback method for switching markup modes.

        Depending on whether to use markup or not, the opacity of the
        PlainInput and Label child widgets is toggled.
        """
        self._edit.opacity      = 0 if self.text and self.markup else 1
        self._display.opacity   = 1 if self.markup else 0
