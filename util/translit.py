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
        u"Ғ": u"G`",
        u"Ў": u"O`",
        u"Ш": u"Sh",
        u"Ч": u"Ch",
        u"Ё": u"Yo",
        u"Ю": u"Yu",
        u"Я": u"Ya",
        u"Ц": u"S",
        u"Е": u"E",

        # Lowercase characters
        u"ғ": u"g`",
        u"ў": u"o`",
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


def init():
    autodiscover()
    registry.register(UzbekCyrillicTranslit)
