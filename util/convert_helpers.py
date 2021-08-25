import re

TRANSLATOR = {
    u'А': 'A',
    u'Б': 'B',
    u'Д': 'D',
    u'Э': 'E',
    u'Ф': 'F',
    u'Г': 'G',
    u'Ҳ': 'H',
    u'И': 'I',
    u'Ж': 'J',
    u'К': 'K',
    u'Қ': 'Q',
    u'Л': 'L',
    u'М': 'M',
    u'Н': 'N',
    u'О': 'O',
    u'П': 'P',
    u'Р': 'R',
    u'С': 'S',
    u'Т': 'T',
    u'У': 'U',
    u'В': 'V',
    u'Х': 'X',
    u'Й': 'Y',
    u'З': 'Z',
    u'Ъ': "'",
    u'Ь': "",

    u'а': 'a',
    u'б': 'b',
    u'д': 'd',
    u'э': 'e',
    u'ф': 'f',
    u'г': 'g',
    u'ҳ': 'h',
    u'и': 'i',
    u'ж': 'j',
    u'к': 'k',
    u'қ': 'q',
    u'л': 'l',
    u'м': 'm',
    u'н': 'n',
    u'о': 'o',
    u'п': 'p',
    u'р': 'r',
    u'с': 's',
    u'т': 't',
    u'у': 'u',
    u'в': 'v',
    u'х': 'x',
    u'й': 'y',
    u'з': 'z',
    u'ъ': "'",
    u'ь': "",
    u'«': '"',
    u'»': '"',
    u'„': '"',
    u'“': '"',
    u'—': '-',
    u'’': "'",
    u' ': ' ',

    # special cases
    u"Ғ": u"G`",
    u"Ў": u"O`",
    u"Ш": u"Sh",
    u"Ч": u"Ch",
    u"Ё": u"Yo",
    u"Ю": u"Yu",
    u"Я": u"Ya", ########
    u"Ц": ["S", "Ts"],
    u"Е": ["Ye", "E"],

    u"ғ": u"g`",
    u"ў": u"o`",
    u"ш": u"sh",
    u"ч": u"ch",
    u"ё": u"yo",
    u"ю": u"yu",
    u"я": u"ya",  ########
    u"ц": ["s", "ts"],
    u"е": ["ye", "e"],

    # Emojis
    u"😀": u":kulayotgan_chehra:",
    u"😁": u":tirjayib_qarayotgan_chehra:",
    u"😂": u":ko`z_yoshi_bilan_kulayotgan_chehra:",
    u"🤣": u":buralib_kulayotgan_chehra:",
    u"😃": u":katta_ko`zlar_bilan_kulayotgan_chehra:",
    u"😄": u":yumuq_ko`z_bilan_kulayotgan_chehra:",
    u"😅": u":biroz_hijolat_chehra:",
    u"😆": u":qattiq_kulayotgan_chehra:",
    u"😉": u":ko`z_qisayotgan_chehra:",
    u"😊": u":jilmaygan_chehra:",
    u"😋": u":ovqatdan_mazza_qilayotgan_chehra:",
    u"😎": u":ko`zoynaklari_bilan_kulayotgan_chehra:",
    u"😍": u":sevgi_ko`zlari_bilan_qarayotgan_chehra:",
    u"😘": u":o`payotgan_chehra:",
    u"🥰": u":sevilayotgan_chehra:",
    u"😗": u":o`payotgan_chehra:",
    u"😙": u":yumuq_ko`zlar_bilan_o`payotgan chehra:",
    u"🥲": u":ko`z_yoshli_chehra:",
    u"😚": u":yumuq_ko`zlar_bilan_o`payotgan_chehra:",
    u"☺️": u":xushchaqchaq_chehra:",
    u"🙂": u":sal_kulayotgan_chehra:",
    u"🤗": u":quchoqlayotgan_chehra:",
    u"🤩": u":yulduzlik_kasalligi:",
    u"🤔": u":o`ylayotgan_chehra:",
    u"🤨": u":shubhalanayotgan_chehra:",
    u"😐": u":oddiy_chehra:",
    u"😑": u":hissiyotsiz_chehra:",
    u"😶": u":og`izsiz_chehra:",
    u"🙄": u":ensasi_qotayotgan_chehra:",
    u"😏": u":kuchli_ensasi_qotayotgan_chehra:",
    u"😣": u":xafa_chehra:",
    u"😥": u":biroz_xafa_chehra:",
    u"😮": u":hayratlangan_chehra:",
    u"🤐": u":og`zi_yopiq_chehra:",
    u"😯": u":sukunatga_tushgan_chehra:",
    u"😪": u":uyqusirayotgan_chehra:",
    u"😫": u":charchagan_chehra:",
    u"🥱": u":esnayotgan_chehra:",
    u"😴": u":uxlayotgan_chehra:",
    u"😌": u":ishongan_chehra:",
    u"😛": u":tilini_ko`rsatayotgan_chehra:",
    u"😜": u":ko`zini_qisib_turgan_chehra:",
    u"😝": u":tilini_ko`rsatayotgan_chehra:",
    u"🤤": u":och_qolgan_chehra:",
    u"😒": u":ensasi_qotgan_chehra:",
    u"😓": u":yerga_qarayotgan_chehra:",
    u"😔": u":xafa_chehra:",
    u"😕": u":ikkilanayotgan_chehra:",
    u"🙃": u":teskari_chehra:",
    u"🤑": u":pul_istagidagi_chehra:",
    u"😲": u":hayratlanayotgan_chehra:",
    u"☹️": u":xafa_chehra"
}

STOP_SYMBOLS = {";", "?", "!", ".", ",", " "}
VOWELS = {"а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е",
          "Ё", "А", "Е", "И", "О", "У", "Ы", "Э", "Ю", "Я"}

REPLACEMENTS = {r"[ (]?[Hh]ttps?[:%]\S+\s?": "",
                r"\n": " ",
                u"\U0001f1fa\U0001f1ff": "",
                r"@\S+\s?": "",
                r"#\S+\s?": "", 
                u"\u2757": "",
                u"\u200b": "",
                u"Actual News\U0001f1fa\U0001f1ff": "", # uz flag
                u"Актуальные новости Узбекистана🇺🇿🇺🇿🇺🇿": "",
                r"[Сс]ентябр": "sentabr",
                r"[Оо]ктябр": "oktabr"}


def change_e(index, text, translator, stop_symbols, vowels):
    """
    Change Cyrillic `e` to Latin `e` or `ye`.
    """
    if index == 0:
        previous_char = "None"
    else:
        previous_char = text[index-1]

    if previous_char == "None" or previous_char in stop_symbols:
        return translator[text[index]][0]
    elif previous_char in vowels:
        return translator[text[index]][0]
    else:
        return translator[text[index]][1]


def change_ts(index, text, translator, stop_symbols, vowels):
    """
    Change Cyrillic `ц` to Latin `s` or `ts`.
    """
    if index == 0:
        previous_char = "None"
    else:
        previous_char = text[index-1]

    if previous_char == "None" or previous_char in stop_symbols:
        return translator[text[index]][0]
    elif previous_char in vowels:
        if index == len(text) - 1:
            return translator[text[index]][0]
        elif text[index+1] in stop_symbols:
            return translator[text[index]][0]
        else:
            return translator[text[index]][1]
    else:
        return translator[text[index]][0]


def multiple_replace(pairs, string):
    def replace(m):
        return next(
            replacement
            for (pattern, replacement), group in zip(pairs.items(), m.groups())
            if group is not None
        )
    patterns = '|'.join("({})".format(pattern) for pattern in pairs)
    return re.sub(patterns, replace, string)
