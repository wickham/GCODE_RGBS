#!/usr/bin/env python -u
# encoding: utf-8
"""Nifty ext holding various tools for our printer."""

class printer():
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
        s = str(s)
        gcode = 'M105 s{s}'
        return(gcode.replace("{s}", s))


    def _send_rgb(self, rgb=[0,0,0], toggle='on'):
        """Send rgb values to printer.

        :param r: int representing red values 0-255.
        :param g: int representing blue values 0-255.
        :param b: int representing green values 0-255.
        :returns gcode: str value for the result gcode.
        """
        if toggle == 'off':
            return("M150")

        gcode = "M150 R{0} U{1} B{2}"
        for item in rgb:
            if item > 255:
                raise "Exception"

        gcode = gcode.format(rgb[0], rgb[1], rgb[2])

        return(gcode)
