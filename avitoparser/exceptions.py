#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Lonely_Dark---
# Python 3.10.5

class PageSourceNotConfigured(Exception):

    def __init__(self, message: str) -> None:
        """
        Thrown an error if page source don't transmitted
        :param message: message to know
        """
        self.message = message

    def __str__(self) -> str:
        return "Page source isn't configured. %s" % self.message
