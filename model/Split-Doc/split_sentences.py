import re


def split_sentences(text):
    # 使用正则表达式切分中英文文本
    pattern = re.compile(r'[。？！；;.]\s*')
    sentences = pattern.split(text)

    # 去除空字符串
    sentences = [s.strip() for s in sentences if s.strip()]

    return sentences


