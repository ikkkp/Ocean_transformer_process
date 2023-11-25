import jieba

def split_article(article):
    # 使用结巴分词进行句子分割
    sentences = list(jieba.cut(article, cut_all=False))

    # 恢复分割后的句子
    sliced_article = []
    current_sentence = ""
    for word in sentences:
        current_sentence += word
        if word in ['。', '？', '！']:
            sliced_article.append(current_sentence)
            current_sentence = ""

    # 处理剩余的文本
    if current_sentence:
        sliced_article.append(current_sentence)

    return sliced_article

if __name__ == '__main__':
    # 你的长文章
    long_article = "A man walks into a bar and buys a drink bloke swigs alcohol at a pub A person is at a diner, ordering an omelette."
    # 进行句子分割
    sliced_article = split_article(long_article)

    # 输出切片后的句子
    for sentence in sliced_article:
        print(sentence, end='\n')
