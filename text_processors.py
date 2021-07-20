import json
import random
import jieba
import pypinyin
import zhconv

from typing import Callable
from constants import SPECIAL_CHARACTERS, PINYIN_PROBABILITY, ZH_PROBABILITY


def replacement_processor(text: str, quest_func: Callable[[str], bool],
                          resource: str = 'resources/replacement.json') -> str:
    if quest_func('Would you like to apply replacements in {}?'.format(resource)):
        with open(resource, encoding='utf-8') as file:
            replacements = json.loads(file.read())
        ans = text
        for replacement in replacements:
            if quest_func('Would you like to replace all "{}" with "{}"?'.format(replacement[0], replacement[1])):
                ans = ans.replace(replacement[0], replacement[1])
        return ans
    else:
        return text


def special_char_processor(text: str, quest_func: Callable[[str], bool]) -> str:
    if quest_func('Would you like to insert special characters?'):
        seg_list = list(jieba.cut(text, cut_all=False))
        for i in range(0, len(seg_list)):
            chars = list(seg_list[i])
            s = ''
            for c in chars:
                s += c
                s += random.choice(SPECIAL_CHARACTERS)
            s = s[0:-1]
            seg_list[i] = s
        text = ''.join(seg_list)

    return text


def pinyin_processor(text: str, quest_func: Callable[[str], bool]) -> str:
    if quest_func('Would you like to convert to Pin Yin?'):
        ans = ''
        for c in text:
            if random.random() < PINYIN_PROBABILITY:
                piny = pypinyin.pinyin(c)[0][0]
                if c != piny:
                    piny = piny
                ans += piny
            else:
                ans += c
        return ans
    return text


def zh_processor(text: str, quest_func: Callable[[str], bool]) -> str:
    if quest_func('Would you like to convert to Traditional Chinese?'):
        ans = ''
        for c in text:
            if random.random() < ZH_PROBABILITY:
                ans += zhconv.convert(c, 'zh-tw')
            else:
                ans += c
        return ans
    return text
