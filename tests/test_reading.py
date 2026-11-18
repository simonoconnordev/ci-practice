import pytest

from reading import reading_time


def test_a_few_words_take_one_minute():
    assert reading_time(5) == 1


def test_exactly_one_minute_of_words():
    assert reading_time(250) == 1


def test_partial_minutes_round_up():
    assert reading_time(251) == 2


def test_empty_text_still_shows_one_minute():
    assert reading_time(0) == 1


def test_negative_word_count_is_rejected():
    with pytest.raises(ValueError):
        reading_time(-1)
