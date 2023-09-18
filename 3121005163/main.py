import sys
import math
from collections import Counter
import jieba
import time
import string


def text_to_vector(text):
    """
    中文分词
    """
    # 去除标点符号和空格
    exclude = set(string.punctuation + ' ' + '。，“”‘’！？【】、')
    words = [word for word in jieba.cut(text) if word not in exclude]
    word_counts = Counter(words)
    return word_counts


def read_text_file(file_path):
    """
    读取文本文件并返回文件内容。
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            return text
    except FileNotFoundError:
        print(f"文件未找到，请检查文件路径")
        return None
    except Exception as e:
        print(f"打开文件时发生错误: {e}")
        return None


def calculate_cosine_similarity(vec1, vec2):
    """
    计算余弦相似度
    """
    # 相同的词语
    common_words = set(vec1.keys()) & set(vec2.keys())
    # 计算点积
    dot_product = sum(vec1[word] * vec2[word] for word in common_words)
    # 计算2-范数
    norm1 = math.sqrt(sum(vec1[word] ** 2 for word in vec1))
    norm2 = math.sqrt(sum(vec2[word] ** 2 for word in vec2))
    # 计算查重率
    similarity = dot_product / (norm1 * norm2) if (norm1 * norm2) != 0 else 0
    print(similarity)
    return similarity


def main():
    if len(sys.argv) != 4:
        print("正确用法应该为: python main.py <原文文件路径> <抄袭版论文的文件路径> <答案文件路径>")
        return

    original_file_path = sys.argv[1]
    plagiarized_file_path = sys.argv[2]
    output_file_path = sys.argv[3]

    # 读取文件中的原文和抄袭文本
    original_text = read_text_file(original_file_path)
    plagiarized_text = read_text_file(plagiarized_file_path)
    if original_text is None or plagiarized_text is None:
        return

    # 计算查重率
    # 将文本转换为词频向量
    original_vector = text_to_vector(original_text)
    plagiarized_vector = text_to_vector(plagiarized_text)

    # 计算余弦相似度
    similarity = calculate_cosine_similarity(original_vector, plagiarized_vector)

    # 输出查重率
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(f"重复率：{similarity * 100:.2f}%")

    print(f"重复率:{similarity * 100:.2f}%")


if __name__ == "__main__":
    main()


