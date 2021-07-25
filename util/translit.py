from transliterate import translit, get_available_language_codes
from transliterate.base import TranslitLanguagePack, registry
from transliterate.discover import autodiscover


class UzbekCyrillicTranslit(TranslitLanguagePack):
    language_code = "uz"
    language_name = "Uzbek"
    mapping = (
        u"АБДЭФГҲИЖКҚЛМНОПРСТУВХЙЗЪабдэфгҳижкқлмнопрстувхйзъ«»„“—",
        u"ABDEFGHIJKQLMNOPRSTUVXYZ'abdefghijkqlmnoprstuvxyz'\"\"\"\"-",
    )
    pre_processor_mapping = {
        # ҒЎШЁЮЯЦЧЕ
        u"Ғ": u"G`",
        u"Ў": u"O`",
        u"Ш": u"Sh",
        u"Ч": u"Ch",
        u"Ё": u"Yo",
        u"Ю": u"Yu",
        u"Я": u"Ya",
        u"Ц": u"Ts",
        u"Е": u"Ye",
        # ғўшёюяцче
        u"ғ": u"g`",
        u"ў": u"o`",
        u"ш": u"sh",
        u"ч": u"ch",
        u"ё": u"yo",
        u"ю": u"yu",
        u"я": u"ya",
        u"ц": u"ts",
        u"е": u"ye",
    }


def init():
    autodiscover()
    registry.register(UzbekCyrillicTranslit)


