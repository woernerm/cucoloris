"""Defines a background widget to create a single-color background."""

from os.path import dirname as _dirname
from typing import Optional as _Optional

from kivy.lang.builder import Builder as _Builder
from kivy.properties import ListProperty as _ListProperty
from kivy.uix.widget import Widget as _Widget

_Builder.load_file(_dirname(__file__) + '\\background.kv')

class Background(_Widget):
    """Simple single-color background.

    Kivy does not provide a background by default. This widget adds one
    that you can select the color of.
    """

    color           = _ListProperty([1, 1, 1])
    """Color of the background.

    The color must be given as RGB values, each between 0 and 1.
    """

    def __init__(self, color:_Optional[list] = None, **kwargs):
        """Initialization method of the widget.

        Args:
            color: The color of the background given as RGB values,
            each between 0 and 1.
            **kwargs: Keyed arguments passed on to the base class
            of the widget.
        """
        self.color = color if color else self.color
        super(Background, self).__init__(**kwargs)
