"""Nifty ext holding various tools for our printer."""


def _get_status(self):
    """Return status to object

    :returns str: return string containing the gcode command.
    """
    return("M105")


def _set_status(self, s=1):
    """Set status on printer

    :param s: (in seconds) frequency of status or 0 to disable defualts to 1.
    """
    return(self.replace("M105 s{s}", s))
