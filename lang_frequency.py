import argparse
from collections import Counter


CONSTANT_WORDS_QUANTITY = 10


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
        [word.strip('",: .;?!*').lower() for word in words_list])
    most_frequent_words_count = \
        words_count.most_common(CONSTANT_WORDS_QUANTITY)
    return [word for word, count in most_frequent_words_count]


def main():
    try:
        filepath = create_parser().filepath
        text_from_file = load_data(filepath)
        most_frequent_words = get_most_frequent_words(text_from_file)
        print(CONSTANT_WORDS_QUANTITY,
              'most frequent words in the text from your file are:')
        for word in most_frequent_words:
            print(word)
    except FileNotFoundError:
        exit('Файл не найден')


if __name__ == '__main__':
    main()
