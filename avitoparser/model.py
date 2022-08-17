#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Lonely_Dark---
# Python 3.10.5

from dataclasses import dataclass


@dataclass(frozen=True)
class Advert:
    """
    Dataclass for Advertisements
    """
    title: str
    description: str
    price: str
