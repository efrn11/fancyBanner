"""
Create a simple and easy way to create pretty and distinctive banners and ribbons
for program feedback and fancy printing.
"""


class FancyBanner(object):
    """Base class for types of output"""
    default_width = 100
    hSep = '-'
    vSep = '|'
    errSym = '*'
    pad = ' '
    width = default_width
    innerSize = width

    def __init__(self, width=0):
        """
        Create instance variables used for inherited objects
        :param width:
        """

        # data
        if width > 0:
            self.width = width

        self.innerSize = self.width

    def display(self):
        """ Print """
        print(self)

    def error(self, symbol='*'):
        """
        Replaces the usual symbols used to construct banners with a different symbol to stand out.

        :param symbol: symbol to replace the filler characters. For aesthetics.
        :return: self
        """

        # only use first character of symbol, if more than one are entered
        if len(symbol) > 1:
            symbol = symbol[0]

        # replace variables for instance
        self.hSep = symbol
        self.vSep = symbol
        self.pad = symbol

        return self

    @classmethod
    def width(cls, width):
        cls.width = width


class Inner(FancyBanner):
    """ Modifies message to have an indent offset"""
    def __init__(self, width=0, offset=5):
        super().__init__(width)
        self.indent_offset = offset
        self.indent = '{:^{}}'.format('', self.indent_offset)

    def error(self, symbol='*'):
        """
        Defines errors for classes inheriting from Inner

        :param symbol: symbol to replace the filler characters. For aesthetics.
        :return: self
        """
        self.indent = '{:<{}}'.format(symbol, self.indent_offset)
        return self


class OneSecMain(FancyBanner):
    """One large Box with a center message buffered by surrounding space"""
    def __init__(self, message='', size_int=0):
        super().__init__(size_int)
        self.message1 = message

    def __str__(self):
        """
        Create box and format message into it.

        :return: string representation
        """
        to_string = '\n'
        to_string += '{3}{0:{1}^{2}}{3}'.format('', self.hSep, self.width, self.pad) + '\n'

        to_string += '{2}{0:^{1}}{2}'.format('', self.width, self.vSep) + '\n'
        to_string += '{2}{0:^{1}}{2}'.format(self.message1, self.innerSize, self.vSep) + '\n'
        to_string += '{2}{0:^{1}}{2}'.format('', self.width, self.vSep) + '\n'

        to_string += '{3}{0:{1}^{2}}{3}'.format('', self.hSep, self.width, self.pad) + '\n'

        return to_string


class TwoSecMain(FancyBanner):
    """Create large buffered box with connected unbuffered second box"""
    def __init__(self, message1='', message2='', size_int=0):
        super().__init__(size_int)
        self.message1 = message1
        self.message2 = message2

    def __str__(self):
        """
        Create string

        :return: string
        """
        to_string = '\n'
        to_string += '{3}{0:{1}^{2}}{3}'.format('', self.hSep, self.width, self.pad) + '\n'

        to_string += '{2}{0:^{1}}{2}'.format('', self.width, self.vSep) + '\n'
        to_string += '{2}{0:^{1}}{2}'.format(self.message1, self.innerSize, self.vSep) + '\n'
        to_string += '{2}{0:^{1}}{2}'.format('', self.width, self.vSep) + '\n'

        to_string += '{2}{0:{3}^{1}}{2}'.format('', self.width, self.vSep, self.hSep) + '\n'

        to_string += '{2}{0:^{1}}{2}'.format(self.message2, self.innerSize, self.vSep) + '\n'
        to_string += '{3}{0:{1}^{2}}{3}'.format('', self.hSep, self.width, self.pad) + '\n'

        return to_string


class ThreeSecMain(FancyBanner):
    """Create a large buffered box, with two attatched unbuffered boxes"""

    def __init__(self, message1='', message2='', message3='', size_int=0):
        super().__init__(size_int)
        self.message1 = message1
        self.message2 = message2
        self.message3 = message3

    def __str__(self):
        to_string = '\n'
        to_string += '{3}{0:{1}^{2}}{3}'.format('', self.hSep, self.width, self.pad) + '\n'

        to_string += '{2}{0:^{1}}{2}'.format('', self.width, self.vSep) + '\n'
        to_string += '{2}{0:^{1}}{2}'.format(self.message1, self.innerSize, self.vSep) + '\n'
        to_string += '{2}{0:^{1}}{2}'.format('', self.width, self.vSep) + '\n'

        to_string += '{2}{0:{3}^{1}}{2}'.format('', self.width, self.vSep, self.hSep) + '\n'
        to_string += '{2}{0:^{1}}{2}'.format(self.message2, self.innerSize, self.vSep) + '\n'

        to_string += '{2}{0:{3}^{1}}{2}'.format('', self.width, self.vSep, self.hSep) + '\n'
        to_string += '{2}{0:^{1}}{2}'.format(self.message3, self.innerSize, self.vSep) + '\n'

        to_string += '{3}{0:{1}^{2}}{3}'.format('', self.hSep, self.width, self.pad) + '\n'

        return to_string


class OneSec(FancyBanner):
    """Create small box"""
    def __init__(self, message='', size_int=0):
        super().__init__(size_int)
        self.message = message

    def __str__(self):
        to_string = '\n'
        to_string += '{3}{0:{2}^{1}}{3}'.format('', self.width, self.hSep, self.pad) + '\n'
        to_string += '{2}{0:^{1}}{2}'.format(self.message, self.innerSize, self.vSep) + '\n'
        to_string += '{3}{0:{2}^{1}}{3}'.format('', self.width, self.hSep, self.pad) + '\n'

        return to_string


class TwoSec(FancyBanner):
    """Create two connected small boxes"""
    def __init__(self, message1='', message2='', size_int=0):
        super().__init__(size_int)
        self.message1 = message1
        self.message2 = message2

    def __str__(self):
        to_string = '\n'
        to_string += '{3}{0:{2}^{1}}{3}'.format('', self.width, self.hSep, self.pad) + '\n'
        to_string += '{2}{0:^{1}}{2}'.format(self.message1, self.innerSize, self.vSep) + '\n'
        to_string += '{2}{0:{3}^{1}}{2}'.format('', self.width, self.vSep, self.hSep) + '\n'
        to_string += '{2}{0:^{1}}{2}'.format(self.message2, self.innerSize, self.vSep) + '\n'
        to_string += '{3}{0:{2}^{1}}{3}'.format('', self.width, self.hSep, self.pad) + '\n'

        return to_string


class Ribbon(FancyBanner):
    """Create centered text surrounded with filler char at given width, if supplied"""
    def __init__(self, message='', size_int=0):
        super().__init__(size_int)
        self.message = message

    def __str__(self):
        to_string = '\n'
        to_string = '{2}{0:{2}^{1}}{2}'.format(self.message, self.width, self.hSep) + '\n'
        return to_string


class SmallRibbon(FancyBanner):
    """Create centered text surrounded with filler char at a third of supplied width"""
    def __init__(self, message='', size_int=0):
        super().__init__(size_int)
        self.message = message

    def __str__(self):

        self.innerSize = int(self.width / 3)

        self.message = '{msg:{fill}^{size}}'.format(msg=self.message, fill=self.hSep, size=self.innerSize)
        to_string = '\n'
        to_string = '{2}{0:{2}^{1}}{2}'.format(self.message, self.width, " ") + '\n'
        return to_string


class InnerMessage(Inner):
    """Create indented message"""
    def __init__(self, message='', size_int=0, offset=5):
        super().__init__(size_int, offset)
        self.message = message
        self.width -= size_int

    def __str__(self):
        to_string = '\n'
        self.message = self.indent + self.message
        to_string += '{:<{}}'.format(self.message, self.width)
        return to_string
