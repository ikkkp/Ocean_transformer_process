# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Load model directly
'''
@File  :text-embedding-v2.py
@Author:Ezra Zephyr
@Date  :2023/11/2522:23
@Desc  :
'''
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import numpy as np

# Press the green button in the gutter to run the script.
# 文本相似度计算模型
if __name__ == '__main__':
    model = AutoModelForSequenceClassification.from_pretrained('vectara/hallucination_evaluation_model')
    tokenizer = AutoTokenizer.from_pretrained('vectara/hallucination_evaluation_model')

    pairs = [
        ["A man walks into a bar and buys a drink", "A bloke swigs alcohol at a pub"],
        ["A person on a horse jumps over a broken down airplane.", "A person is at a diner, ordering an omelette."],
        ["A person on a horse jumps over a broken down airplane.", "A person is outdoors, on a horse."],
        ["A boy is jumping on skateboard in the middle of a red bridge.",
         "The boy skates down the sidewalk on a blue bridge"],
        ["A man with blond-hair, and a brown shirt drinking out of a public water fountain.",
         "A blond drinking water in public."],
        ["A man with blond-hair, and a brown shirt drinking out of a public water fountain.",
         "A blond man wearing a brown shirt is reading a book."],
        ["Mark Wahlberg was a fan of Manny.", "Manny was a fan of Mark Wahlberg."],
    ]

    inputs = tokenizer.batch_encode_plus(pairs, return_tensors='pt', padding=True)

    model.eval()
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits.cpu().detach().numpy()
        # convert logits to probabilities
        scores = 1 / (1 + np.exp(-logits)).flatten()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
