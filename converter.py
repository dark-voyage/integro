import json
import fasttext
import re
import os
import util
from util.convert_helpers import (TRANSLATOR, STOP_SYMBOLS, VOWELS, 
                                  change_e, change_ts)

util.main()
os.chdir("/Users/a.orzikulov/Desktop/GitHub/Integro")
file_path = "output-28-7-2021.json"
with open(file_path, "r", encoding="UTF-8") as file:
    data = json.load(file)

LANGUAGE_MODEL_PATH = '/Users/asrorbek/GitHub/integro_old/lid.176.bin'
model = fasttext.load_model(LANGUAGE_MODEL_PATH)

russian_texts = []
uzbek_texts = []
for posts in data.values():
    for post_text in posts.values():
        if post_text != "None" and post_text != "":
            post_text = re.sub(r"[ (]?[Hh]ttps?[:%].+/s?", "", post_text)
            post_text = re.sub(r"\s", " ", post_text)
            prediction, score = model.predict(post_text)
            if prediction[0] == "__label__ru" and score[0] >= 0.8:
                russian_texts.append(post_text)
            else:
                uzbek_texts.append(post_text)

print(len(uzbek_texts))
print(len(russian_texts))

with open("uzbek_texts.txt", "w", encoding="UTF-8") as file:
    for text in uzbek_texts:
        file.writelines(text + "\n")

with open("russian_texts.txt", "w", encoding="UTF-8") as file:
    for text in russian_texts:
        file.writelines(text + "\n")

with open("links.txt", "w", encoding="UTF-8") as file:
    for key in data:
        file.writelines(key + "\n")


text = "Тўхтанг! Бир нарсани унутманг: Ўзбекистонда муаммо йўқ!  Ана ўша суҳбатдан сўнг Ўзбекистондаги партиялар ҳақида маълум тасаввур шаклланиб қолган менда. Бу тасаввурим кейинчалик кўплаб гувоҳликлар асосида мустаҳкамланди.  Дўстим Рафаэль Сатторов Hook Report нашри учун бир мақола тайёрлапти. Менинг тасаввурим ва, фикримча, кўпчилик ўзбекистонликларнинг партиялар ҳақидаги тасаввурлари акс этган яхши мақола бўпти. Яхши муаллифнинг иши ўзи шу: ҳаётда кўриб турган нарсаларимизни чиройли қилиб тасвирлаб бериш, токи ўқувчи “ие, ҳақиқатан шундай!” деб юборсин. Яхши муаллиф доим ҳам янги билим бермайди, балки ўқувчидаги билимларни тасдиқлаб, мустаҳкамлаб беради.  Хуллас, мақоланинг қисқача мазмунини келтираман.  Партиялар бутун дунёда фуқароларни маълум ғоялар атрофида бирлаштириш, сўнг бу ғояларни сиёсий майдонга"
text = re.sub(r"\s", " ", text)

fixed_message = ""
for idx, character in enumerate(text):
    if character == "Е" or character == "е":
        fixed_message += change_e(
            idx, text, TRANSLATOR, STOP_SYMBOLS, VOWELS)
    elif character == "Ц" or character == "ц":
        fixed_message += change_ts(
            idx, text, TRANSLATOR, STOP_SYMBOLS, VOWELS)
    elif character in TRANSLATOR:
        fixed_message += TRANSLATOR[character]
    else:
        fixed_message += character

fixed_message
