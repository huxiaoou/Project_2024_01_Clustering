def SetFontColor(c):
    def inner(s: str):
        return f"\033[{c}m{s}\033[0m"

    return inner


SFR = SetFontColor(c="0;31;40")  # Red
SFG = SetFontColor(c="0;32;40")  # Green
SFY = SetFontColor(c="0;33;40")  # Yellow
SFB = SetFontColor(c="0;34;40")  # Blue
SFM = SetFontColor(c="0;35;40")  # Magenta
SFC = SetFontColor(c="0;36;40")  # Cyan
SFW = SetFontColor(c="0;37;40")  # White


def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30, 38):
            s1 = ''
            for bg in range(40, 48):
                fmt = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (fmt, fmt)
            print(s1)
        print('\n')


if __name__ == "__main__":
    test_string = "hello, world"
    print(SFR(test_string))
    print(SFG(test_string))
    print(SFY(test_string))
    print(SFB(test_string))
    print(SFM(test_string))
    print(SFC(test_string))
    print(SFW(test_string))
    print_format_table()
