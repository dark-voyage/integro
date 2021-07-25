from transliterate import translit, get_available_language_codes
from transliterate.base import TranslitLanguagePack, registry
from transliterate.discover import autodiscover


class UzbekCyrillicTranslit(TranslitLanguagePack):
    language_code = "uz"
    language_name = "Uzbek"
    mapping = (
        u"АБДЭФГҲИЖКҚЛМНОПРСТУВХЙЗЪабдэфгҳижкқлмнопрстувхйзъ«»„“—‘’ ",
        u"ABDEFGHIJKQLMNOPRSTUVXYZ'abdefghijkqlmnoprstuvxyz'\"\"\"\"-'' ",
    )
    pre_processor_mapping = {
        # Uppercase characters
        u"Ғ": u"G`",
        u"Ў": u"O`",
        u"Ш": u"Sh",
        u"Ч": u"Ch",
        u"Ё": u"Yo",
        u"Ю": u"Yu",
        u"Я": u"Ya",
        u"Ц": u"Ts",
        u"Е": u"Ye",
        # Lowercase characters
        u"ғ": u"g`",
        u"ў": u"o`",
        u"ш": u"sh",
        u"ч": u"ch",
        u"ё": u"yo",
        u"ю": u"yu",
        u"я": u"ya",
        u"ц": u"ts",
        u"е": u"ye",
        # Emojis
        u"😀": u":kulayotgan chehra:",
        u"😁": u":tirjayib qarayotgan chehra:",
        u"😂": u":kulgu ko`z yoshi bilan kulayotgan chehra:",
        u"🤣": u":buralib ko`z yosh bilan kulayotgan chehra:",
        u"😃": u":katta ko`zlar bilan kulayotgan chehra:",
        u"😄": u":yumuq ko`z bilan kulayotgan chehra:",
        u"😅": u":ter bilan kulayotgan chehra:",
        u"😆": u":g`ilaylanib kulayotgan chehra:",
        u"😉": u":ko`z qisayotgan chehra:",
        u"😊": u":qizargan yuz bilan kulayotgan chehra:",
        u"😋": u":ovqatdan mazza qilayotgan chehra:",
        u"😎": u":quyosh ko`zoynaklari bilan kulayotgan chehra:",
        u"😍": u":sevgi ko`zlari bilan qarayotgan chehra:",
        u"😘": u":sevgi ila o`payotgan chehra:",
        u"🥰": u":sevilayotgan chehra:",
        u"😗": u":o`payotgan chehra:",
        u"😙": u":yumuq ko`zlar bilan o`payotgan chehra:",
        u"🥲": u":ko`z yoshlar bilan kulayotgan chehra:",
        u"😚": u":yumuq ko`zlar bilan o`payotgan chehra:",
        u"☺️": u":xushchaqchaq chehra:",
        u"🙂": u":sal kulayotgan chehra:",
        u"🤗": u":quchoqlayotgan chehra:",
        u"🤩": u":yulduz kasalligi:",
        u"🤔": u":o`ylayotgan chehra:",
        u"🤨": u":shubhalanayotgan chehra:",
        u"😐": u":oddiy chehra:",
        u"😑": u":xissiyotsiz chehra:",
        u"😶": u":og`izsiz chehra:",
        u"🙄": u":ensasi qotayotgan chehra:",
        u"😏": u":ayyorona tirjayotgan chehra:",
        u"😣": u":istamayotgan chehra:",
        u"😥": u":ishonch bilan qarayotgan xafa chehra:",
        u"😮": u":og`zi ochiq chehra:",
        u"🤐": u":og`zi yopiq chehra:",
        u"😯": u":sukunatga tushgan chehra:",
        u"😪": u":uyqusirayotgan chehra:",
        u"😫": u":charchagan chehra:",
        u"🥱": u":ensirayotgan chehra:",
        u"😴": u":uxlayotgan chehra:",
        u"😌": u":ishongan chehra:",
        u"😛": u":tilini ko`rsatayotgan chehra:",
        u"😜": u":ko`zini qisib tilini ko`rsatayotgan chehra:",
        u"😝": u":ko`zlarini qisib tilini ko`rsatayotgan chehra:",
        u"🤤": u":so`lagi tomayotgan chehra:",
        u"😒": u":kulmayotgan chehra:",
        u"😓": u":yerga teri bilan qarayotgan chehra:",
        u"😔": u":o`ylanib qogan chehra:",
        u"😕": u":ikkilanayotgan chehra:",
        u"🙃": u":teskari chehra:",
        u"🤑": u":pul istagidagi chehra:",
        u"😲": u":xayratlanayotgan chehra:",
        u"☹️": u"::"
    }


def init():
    autodiscover()
    registry.register(UzbekCyrillicTranslit)


