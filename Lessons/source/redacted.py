from set import Set

test_string = ["I", "love", "dogs", "and", "fish"]
redacted_words = ["love", "fish", "impala"]

def redact(string):
    redacted_set = Set(redacted_words)
    returned_words = []
    for word in test_string:
        if not redacted_set.contains(word):
            returned_words.append(word)
        return returned_words
    print(returned_words)

redact(test_string)
