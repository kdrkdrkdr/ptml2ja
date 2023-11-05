# -*- coding: utf-8 -*-
from ....hangulize import *
from ....ko2kana.korean import join_jamos, split_syllables

_repl1 = {
    # 'kh': 'ㅋ',
    'ng': 'ㅇ',
    'gh': 'ㄱ',
    'b': 'ㅂ',
    'c': 'ㅉ',
    'd': 'ㄷ',
    'f': 'ㅍ',
    'g': 'ㄱ',
    'h': 'ㅎ',
    'j': 'ㅈ',
    'k': 'ㄲ',
    'l': 'ㄹ',
    'm': 'ㅁ',
    'n': 'ㄴ',
    'p': 'ㅃ',
    'q': 'ㅋ',
    'r': 'ㄹ',
    's': 'ㅅ',
    't': 'ㅌ',
    'v': 'ㅂ',
    'x': 'ㅅ',
    'z': 'ㅈ',
    'ya': 'ㅑ',
    'yi': 'ㅣ',
    'yu': 'ㅠ',
    'ye': 'ㅖ',
    'yo': 'ㅛ',
    'a': 'ㅏ',
    'e': 'ㅔ',
    'i': 'ㅣ',
    'o': 'ㅗ',
    'u': 'ㅜ',
}

_repl2 = {
    # ㅑㅣㅠㅖㅛㅏㅔㅣㅗㅜ
    'ㅃ': 'ㅂ',
    'ㅉ': 'ㅈ',
    'ㅑ': '야',
    'ㅣ': '이',
    'ㅠ': '유',
    'ㅖ': '예',
    'ㅛ': '요',
    'ㅏ': '아',
    'ㅔ': '에',
    'ㅗ': '오',
    'ㅜ': '우'
}



class Indonesian(Language):
    """For transcribing Indonesian."""

    __iso639__ = {1: 'id', 2: 'ind', 3: 'ind'}
    # __tmp__ = '.;,'

    notation = Notation([
        
    ])

    def normalize(self, string):
        string = str(normalize_roman(string)).replace('  ', ' ').strip()+' '
        for k, v in _repl1.items():
            string = string.replace(k, v)
        string = join_jamos(string)
        for k, v in _repl2.items():
            string = string.replace(k, v)
        string = join_jamos(split_syllables(string))
        return string


__lang__ = Indonesian