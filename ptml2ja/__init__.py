
from .ko2kana import korean2katakana
from .hangulize import hangulize, langs
import re
from .cleaners import japanese_cleaners, _cleaner_cleans


lang_code_lst = {
    'KO', # 한국어
    'JA', # 일본어
    'EN', # 영어
    'ID', # 인도네시아어
    'VI', # 베트남어
    'RU', # 러시아어
    'TR', # 터키어
    'ES', # 스페인어
    'PT', # 포르투갈어
    'IT', # 이탈리아어
    'PO', # 폴란드어
    'DE', # 독일어
    'NL', # 네덜란드어
    'UK', # 우크라이나어
    'SV', # 스웨덴어
    'CS', # 체코어
    'FI', # 핀란드어
    'LA', # 라틴어
    'HU', # 헝가리어
}



def to_korean(text:str, lang_code:str):
    lang_code = lang_code.upper()
    text = text+' '
    if lang_code in ('KO', 'JA'):
        return text
    return hangulize(text, lang_code)



def to_japanese(text, lang_code):
    lang_code = lang_code.upper()
    if lang_code == 'JA':
        return text
    if lang_code != 'KO':
        text = to_korean(text, lang_code)
    return korean2katakana(text)



def ml2ja_ipa(text):
    for lc in lang_code_lst:
        lc = lc.upper()
        if lc != 'JA':
            text = re.sub(
                rf'\[{lc}\](.*?)\[{lc}\]', 
                lambda x: japanese_cleaners(to_japanese(x.group(1), lc)).replace(' ', '')+' ', 
                text
            ).replace('↓', '').replace('↑', '').replace('QQ', 'Q')

        else:
            text = re.sub(
                r'\[JA\](.*?)\[JA\]', 
                lambda x: japanese_cleaners(x.group(1))+' ', 
                text
            )
            
    text = ''.join(_cleaner_cleans.findall(text))
    return text