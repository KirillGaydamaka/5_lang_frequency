import argparse
from collections import Counter


def load_data(filepath):
    with open(filepath, 'r', encoding='utf8') as file:
        return file.read()


def create_parser():
    parser = argparse.ArgumentParser(description='Parameters')
    parser.add_argument('filepath', nargs='?', default='my.txt',
                        help='An optional filepath')
    args = parser.parse_args()
    return args


def get_most_frequent_words(text):
    words_list = text.split()
    words_count = Counter(
        map(lambda w: w.strip('",: .;?!*').lower(), words_list))
    most_frequent_words_count = words_count.most_common(10)
    return list(map(lambda x: x[0], most_frequent_words_count))


def main():
    try:
        filepath = create_parser().filepath
        text = load_data(filepath)
        print('Most frequent words:', get_most_frequent_words(text))
    except FileNotFoundError:
        exit('Файл не найден')


if __name__ == '__main__':
    main()
