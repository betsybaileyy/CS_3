
from redacted import Redact

def word_test(string):
    test_string = [ "I", "love", "dogs", "and", "fish" ]
    redacted_words = [ "love", "fish" ]
    assert redact(test_string, redacted_words) ==
