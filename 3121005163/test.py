import unittest
from unittest.mock import mock_open, patch
from main import calculate_cosine_similarity, text_to_vector, read_text_file


class MyTestCase(unittest.TestCase):
    def test_open_failure(self):
        # 模拟一个文件路径
        file_path = 'some_file.txt'

        # 使用unittest.mock.patch模拟open函数，返回一个抛出异常的文件对象
        with patch('builtins.open', mock_open()) as mock_file:
            mock_file.side_effect = Exception("File open failed")

            # 尝试读取文件
            result = read_text_file(file_path)
            self.assertIsNone(result)  # 期望返回None

    def test_open_notfound(self):
        # 模拟一个文件路径
        file_path = 'some_file.txt'
        # 尝试读取文件
        result = read_text_file(file_path)
        self.assertIsNone(result)  # 期望返回None

    def test_cosine_similarity(self):
        # 构造测试数据
        vec1 = {'今天': 1, '的': 1, '天气': 1, '晴': 1, '啊': 1}
        vec2 = {'今天': 1, '的': 1, '天气': 1, '晴朗': 1, '啊': 1}
        similarity = calculate_cosine_similarity(vec1, vec2)
        self.assertAlmostEqual(similarity, 0.8, places=2)  # 期望余弦相似度为0.8

    def test_text_to_vector(self):
        text = "一位真正的作家永远只为内心写作，只有内心才会真实地告诉他，他的自私、他的高尚是多么突出。"
        expected_vector = {'的': 3, '他': 3,  '内心': 2, '一位': 1, '真正': 1, '作家': 1, '永远': 1, '只': 1, '为': 1, '写作': 1, '只有': 1, '才': 1,
                           '会': 1, '真实': 1, '地': 1, '告诉': 1,  '自私': 1, '高尚': 1, '是': 1, '多么': 1, '突出': 1}
        vector = text_to_vector(text)
        self.assertDictEqual(vector, expected_vector)  # 断言词频向量正确


if __name__ == '__main__':
    unittest.main()
