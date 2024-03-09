from sample import native


def ts_factor(word, idx, is_lowercase):
    if (len(word) > 1) & (word[idx - 1] in ['ц', 'Ц']):
        return ''
    else:
        return 'ts' if is_lowercase else 'Ts'


def convert_loanworld(loanword: str):
    t = []
    for idx, ch in enumerate(loanword):
        t.append(_convert(ch, loanword, idx))
    return "".join(t)


def _convert(char, word, idx):
    match char:
        case 'щ':
            return 'şç'
        case 'в':
            return 'v'
        case 'г':
            return 'g'
        case 'к':
            return 'k'
        case 'ц':
            return ts_factor(word, idx, True)
        case 'я':
            return 'ya'
        case 'ю':
            return 'yu'
        case 'е':
            # todo fix me
            return 'е'
        case 'ё':
            return 'yo'
        case 'ь':
            return '’'
        case 'ъ':
            return '’'
        case 'у':
            return 'u'
        case 'ы':
            # todo fix me sometimes can be 'yı'
            return 'ı'

        case 'Щ':
            return 'Şç'
        case 'В':
            return 'V'
        case 'Г':
            return 'G'
        case 'К':
            return 'K'
        case 'Ц':
            return ts_factor(word, idx, False)
        case 'Я':
            return 'Ya'
        case 'Ю':
            return 'Yu'
        case 'Е':
            # todo fix me
            return 'E'
        case 'Ё':
            return 'Yo'
        case 'У':
            return 'U'
        case 'Ы':
            # todo fix me sometimes can be 'yı'
            return 'I'

        case _:
            return native.convert_common(char)
