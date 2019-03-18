"""Nifty ext holding various tools for our printer."""


def _get_status(self):
    """Return status to object.

    :returns str: return string containing the gcode command.
    """
    return("M105")


def _set_status(self, s=1):
    """Set status on printer.

    :param s: (in seconds) frequency of status or 0 to disable defualts to 1.
    :return
    """
    gcode = "M105 s{s}"
    return(gcode.replace("{s}", s))


def _send_rgb(self, r=0, g=0, b=0, toggle='on'):
    """Send rgb values to printer.

    :param r: int representing red values 0-255.
    :param g: int representing blue values 0-255.
    :param b: int representing green values 0-255.
    :returns gcode: str value for the result gcode.
    """
    if r or g or b > 255:
        raise Exception

    gcode = """
        M150 R{r} U{g} B{b}
    """
    gcode = gcode.replace("{r}", r)
    gcode = gcode.replace("{g}", g)
    gcode = gcode.replace("{b}", b)
    if toggle == 'off':
        return("M150")
    return(gcode)
