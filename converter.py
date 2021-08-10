import json
import fasttext
import re
from transliterate import translit

file_path = "/Users/asrorbek/Desktop/Scraping/Database/output-28-7-2021.json"
with open(file_path, "r", encoding="UTF-8") as file:
    data = json.load(file)

texts = []
for posts in data.values():
    for post_text in posts.values():
        if post_text != "None" and post_text != "":
            post_text += "\n"
            post_text = re.sub(r"[ (]?(H|h)ttps?(:|%).+/s?", "", post_text)
            texts.append(post_text)

print(len(texts))

LANGUAGE_MODEL_PATH = '/Users/asrorbek/GitHub/integro_old/lid.176.bin'
model = fasttext.load_model(LANGUAGE_MODEL_PATH)

with open("text_responses.txt", "w", encoding="UTF-8") as file:
    for text in texts:
        file.writelines(text)

predictions = model.predict(texts[0].split("\n")[0])
print(predictions)

text = texts[12000] # 15000
text
text = text.split("\n")[2]
text
text = translit(u"" + text, "uz")
text
predictions = model.predict(text)
print(predictions)

import util
util.main()