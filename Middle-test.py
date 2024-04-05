


def read_file(file_path):
    file_path="/ text.txt"
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def find_top_n_words(text, n=10):
    word_counts = {}
    words = text.lower().split()  # Розділити текст на слова за пробілами
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_word_counts[:n]


def write_to_file(word_counts, output_file):
    output_file="/ output.txt"
    with open(output_file, 'w', encoding='utf-8') as file:
        for word, count in word_counts:
            file.write(f"{word}-{count}\n")