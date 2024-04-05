import re
import pytest


def read_file(file_path):
    """Reads content from a text file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def find_top_n_words(text, n=10):
    """Finds the top N most common words in the text."""
    word_counts = {}
    words = re.findall(r'\b\w+\b', text.lower())
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_word_counts[:n]


def write_to_file(word_counts, output_file):
    """Writes word counts to a file."""
    with open(output_file, 'w', encoding='utf-8') as file:
        for word, count in word_counts:
            file.write(f"{word}-{count}\n")


@pytest.fixture
def sample_text_file(tmp_path):
    """Creates a sample text file with content."""
    file_content = "Hello world! How are you?How are your friends?How is your dog?"
    file_path = tmp_path / "sample.txt"
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(file_content)
    return file_path


@pytest.mark.parametrize("input_text, expected_output", [
    ("Hello world! How are you?How are your friends?How is your dog?",
     [('how', 3), ('are', 2), ('your', 2), ('hello', 1), ('world', 1), ('you', 1), ('friends', 1), ('is', 1), ('dog', 1)]),
])
def test_find_top_n_words(input_text, expected_output):
    top_words = find_top_n_words(input_text, n=9)
    assert top_words == expected_output

def test_read_file(sample_text_file):
    content = read_file(sample_text_file)
    assert content == "Hello world! How are you?How are your friends?How is your dog?"

def test_write_to_file(tmp_path):
    """Tests the write_to_file function."""
    word_counts = [('word1', 5), ('word2', 3), ('word3', 2), ('word4', 1)]
    output_file = tmp_path / "output.txt"
    write_to_file(word_counts, output_file)
    with open(output_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    assert lines == ["word1-5\n", "word2-3\n", "word3-2\n", "word4-1\n"]

if __name__ == "__main__":
    pytest.main([__file__])