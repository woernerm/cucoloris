"""Defines a scroll bar that fits the rounded edges of other widgets.

The standard scroll bar of a ScrollView widget has sharp corners.
However, that does not fit the rounded Bootstrap shapes well.
Therefore, this widget defines a new scroll bar with rounded corners
and the ability to define separate border and fill colors of the
scroll bar.
"""

from os.path import dirname as _dirname

from kivy.lang.builder import Builder as _Builder
from kivy.properties import NumericProperty as _NumericProperty
from kivy.properties import StringProperty as _StringProperty

from ._box import Box as _Box


_Builder.load_file(_dirname(__file__) + '\\_scrollbar.kv')

class ScrollBar(_Box):
    """Widget for a scroll bar with rounded corners.

    The standard scroll bar of a ScrollView widget has sharp corners.
    However, that does not fit the rounded Bootstrap shapes well.
    Therefore, this widget defines a new scroll bar with rounded corners
    and the ability to define separate border and fill colors of the
    scroll bar.
    """

    bar_orientation         = _StringProperty()
    """The orientation of the scroll bar.

    The orientation value may either be 'vertical' or 'horizontal'.
    """

    bar_length              = _NumericProperty()
    """The length of the scroll bar in pixels.

    Typically, the length of the scroll bar depends on the ratio of the
    scroll areas size and the size of the document being scrolled.
    """

    STR_VERTICAL            = 'vertical'
    """Constant defining the vertical scroll bar orientation value."""

    STR_HORIZONTAL          = 'horizontal'
    """Constant defining the horizontal scroll bar orientation value."""

    bar_width               = _NumericProperty()
    """The width of the scroll bar in pixels.

    The width of the scroll bar can be set to taste. It is given in
    pixels.
    """

    def on_bar_orientation(self, _, orientation:str):
        """Determines the validity of the selected orientation value.

        This is a callback method determines whether the selected
        orientation value is valid or not. If the value is valid, the
        scroll bar geometry gets updated. If the valid is invalid,
        an Exception is raised.

        Args:
            orientation: The desired orientation of the scroll bar.
            Can be either 'vertical' or 'horizontal'.
        """
        if orientation in (ScrollBar.STR_VERTICAL, ScrollBar.STR_HORIZONTAL):
            self._update(self.bar_length)
            return
        raise Exception('Orientation must be "veritcal" or "horizontal". Got "' + orientation + '"')

    def _update(self, length:int):
        """Updates the scroll bar geometry.

        Updates the dimensions of the scroll bar based on the selected
        orientation and length. This method needs to be called whenever
        either the orientation or the length of the scroll bar changes.

        Args:
            length: The desired length of the scroll bar.
        """
        if self.bar_orientation == ScrollBar.STR_VERTICAL:
            minv            = max(self.radius[0] + self.radius[3], self.radius[1] + self.radius[2])
            self.bar_length = max(length, minv)
        elif self.bar_orientation == ScrollBar.STR_HORIZONTAL:
            minh            = max(self.radius[0] + self.radius[1], self.radius[2] + self.radius[3])
            self.bar_length = max(length, minh)

    def on_bar_length(self, _, length:int):
        """Callback for scroll bar length changes.

        This is a callback method that gets called whenever the length
        of the scroll bar is changed. It then triggers an update of the
        scroll bar's dimensions.

        Args:
            length: The desired length of the scroll bar in pixels.
        """
        self._update(length)
