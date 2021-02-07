"""Defines a text input that fixes some bugs in Kivy."""

from os.path import dirname as _dirname

from kivy.lang.builder import Builder as _Builder
from kivy.uix.textinput import TextInput as _TextInput

_Builder.load_file(_dirname(__file__) + '\\plaininput.kv')

class PlainInput(_TextInput):
    """Class that provides a plain text input area.

    Although there is already a text input provided in Kivy, there seems
    to be a bug in that widget's cursor position (at least in kivy 2.0).
    If one types in text and reaches the end of a non-multiline
    text input, the cursor may overflow the text input, i.e. the cursor 
    is outside the text input widget. This is even more present if a 
    long text is pasted into the widget. Then, the cursor will be way 
    outside the widget. To work around that issue, this class inherits
    from Kivy's text input and overwrites the necessary function. <br/>
    The cursor position is compared with the position of the right
    border of the text input. If the cursor is right of the text input,
    the cursor is moved to the left and to the right. This will put the
    cursor back into the confines of the text input. Since the movement
    is first left, then right, there will be no movement in sum.
    """

    def insert_text(self, substring:str, from_undo:bool=False):
        """Overwritten version of insert_text to fix the Kivy bug.

        Args:
            substring: The string to be added to the widget.
            from_undo: Set to True, if the substring is a result of an
            undo operation, False otherwise.

        Returns:
            The return value of the base classes version of the method.
        """
        super(PlainInput, self).insert_text(substring, from_undo=from_undo)
        if self.cursor_pos[0] >= self.pos[0] + self.size[0]:
            self.do_cursor_movement('cursor_left')
            self.do_cursor_movement('cursor_right')
            