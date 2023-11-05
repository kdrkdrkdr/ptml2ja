# -*- coding: utf-8 -*-
from ....hangulize import *
from ....g2pk3.english import convert_eng

class English(Language):
    """For transcribing English."""

    __iso639__ = {1: 'en', 2: 'eng', 3: 'eng'}
    __tmp__ = '.;,'

    notation = Notation([

    ])

    def normalize(self, string):
        return normalize_roman(convert_eng(string))

__lang__ = English