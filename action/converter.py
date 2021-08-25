import json
import fasttext
# import os
import pandas as pd
# import numpy as np

# os.chdir("/Users/a.orzikulov/Desktop/GitHub/Integro")  ################

import util   ################


# util.main()  ################
# file_path = .handler  ################


def main(file_path):
    with open(file_path, "r", encoding="UTF-8") as file:   ################
        data = json.load(file)
    
    LANGUAGE_MODEL_PATH = '../lid.176.bin'
    model = fasttext.load_model(LANGUAGE_MODEL_PATH)
    russian_texts = []
    uzbek_texts = []
    for channel, posts in data.items():
        for post_id, (date, views, post_text) in posts.items():     ##  data["https://t.me/Buka_tumani"].values()
            if not any([post_text == "None", post_text == "", post_text is None]):
                post_text = util.multiple_replace(util.REPLACEMENTS, post_text)
                prediction, score = model.predict(post_text)
                if prediction[0] == "__label__ru" and score[0] >= 0.8:
                    russian_texts.append([channel, post_id, date, views, post_text])
                else:
                    fixed_message = ""
                    for idx, character in enumerate(post_text):
                        if character == "Е" or character == "е":
                            fixed_message += util.change_e(
                                idx, post_text, util.TRANSLATOR, util.STOP_SYMBOLS, util.VOWELS)
                        elif character == "Ц" or character == "ц":
                            fixed_message += util.change_ts(
                                idx, post_text, util.TRANSLATOR, util.STOP_SYMBOLS, util.VOWELS)
                        elif character in util.TRANSLATOR:
                            fixed_message += util.TRANSLATOR[character]
                        else:
                            fixed_message += character
    
                    uzbek_texts.append([channel, post_id, date, views, fixed_message])

    util.log('info', f"The number of Uzbek posts is {len(uzbek_texts)}")
    util.log('info', f"The number of Russian posts is {len(russian_texts)}")
    header = ["channel", "post_id", "date", "views", "post"] # "label"
    if uzbek_texts:
        data_frame = pd.DataFrame(uzbek_texts)
        data_frame.to_excel('uzbek.xlsx', header=header, index=False)
    if russian_texts:
        data_frame = pd.DataFrame(russian_texts)
        data_frame.to_excel('russian.xlsx', header=header, index=False)

    util.log('success', "Two Excel files have been created.")

# with open("../uzbek_texts.txt", "w", encoding="UTF-8") as file:
#     for text in uzbek_texts:
#         file.writelines(text + "\n")

# with open("../russian_texts.txt", "w", encoding="UTF-8") as file:
#     for text in russian_texts:
#         file.writelines(text + "\n")

# russian_texts = []
# uzbek_texts = []
# for posts in data.values():
#     for post_text in posts.values():     ##  data["https://t.me/Buka_tumani"].values()
#         if not any([post_text == "None", post_text == "", post_text is None]):
#             if np.random.random() <= 0.03693444136657433:
#                 post_text = util.multiple_replace(REPLACEMENTS, post_text)
#                 prediction, score = model.predict(post_text)
#                 if prediction[0] == "__label__ru" and score[0] >= 0.8:
#                     russian_texts.append(post_text)
#                 else:
#                     uzbek_texts.append(post_text)

# print(len(uzbek_texts))
# print(len(russian_texts))
