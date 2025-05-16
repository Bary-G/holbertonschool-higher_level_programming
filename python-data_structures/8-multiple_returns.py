#!/usr/bin/python3
def multiple_returns(sentence):
    """Return the length of a string and its first character"""
    if not sentence:
        return None
    sentence_len = len(sentence)
    first_char = sentence[0]
    return sentence_len, first_char
