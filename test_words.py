import hangman
import pytest

def test_word_work1():
    str = 'redivider'
    word = []
    guess = []
    hangman.word_work(str,word,guess)
    assert word == ['R','E','D','I','V','I','D','E','R']
    assert guess == ['-','-','-','-','-','-','-','-','-']

def test_word_work2():
    str = 'Sam Hawkens'
    word = []
    guess = []
    hangman.word_work(str,word,guess)
    assert word == ['S','A','M',' ','H','A','W','K','E','N','S']
    assert guess == ['-','-','-',' ','-','-','-','-','-','-','-']

def test_word_work3():
    str = 'Avengers: Endgame'
    word = []
    guess = []
    hangman.word_work(str,word,guess)
    assert word == ['A','V','E','N','G','E','R','S',':',' ','E','N','D','G','A','M','E']
    assert guess == ['-','-','-','-','-','-','-','-',':',' ','-','-','-','-','-','-','-']

def test_letter_work1():
    word = ['R','E','D','I','V','I','D','E','R']
    guess = ['-','-','-','-','-','-','-','-','-']
    errors = []
    new_letter = 'r'
    result = hangman.letter_work(word,guess,errors,new_letter)
    assert result == 'Right!'
    assert word == ['R','E','D','I','V','I','D','E','R']
    assert guess == ['R','-','-','-','-','-','-','-','R']
    assert errors == []

def test_letter_work2():
    word = ['R','E','D','I','V','I','D','E','R']
    guess = ['-','-','-','-','-','-','-','-','-']
    errors = []
    new_letter = 'x'
    result = hangman.letter_work(word,guess,errors,new_letter)
    assert result == 'Wrong!'
    assert word == ['R','E','D','I','V','I','D','E','R']
    assert guess == ['-','-','-','-','-','-','-','-','-']
    assert errors == ['X']

def test_letter_work3():
    word = ['R','E','D','I','V','I','D','E','R']
    guess = ['-','-','-','-','-','-','-','-','-']
    errors = []
    new_letter = ';'
    result = hangman.letter_work(word,guess,errors,new_letter)
    assert result == 'Not a letter...'
    assert word == ['R','E','D','I','V','I','D','E','R']
    assert guess == ['-','-','-','-','-','-','-','-','-']
    assert errors == []

def test_letter_work4():
    word = ['R','E','D','I','V','I','D','E','R']
    guess = ['R','-','-','-','-','-','-','-','R']
    errors = ['']
    new_letter = 'r'
    result = hangman.letter_work(word,guess,errors,new_letter)
    assert result == 'Already right!'
    assert word == ['R','E','D','I','V','I','D','E','R']
    assert guess == ['R','-','-','-','-','-','-','-','R']
    assert errors == ['']

def test_letter_work5():
    word = ['R','E','D','I','V','I','D','E','R']
    guess = ['-','-','-','-','-','-','-','-','-']
    errors = ['X']
    new_letter = 'x'
    result = hangman.letter_work(word,guess,errors,new_letter)
    assert result == 'Already wrong.'
    assert word == ['R','E','D','I','V','I','D','E','R']
    assert guess == ['-','-','-','-','-','-','-','-','-']
    assert errors == ['X']
