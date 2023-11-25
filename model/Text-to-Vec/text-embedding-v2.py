'''
@File  :text-embedding-v2.py
@Author:Ezra Zephyr
@Date  :2023/11/2522:23
@Desc  :阿里云通用文本向量，通义实验室基于LLM底座的多语言文本统一向量模型，将文本数据快速转换为高质量的向量数据。
        https://help.aliyun.com/zh/dashscope/developer-reference/text-embedding-quick-start?disableWebsiteRedirect=true
'''
import dashscope
from http import HTTPStatus


def embed_with_str(dashscope_api_key, input_str):
    resp = dashscope.TextEmbedding.call(
        model=dashscope.TextEmbedding.Models.text_embedding_v1,
        input=input_str,
        api_key=dashscope_api_key)
    if resp.status_code == HTTPStatus.OK:
        print(resp)
    else:
        print(resp)
