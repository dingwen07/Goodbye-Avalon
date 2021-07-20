from typing import Callable, List
from text_processors import *
from constants import *


def goodbye_avalon(text: str, quest_func: Callable[[str], bool]) -> List[str]:
    text = replacement_processor(text, quest_func)
    # text = special_char_processor(text, quest_func)
    text = pinyin_processor(text, quest_func)
    text = zh_processor(text, quest_func)

    return [text[i: i + LENGTH_LIMIT] for i in range(0, len(text), LENGTH_LIMIT)]


def always_true(s: str) -> bool:
    return True


def always_false(s: str) -> bool:
    return False


if __name__ == '__main__':
    while True:
        text = input('> ')
        if text.lower() == 'exit':
            break
        ans = goodbye_avalon(text, always_true)
        for s in ans:
            print(s)
            print()
