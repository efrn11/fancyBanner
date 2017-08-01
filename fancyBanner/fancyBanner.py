"""
Create a simple and easy way to create pretty and distinctive banners and ribbons
for program feedback and fancy printing.
"""


class FancyBanner(object):
    default_width = 100

    width = default_width
    innerSize = width
    box = {}
    messages = []

    msg_line = ''

    def __init__(self, *args, width=0, mode='normal'):
        self.messages = []
        # data
        if width > 0:
            self.width = width

        for arg in args:
            self.messages.append(arg)

        if len(self.messages) == 0:
            self.messages.append('')

        self.box_chars = {
            '': {
                'h': '-',
                'v': '|',
                'tl': ' ',
                'tr': ' ',
                'bl': ' ',
                'br': ' ',
                'i': '+',
                'li': '|',
                'ri': '|',
                'ti': '-',
                'bi': '-'
            },
            'error': {
                'h': '-',
                'v': '|',
                'tl': ' ',
                'tr': ' ',
                'bl': ' ',
                'br': ' ',
                'i': '+',
                'li': '|',
                'ri': '|',
                'ti': '-',
                'bi': '-'
            }
        }
        self.innerSize = self.width
        self.box = self.box_chars[mode]



"""
Create a simple and easy way to create pretty and distinctive banners and ribbons
for program feedback and fancy printing.
"""


class FancyBannerUni(object):
    default_width = 100
    width = default_width
    msg_line = ''

    def __init__(self, *args, width=0, mode='normal'):
        self.messages = []
        self.box_chars = {
            'normal': {
                'h': '-',
                'v': '|',
                'tl': ' ',
                'tr': ' ',
                'bl': ' ',
                'br': ' ',
                'i': '+',
                'li': '|',
                'ri': '|',
                'ti': '-',
                'bi': '-'
            },

            'dbl': {
                'h': '-',
                'v': '|',
                'tl': ' ',
                'tr': ' ',
                'bl': ' ',
                'br': ' ',
                'i': '+',
                'li': '|',
                'ri': '|',
                'ti': '-',
                'bi': '-'
            },
            'bold': {
                'h': '-',
                'v': '|',
                'tl': ' ',
                'tr': ' ',
                'bl': ' ',
                'br': ' ',
                'i': '+',
                'li': '|',
                'ri': '|',
                'ti': '-',
                'bi': '-'
            }
        }

        # data
        if width > 0:
            self.width = width

        for arg in args:
            self.messages.append(arg)

        if len(self.messages) == 0:
            self.messages.append('')

        self.width = self.width
        self.box = self.box_chars[mode]

    def top(self):
        """
        ┌────────────────────┐

        :return: 
        """
        return '{ul}{msg:{h}^{width}}{ur}'.format(width=self.width,
                                                  msg='',
                                                  h=self.box['h'],
                                                  ul=self.box['tl'],
                                                  ur=self.box['tr']
                                                  ) + '\n'

    def blank(self):
        """
        │                    │

        :return: 
        """
        return self.msg()

    def msg(self, msg=''):
        """
        │       ~~~~         │

        :param msg: message to print
        :return: 
        """

        return '{v}{msg:^{width}}{v}'.format(msg=msg,
                                             width=self.width,
                                             v=self.box['v']
                                             ) + '\n'

    def bot(self):
        """
        └────────────────────┘

        :return: 
        """
        return '{bl}{msg:{h}^{width}}{br}'.format(width=self.width,
                                                  msg='',
                                                  h=self.box['h'],
                                                  bl=self.box['bl'],
                                                  br=self.box['br']
                                                  ) + '\n'

    def line(self, msg=''):
        """
        ──────────────────────

        :param msg: msg to print
        :return: 
        """
        return '{h}{msg:{h}^{width}}{h}'.format(width=self.width,
                                                msg=msg,
                                                h=self.box['h'],
                                                ) + '\n'

    def line_int(self):
        """
        ├────────────────────┤

        :return: 
        """
        return '{li}{msg:{h}^{width}}{ri}'.format(msg='',
                                                  width=self.width,
                                                  h=self.box['h'],
                                                  li=self.box['li'],
                                                  ri=self.box['ri']
                                                  ) + '\n'

    def top_two_part(self):
        """
         ╔══════════╦══════════╗

        :return: 
        """
        return '{tl}{msg:{h}^{width}}{tr}'.format(width=self.width,
                                                  msg=self.box['ti'],
                                                  h=self.box['h'],
                                                  tl=self.box['tl'],
                                                  tr=self.box['tr']
                                                  ) + '\n'

    def msg_two_part(self, msg1='', msg2=''):
        """
        ║    ~~    ║     ~~    ║

        :param msg1: 
        :param msg2: 
        :return: 
        """

        if self.width % 2 == 0:
            halfsize = int(self.width / 2)
            part1 = '{v}{msg:^{width}}{v}'.format(msg=msg1, width=halfsize - 1, v=self.box['v'])
            part2 = '{msg:^{width}}{v}'.format(msg=msg2, width=halfsize, v=self.box['v'])

        else:
            halfsize = int(self.width / 2) + 1
            part1 = '{v}{msg:^{width}}{v}'.format(msg=msg1, width=(halfsize - 1), v=self.box['v'])
            part2 = '{msg:^{width}}{v}'.format(msg=msg2, width=(halfsize - 1), v=self.box['v'])

        return part1 + part2 + '\n'

    def blank_two_part(self):
        """
        ║          ║           ║

        :return: 
        """
        return self.msg_two_part()

    def line_two_part_top(self):
        """
        ╠══════════╦══════════╣

        :return: 
        """
        return '{li}{msg:{h}^{width}}{ri}'.format(width=self.width,
                                                  msg=self.box['ti'],
                                                  h=self.box['h'],
                                                  li=self.box['li'],
                                                  ri=self.box['ri']
                                                  ) + '\n'

    def line_two_part(self) -> str:
        """
        ╠══════════╬═══════════╣

        :return: str
        """

        return '{li}{msg:{h}^{width}}{ri}'.format(width=self.width,
                                                  msg=self.box['i'],
                                                  h=self.box['h'],
                                                  li=self.box['li'],
                                                  ri=self.box['ri']
                                                  ) + '\n'

    def line_two_part_bot(self):
        """
        ╠══════════╩══════════╣

        :return: 
        """
        return '{li}{msg:{h}^{width}}{ri}'.format(width=self.width,
                                                  msg=self.box['bi'],
                                                  h=self.box['h'],
                                                  li=self.box['li'],
                                                  ri=self.box['ri']
                                                  ) + '\n'

    def bot_two_part(self):
        """
        ╚══════════╩═══════════╝

        :return: 
        """
        return '{bl}{msg:{h}^{width}}{br}'.format(width=self.width,
                                                  msg=self.box['bi'],
                                                  h=self.box['h'],
                                                  bl=self.box['bl'],
                                                  br=self.box['br']
                                                  ) + '\n'

    def display(self):
        print(self)

    def error(self, char='*'):
        """
        Replaces the usual symbols used to construct banners with a different symbol to stand out.

        :param char: symbol to replace the filler characters. For aesthetics.
        :return: self
        """

        self.box = self.box_chars['bold']
        for key in self.box.keys():
            self.box[key] = char[0]

        return self


class OneSec(FancyBannerUni):
    def __init__(self, msg='', width=0):
        super().__init__(msg, width=width)
        self.msgs = self.messages

    def __str__(self):
        to_str = '\n'
        to_str += self.top()
        to_str += self.msg(self.messages[0])
        to_str += self.bot()
        return to_str


class OneSecMain(FancyBannerUni):
    def __init__(self, msg='', width=0):
        super().__init__(msg, width=width, mode='dbl')

    def __str__(self):
        to_str = '\n'
        to_str += self.top()
        to_str += self.blank()
        to_str += self.msg(self.messages[0])
        to_str += self.blank()
        to_str += self.bot()
        return to_str


class OneSecMega(FancyBannerUni):
    def __init__(self, msg='', width=0):
        super().__init__(msg, width=width, mode='dbl')

    def __str__(self):
        to_str = '\n'
        to_str += self.top()
        to_str += self.blank()
        to_str += self.blank()
        to_str += self.msg(self.messages[0].upper())
        to_str += self.blank()
        to_str += self.blank()
        to_str += self.bot()
        return to_str


class TwoSec(FancyBannerUni):
    def __init__(self, msg1='', msg2='', width=0):
        super().__init__(msg1, msg2, width=width)

    def __str__(self):
        to_str = '\n'
        to_str += self.top()
        to_str += self.msg(self.messages[0])

        to_str += self.line_int()

        to_str += self.msg(self.messages[1])
        to_str += self.bot()
        return to_str


class TwoSecHor(FancyBannerUni):
    def __init__(self, msg1='', msg2='', width=0):
        super().__init__(msg1, msg2, width=width)

    def __str__(self):
        to_str = '\n'
        to_str += self.top_two_part()
        to_str += self.msg_two_part()
        to_str += self.bot_two_part()

        return to_str


class TwoSecMain(FancyBannerUni):
    def __init__(self, msg1='', msg2='', width=0):
        super().__init__(msg1, msg2, width=width, mode='dbl')

    def __str__(self):
        to_str = '\n'
        to_str += self.top()
        to_str += self.blank()
        to_str += self.msg(self.messages[0])
        to_str += self.blank()
        to_str += self.line_int()
        to_str += self.msg(self.messages[1])
        to_str += self.bot()
        return to_str


class TwoSecMainHor(FancyBannerUni):
    def __init__(self, msg1='', msg2='', msg3='', width=0):
        super().__init__(msg1, msg2, msg3, width=width, mode='dbl')

    def __str__(self):
        to_str = '\n'
        to_str += self.top()
        to_str += self.blank()
        to_str += self.msg(self.messages[0])
        to_str += self.blank()
        to_str += self.line_two_part_top()
        to_str += self.msg_two_part()
        to_str += self.bot_two_part()

        return to_str


class TwoSecMega(FancyBannerUni):
    def __init__(self, msg1='', msg2='', width=0):
        super().__init__(msg1, msg2, width=width, mode='dbl')

    def __str__(self):
        to_str = '\n'
        to_str += self.top()
        to_str += self.blank()
        to_str += self.blank()
        to_str += self.msg(self.messages[0].upper())
        to_str += self.blank()
        to_str += self.blank()
        to_str += self.line_int()
        to_str += self.msg(self.messages[1])
        to_str += self.bot()
        return to_str


class ThreeSec(FancyBannerUni):
    def __init__(self, msg1='', msg2='', msg3='', width=0):
        super().__init__(msg1, msg2, msg3, width=width)

    def __str__(self):
        to_str = '\n'
        to_str += self.top()
        to_str += self.msg(self.messages[0].upper())

        to_str += self.line_int()
        to_str += self.msg(self.messages[1])

        to_str += self.line_int()
        to_str += self.msg(self.messages[2])
        to_str += self.bot()
        return to_str


class ThreeSecMain(FancyBannerUni):
    def __init__(self, msg1='', msg2='', msg3='', width=0):
        super().__init__(msg1, msg2, msg3, width=width, mode='dbl')

    def __str__(self):
        to_str = '\n'
        to_str += self.top()
        to_str += self.blank()
        to_str += self.msg(self.messages[0].upper())
        to_str += self.blank()
        to_str += self.line_int()
        to_str += self.msg(self.messages[1])
        to_str += self.line_int()
        to_str += self.msg(self.messages[2])
        to_str += self.bot()
        return to_str


class ThreeSecMega(FancyBannerUni):
    def __init__(self, msg1='', msg2='', msg3='', width=0):
        super().__init__(msg1, msg2, msg3, width=width, mode='dbl')

    def __str__(self):
        to_str = '\n'
        to_str += self.top()
        to_str += self.blank()
        to_str += self.blank()
        to_str += self.msg(self.messages[0].upper())
        to_str += self.blank()
        to_str += self.blank()
        to_str += self.line_int()
        to_str += self.blank()
        to_str += self.msg(self.messages[1])
        to_str += self.blank()
        to_str += self.line_int()
        to_str += self.msg(self.messages[2])
        to_str += self.bot()
        return to_str


class Ribbon(FancyBannerUni):
    def __init__(self, msg='', width=0):
        super().__init__(msg, width=width)

    def __str__(self):
        to_str = '\n'
        to_str += self.line(self.messages[0])

        return to_str


class SmallRibbon(FancyBannerUni):
    def __init__(self, msg='', width=0):
        super().__init__(msg, width=width)

    def __str__(self):
        self.innerSize = int(self.width / 3)
        to_str = '\n'
        to_str += '{msg:^{width}}'.format(msg=self.line(self.messages[0]), width=self.width)

        return to_str
