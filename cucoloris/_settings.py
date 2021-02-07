"""Defines a class for settings.

The settings class is used to select the correct settings, e.g. font,
for the current system.
"""

from sys import platform as _platform

class Settings:
    """Class for determining the correct settings.

    Settings like the font and corrective font offset (to move the font
    baseline up or down for correct vertical centering) are determined
    by this class. These depend on the platform and the font being used.
    For example, on Windows, Segoe UI is used as font. Unfortunately,
    that font has a weird baseline, making it appear off-center, even
    if centered vertically. Therefore, the text has to be moved
    slightly.
    """

    @staticmethod
    def get_font_name() -> str:
        """Returns the font name to be used for the current platform.

        Returns:
            Font name appropriate for the current platform.
        """
        if _platform == 'win32':
            return 'segoeui'
        elif _platform == 'darwin':
            return 'SF-UI-Text-Regular'
        else:
            return 'Roboto-Regular'

    @staticmethod
    def get_font_baseline_offset() -> int:
        """Returns a corrective offset in y-direction.

        On Windows, Segoe UI is used as font. Unfortunately, that font
        has a weird baseline, making it appear off-center, even if
        centered vertically. Therefore, the text has to be moved
        slightly. How much, it needs to move is determined by the
        returned value.

        Returns:
            Vertical offset in pixels.
        """
        if _platform == 'win32':
            return -1

    @staticmethod
    def get_scroll_threshold() -> int:
        """Determines scroll_distance of a ScrollView widget.

        On a mobile device it makes sense to have a threshold before
        starting to scroll down. However, on a desktop computer, this
        behavior can quickly become annoying. Therefore, this threshold
        is chosen depending on the current platform.
        """
        if _platform == 'win32':
            return 0
        elif _platform == 'darwin':
            return 0
        else:
            return 20

    @staticmethod
    def get_scroll_type() -> list:
        """Determines scroll_type of a ScrollView widget.

        On a mobile device it makes sense to have scroll down content
        by touching the text. However, on a desktop computer, this#
        behavior can quickly become annoying. In addition, it makes
        selecting text more difficult on a desktop computer. Therefore,
        the behavior is chosen depending on the platform.
        """
        if _platform == 'win32':
            return ['bars']
        elif _platform == 'darwin':
            return ['bars']
        else:
            return ['bars', 'content']
