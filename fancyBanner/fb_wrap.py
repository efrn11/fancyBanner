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
                'h': '─',
                'v': '│',
                'tl': '┌',
                'tr': '┐',
                'bl': '└',
                'br': '┘',
                'i': '┼',
                'li': '├',
                'ri': '┤',
                'ti': '┬',
                'bi': '┴'
            },
            'dbl': {
                'h': '═',
                'v': '║',
                'tl': '╔',
                'tr': '╗',
                'bl': '╚',
                'br': '╝',
                'i': '╬',
                'li': '╠',
                'ri': '╣',
                'ti': '╦',
                'bi': '╩'
            },
            'bold': {
                'h': '━',
                'v': '┃',
                'tl': '┏',
                'tr': '┓',
                'bl': '┗',
                'br': '┛',
                'i': '╋',
                'li': '┣',
                'ri': '┫',
                'ti': '┳',
                'bi': '┻'
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

    def msg_wrapper(self, func):
        def inner(msg):
            if len(msg) >= self.width:
                s = msg[::self.width - 5]
                for line in s:
                    print(func(line))
        return inner


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

    @msg_wrapper
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
