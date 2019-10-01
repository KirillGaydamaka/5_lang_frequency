import argparse


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
    words_dict = {}
    for word in words_list:
        word = word.strip('",: .;?!*').lower()
        if word in words_dict.keys():
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1

    most_frequent_words_frequencies = \
        sorted(words_dict.items(), key=lambda x: x[1], reverse=True)[:10]
    most_frequent_words = list(map(lambda x: x[0],
                                   most_frequent_words_frequencies))
    return most_frequent_words


def main():
    try:
        filepath = create_parser().filepath
        text = load_data(filepath)
        print('Most frequent words:', get_most_frequent_words(text))
    except FileNotFoundError:
        exit('Файл не найден')


if __name__ == '__main__':
    main()
