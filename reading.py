"""Estimate how long a piece of text takes to read."""

import math

WORDS_PER_MINUTE = 200


def reading_time(word_count: int) -> int:
    """Return the whole minutes needed to read word_count words, never less than 1."""
    if word_count < 0:
        raise ValueError("word_count can't be negative")
    return max(1, math.ceil(word_count / WORDS_PER_MINUTE))
