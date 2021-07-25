from transliterate.base import TranslitLanguagePack, registry
from transliterate.discover import autodiscover


class UzbekCyrillicTranslit(TranslitLanguagePack):
    language_code = "uz"
    language_name = "Uzbek"
    mapping = (
        u"АБДЭФГҲИЖКҚЛМНОПРСТУВХЙЗЪабдэфгҳижкқлмнопрстувхйзъ«»„“—‘’ ",
        u"ABDEFGHIJKQLMNOPRSTUVXYZ'abdefghijkqlmnoprstuvxyz'\"\"\"\"-'' ",
    )
    pre_processor_mapping = {
        # Uppercase characters
        u"Ғ": u"G'",
        u"Ў": u"O'",
        u"Ш": u"Sh",
        u"Ч": u"Ch",
        u"Ё": u"Yo",
        u"Ю": u"Yu",
        u"Я": u"Ya",
        u"Ц": u"S",
        u"Е": u"E",
        # Lowercase characters
        u"ғ": u"g'",
        u"ў": u"o'",
        u"ш": u"sh",
        u"ч": u"ch",
        u"ё": u"yo",
        u"ю": u"yu",
        u"я": u"ya",
        u"ц": u"s",
        u"е": u"e",
        # Emojis
        u"😀": u":kulayotgan_chehra:",
        u"😁": u":tirjayib_qarayotgan_chehra:",
        u"😂": u":ko'z_yoshi_bilan_kulayotgan_chehra:",
        u"🤣": u":buralib_kulayotgan_chehra:",
        u"😃": u":katta_ko'zlar_bilan_kulayotgan_chehra:",
        u"😄": u":yumuq_ko'z_bilan_kulayotgan_chehra:",
        u"😅": u":biroz_hijolat_chehra:",
        u"😆": u":qattiq_kulayotgan_chehra:",
        u"😉": u":ko'z_qisayotgan_chehra:",
        u"😊": u":jilmaygan_chehra:",
        u"😋": u":ovqatdan_mazza_qilayotgan_chehra:",
        u"😎": u":ko'zoynaklari_bilan_kulayotgan_chehra:",
        u"😍": u":sevgi_ko'zlari_bilan_qarayotgan_chehra:",
        u"😘": u":o'payotgan_chehra:",
        u"🥰": u":sevilayotgan_chehra:",
        u"😗": u":o'payotgan_chehra:",
        u"😙": u":yumuq_ko`zlar_bilan o'payotgan chehra:",
        u"🥲": u":ko'z_yoshli_chehra:",
        u"😚": u":yumuq_ko'zlar_bilan_o'payotgan_chehra:",
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
