import pytest
from lib.text import normalize, tokenize, count_freq, top_n


# normalize
def test_normalize_basic():
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир"


def test_normalize_empty():
    assert normalize("") == ""


def test_normalize_no_casefold():
    assert normalize("ПрИвЕт", casefold=False) == "ПрИвЕт"


def test_normalize_no_yo2e():
    assert normalize("Ёлка ёж", yo2e=False) == "ёлка ёж"


def test_normalize_multiple_spaces_and_tabs():
    text = "  hello\t\tworld\n\n"
    assert normalize(text) == "hello world"


# tokenize
def test_tokenize_basic():
    assert tokenize("hello world") == ["hello", "world"]


def test_tokenize_hyphenated():
    assert tokenize("text-with-hyphen") == ["text-with-hyphen"]


def test_tokenize_unicode():
    assert tokenize("привет-мир") == ["привет-мир"]


def test_tokenize_numbers_and_words():
    assert tokenize("win10 ubuntu20") == ["win10", "ubuntu20"]


def test_tokenize_apostrophe_split():
    assert tokenize("don't can't i'm") == ["don", "t", "can", "t", "i", "m"]


def test_tokenize_empty():
    assert tokenize("") == []


# count_freq
def test_count_freq_basic():
    tokens = ["a", "b", "a"]
    assert count_freq(tokens) == {"a": 2, "b": 1}


def test_count_freq_case_sensitive():
    tokens = ["a", "A", "a"]
    assert count_freq(tokens) == {"a": 2, "A": 1}


def test_count_freq_empty():
    assert count_freq([]) == {}


def test_count_freq_large_input():
    tokens = ["x"] * 1000
    assert count_freq(tokens) == {"x": 1000}


# top_n
def test_top_n_basic():
    freq = {"a": 3, "b": 2, "c": 1}
    assert top_n(freq, 2) == [("a", 3), ("b", 2)]


def test_top_n_tie_breaker():
    freq = {"bbb": 2, "aaa": 2, "ccc": 1}
    # при равной частоте сортировка по алфавиту
    assert top_n(freq, 3) == [("aaa", 2), ("bbb", 2), ("ccc", 1)]


def test_top_n_more_than_available():
    freq = {"x": 10}
    assert top_n(freq, 5) == [("x", 10)]


def test_top_n_empty_dict():
    assert top_n({}, 3) == []
