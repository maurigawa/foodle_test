import pytest

from sentences import sentence_word_count

def test_sentence_word_count():
    input = "baz bar foo foo zblah zblah zblah baz toto bar"
    expected = [
        ("zblah", 3),
        ("bar", 2),
        ("baz", 2),
    ]

    assert sentence_word_count(input, 3) == expected

def test_sentence_word_count_empty():
    input = ""
    expected = [
    ]

    assert sentence_word_count(input, 3) == expected

def test_sentence_word_count_zero_count():
    input = "a super test"
    expected = [
    ]

    assert sentence_word_count(input, 0) == expected

def test_sentence_word_count_big_count():
    input = "baz bar foo foo zblah zblah zblah baz toto bar"
    expected = [
        ("zblah", 3),
        ("bar", 2),
        ("baz", 2),
        ("foo", 2),
        ("toto", 1)
    ]

    assert sentence_word_count(input, 15000) == expected

@pytest.mark.parametrize(
    "input, count, expected",
    [
        ("test\tseparators test", 2, [("test", 2), ("separators", 1)]),
        ("test separators\ntest", 2, [("test", 2), ("separators", 1)]),
        ("test             separators test", 2, [("test", 2), ("separators", 1)]),
        ("test \t  separators \t\ntest", 2, [("test", 2), ("separators", 1)]),
    ]
)
def test_sentence_word_count_separators(input, count, expected):
    assert sentence_word_count(input, 3) == expected