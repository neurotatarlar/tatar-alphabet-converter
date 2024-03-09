from sample.loanword import convert_loanworld
from sample.native import convert_native

# todo check exception 'ädäbiyat'
# todo arabic loanwords uses xamza
# todo check how to translate 'ЦК'
# todo consider all upper case ПИTsА
# todo check `e` is vowel
# todo г, к cannot be formalized, need to go to the deeper level
# todo check words stating with 'дж'
# todo check common and native intersections
# todo describe translation rules for `г` and `к`


# Simple metrics to calculate how many times we can determine origins by rules
uncertainty_counter = 0
total_counter = 0


def trivial_analysis(word: str):
    """
    This method does simple analysis of the word to determine it origins. Sometimes we can determine origins by some
    patterns in chars
    :param word: word to analysis
    :return: translated word if analysis was successful or None if not
    """
    # if word starts with letter 'ы' this is a tatar word
    if word[0] in ['ы', 'Ы']:
        return convert_native(word)

    return None


def ask_model(word: str):
    """
    Ask trained model for help
    :param word: word to translate
    :return: best try to translate the word
    """
    return '<<X>>'


def word_wrap_up(word, contains_native_chars, contains_foreign_chars):
    global total_counter
    total_counter += 1
    word = "".join(word)
    if contains_foreign_chars and not contains_native_chars:
        # the word is a loanword
        translation = convert_loanworld(word)
    elif contains_native_chars and not contains_foreign_chars:
        # the word is a native word
        translation = convert_native(word)
    else:
        # we do not have enough info about the word's origins
        # go for a deeper level
        global uncertainty_counter
        uncertainty_counter += 1
        translation = trivial_analysis(word)

    return translation if translation else ask_model(word)


def translate_cy_la(text):
    accumulated_result = []
    word = []
    contains_native_chars = False
    contains_foreign_chars = False
    for ch in text:
        match ch:
            case 'ә' | 'Ә' | 'ү' | 'Ү' | 'ө' | 'Ө' | 'җ' | 'Җ' | 'ң' | 'Ң' | 'һ' | 'Һ':
                contains_native_chars = True
                word.append(ch)
            case 'ц' | 'Ц' | 'щ' | 'Щ' | 'ё' | 'Ё':
                contains_foreign_chars = True
                word.append(ch)
            case '-' | '—':
                # çaq-çaq
                word.append(ch)
            case 'а' | 'А' | 'б' | 'Б' | 'в' | 'В' | 'г' | 'Г' | 'д' | 'Д' | 'е' | 'Е' | 'ж' | 'Ж' | 'з' | 'З' \
                 | 'и' | 'И' | 'й' | 'Й' | 'к' | 'К' | 'л' | 'Л' | 'м' | 'М' | 'н' | 'Н' | 'о' | 'О' | 'п' | 'П' \
                 | 'р' | 'Р' | 'с' | 'С' | 'т' | 'Т' | 'у' | 'У' | 'ф' | 'Ф' | 'х' | 'Х' | 'ч' | 'Ч' | 'ш' | 'Ш' \
                 | 'ъ' | 'Ъ' | 'ы' | 'Ы' | 'ь' | 'Ь' | 'э' | 'Э' | 'ю' | 'Ю' | 'я' | 'Я':
                word.append(ch)
            case _:
                # anything but tatar cyrillic alphabet's character left
                # wrap up the word
                if word:
                    accumulated_result.append(
                        word_wrap_up(word, contains_native_chars, contains_foreign_chars)
                    )

                # just return non-cyrillic char as is
                accumulated_result.append(ch)

                # reset for the next word
                contains_native_chars = False
                contains_foreign_chars = False
                word = []

    # finalize
    if word:
        accumulated_result.append(word_wrap_up(word, contains_native_chars, contains_foreign_chars))
    print(uncertainty_counter, total_counter, (uncertainty_counter / total_counter * 100))
    return "".join(accumulated_result)


if __name__ == "__main__":
    print(translate_cy_la("су анасы"))
