import sys
import math
import time
from collections import Counter
import jieba

def text_to_vector(text):
    # 中文分词
    words = jieba.lcut(text)
    word_counts = Counter(words)
    return word_counts


def calculate_cosine_similarity(vec1, vec2):
    # 计算余弦相似度
    common_words = set(vec1.keys()) & set(vec2.keys())
    dot_product = sum(vec1[word] * vec2[word] for word in common_words)
    norm1 = math.sqrt(sum(vec1[word] ** 2 for word in vec1))
    norm2 = math.sqrt(sum(vec2[word] ** 2 for word in vec2))
    similarity = dot_product / (norm1 * norm2) if (norm1 * norm2) != 0 else 0
    return similarity


def main():
    if len(sys.argv) != 4:
        print("Usage: python plagiarism_checker.py <original_file_path> <plagiarized_file_path> <output_file_path>")
        return
    start_time = time.time()
    original_file_path = sys.argv[1]
    plagiarized_file_path = sys.argv[2]
    output_file_path = sys.argv[3]

    # 读取文件中的原文和抄袭文本
    with open(original_file_path, 'r', encoding='utf-8') as original_file:
        original_text = original_file.read()

    with open(plagiarized_file_path, 'r', encoding='utf-8') as plagiarized_file:
        plagiarized_text = plagiarized_file.read()

    # 计算查重率
    # 将文本转换为词频向量
    original_vector = text_to_vector(original_text)
    plagiarized_vector = text_to_vector(plagiarized_text)

    # 计算余弦相似度
    similarity = calculate_cosine_similarity(original_vector, plagiarized_vector)

    # 输出查重率
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(f"重复率：{similarity * 100:.2f}%")

    end_time = time.time()
    run_time = end_time - start_time
    print(f"{similarity * 100:.2f}%")
    print(f"程序运行时间：{run_time:.5f} 秒")

if __name__ == "__main__":
    main()
