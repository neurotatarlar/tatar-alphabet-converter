def u_factor(word, idx, normal, special):
    l = len(word)
    if l > 1 & (idx == l - 1) & (word[idx - 1] in ['а', 'ә', 'А', 'Ә']):
        return special
    else:
        return normal


def ya_factor(word, idx, is_lowercase):
    l = len(word)
    if l > 1 & (word[idx - 1] in ['и', 'И']):
        return 'ä' if is_lowercase else 'Ä'

    return None


def g_factor(word, idx, is_lowercase):
    if idx != (len(word) - 1):
        next_char = word[idx + 1]
        if next_char in ['а', 'А' 'о', 'О', 'ы', 'Ы', 'у', 'У', 'ъ', 'Ъ']:
            return 'ğ' if is_lowercase else 'Ğ'
        elif next_char in ['ә', 'Ә' 'ө', 'Ө', 'е', 'Е', 'ү', 'Ү', 'и', 'И', 'ь', 'Ь']:
            return 'g' if is_lowercase else 'G'
    return None


def k_factor(word, idx, is_lowercase):
    if idx != (len(word) - 1):
        next_char = word[idx + 1]
        if next_char in ['а', 'А' 'о', 'О', 'ы', 'Ы', 'у', 'У', 'ъ', 'Ъ']:
            return 'q' if is_lowercase else 'Q'
        elif next_char in ['ә', 'Ә' 'ө', 'Ө', 'е', 'Е', 'ү', 'Ү', 'и', 'И', 'ь', 'Ь']:
            return 'k' if is_lowercase else 'K'

    # signal up there is uncertainty and we need to look up in the model
    return None


def convert_native(word: str):
    t = []
    for idx, ch in enumerate(word):
        converted = _convert(ch, word, idx)
        if converted:
            t.append(converted)
        else:
            return None
    return "".join(t)


def _convert(char, word, idx):
    match char:
        case '-' | '—':
            return char
        case 'а':
            return 'a'
        case 'А':
            return 'A'
        case 'о':
            return 'o'
        case 'О':
            return 'O'
        case 'э':
            return 'e'
        case 'Э':
            return 'E'
        case 'и':
            return 'i'
        case 'И':
            return 'İ'

        case 'б':
            return 'b'
        case 'Б':
            return 'B'
        case 'ч':
            return 'ç'
        case 'Ч':
            return 'ç'
        case 'д':
            return 'd'
        case 'Д':
            return 'D'
        case 'ф':
            return 'f'
        case 'Ф':
            return 'F'
        case 'ж':
            return 'j'
        case 'Ж':
            return 'J'
        case 'л':
            return 'l'
        case 'Л':
            return 'L'
        case 'м':
            return 'm'
        case 'М':
            return 'M'
        case 'н':
            return 'n'
        case 'Н':
            return 'N'
        case 'п':
            return 'p'
        case 'П':
            return 'P'
        case 'р':
            return 'r'
        case 'Р':
            return 'R'
        case 'с':
            return 's'
        case 'С':
            return 'S'
        case 'ш':
            return 'ş'
        case 'Ш':
            return 'Ş'
        case 'т':
            return 't'
        case 'Т':
            return 'T'
        case 'х':
            return 'x'
        case 'Х':
            return 'X'
        case 'й':
            return 'y'
        case 'Й':
            return 'Y'
        case 'з':
            return 'z'
        case 'З':
            return 'Z'

        case 'ә':
            return 'ä'
        case 'ө':
            return 'ö'
        case 'ү':
            return u_factor(word, idx, 'ü', 'w')
        case 'у':
            return u_factor(word, idx, 'u', 'w')
        case 'җ':
            return 'c'
        case 'ң':
            return 'ñ'
        case 'һ':
            return 'һ'
        case 'ы':
            return 'ı'
        case 'в':
            return 'w'
        case 'г':
            return g_factor(word, idx, True)
        case 'к':
            return k_factor(word, idx, True)
        case 'ю':
            return None
        case 'я':
            return ya_factor(word, idx, True)
        case 'е':
            return None

        case 'Ә':
            return 'Ä'
        case 'Ө':
            return 'Ö'
        case 'Ү':
            return u_factor(word, idx, 'Ü', 'W')
        case 'У':
            return u_factor(word, idx, 'U', 'W')
        case 'Җ':
            return 'C'
        case 'Ң':
            return 'Ñ'
        case 'Һ':
            return 'Һ'
        case 'Ы':
            return 'I'
        case 'В':
            return 'W'
        case 'Г':
            return g_factor(word, idx, False)
        case 'К':
            return k_factor(word, idx, False)
        case 'Ю':
            return None
        case 'Я':
            return ya_factor(word, idx, True)
        case 'Е':
            return None
        case _:
            return convert_common(char)


def convert_common(char):
    match char:
        case '-' | '—':
            return char
        case 'а':
            return 'a'
        case 'А':
            return 'A'
        case 'о':
            return 'o'
        case 'О':
            return 'O'
        case 'э':
            return 'e'
        case 'Э':
            return 'E'
        case 'и':
            return 'i'
        case 'И':
            return 'İ'

        case 'б':
            return 'b'
        case 'Б':
            return 'B'
        case 'ч':
            return 'ç'
        case 'Ч':
            return 'ç'
        case 'д':
            return 'd'
        case 'Д':
            return 'D'
        case 'ф':
            return 'f'
        case 'Ф':
            return 'F'
        case 'ж':
            return 'j'
        case 'Ж':
            return 'J'
        case 'л':
            return 'l'
        case 'Л':
            return 'L'
        case 'м':
            return 'm'
        case 'М':
            return 'M'
        case 'н':
            return 'n'
        case 'Н':
            return 'N'
        case 'п':
            return 'p'
        case 'П':
            return 'P'
        case 'р':
            return 'r'
        case 'Р':
            return 'R'
        case 'с':
            return 's'
        case 'С':
            return 'S'
        case 'ш':
            return 'ş'
        case 'Ш':
            return 'Ş'
        case 'т':
            return 't'
        case 'Т':
            return 'T'
        case 'х':
            return 'x'
        case 'Х':
            return 'X'
        case 'й':
            return 'y'
        case 'Й':
            return 'Y'
        case 'з':
            return 'z'
        case 'З':
            return 'Z'
        case 'ь' | 'Ь' | 'ъ' | 'Ъ':
            return ''
        case _:
            raise IOError(f"Unexpected char `{char}`")
