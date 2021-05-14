import word_count


def test_tacocat():
    assert word_count.word_length("taco cat") == 2

def test_Sentence1():
    assert word_count.word_length("Hello my name is Jacob Redfern.") == 6

def test_Sentence2():
    assert word_count.word_length("This is an in class activity.") == 6