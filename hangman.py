#!/usr/bin/env python3
import time
import curses
import random

def read_drawing(filename):
    drawing = []
    with open(filename) as f:
        for line in f:
            line = line.rstrip('\n')
            drawing.append(line)
    return drawing

def draw_title(scr, drawing):
    scr.attron(curses.color_pair(1))
    scr.attron(curses.A_BOLD)
    start_row = 1
    start_col = 37
    idx = 0
    for item in drawing:
        scr.addstr(start_row + idx, start_col, item)
        idx = idx + 1

def draw_echafaud(scr, drawing):
    scr.attron(curses.color_pair(2))
    scr.attron(curses.A_BOLD)
    start_row = 1
    start_col = 1
    idx = 0
    for item in drawing:
        scr.addstr(start_row + idx, start_col, item)
        idx = idx + 1

def draw_screen(scr):
    title = read_drawing('res/title.txt')
    echafaud1 = read_drawing('res/echafaud1.txt')
    echafaud2 = read_drawing('res/echafaud2.txt')
    echafaud3 = read_drawing('res/echafaud3.txt')
    echafaud4 = read_drawing('res/echafaud4.txt')
    echafaud5 = read_drawing('res/echafaud5.txt')
    echafaud6 = read_drawing('res/echafaud6.txt')
    echafaud7 = read_drawing('res/echafaud7.txt')
    echafaud8 = read_drawing('res/echafaud8.txt')
    echafaud9 = read_drawing('res/echafaud9.txt')
    echafaud10 = read_drawing('res/echafaud10.txt')
    echafauds = [echafaud1, echafaud2, echafaud3, echafaud4, echafaud5, echafaud6, echafaud7, echafaud8, echafaud9, echafaud10]
    message = read_drawing('res/message.txt')
    n = 0
    key = 0
    scr.clear()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    draw_title(scr,title)
    options = ["Endgame", "Marvel", "Iron Man", "Harry Potter", "Gryffindor"]
    w = random.choice(options)
    word =[]
    guess = []
    errors = []
    word_work(w, word, guess)
    while '-' in guess:
        key = scr.getch()
        letter = chr(key)
        if letter == '1':
            exit()
        res = letter_work(word, guess, errors, letter)
        draw_echafaud(scr, echafauds[len(errors)])
        draw_guess(scr, guess)
        draw_errors(scr, errors)
        draw_status_bar(scr)
        scr.refresh()
    draw_message(scr, message)
    scr.refresh()
    time.sleep(2)




def word_work(str, word, guess):
    for item in str:
        item = item.upper()
        word.append(item)
        if item.isalpha() != True :
            guess.append(item)
        else:
            guess.append('-')

def letter_work(word, guess, errors, new_letter):
    result = 'Wrong!'
    new_letter = new_letter.upper()
    if new_letter.isalpha() != True:
        result = 'Not a letter...'
    else:
        if new_letter in errors:
                result = 'Already wrong.'
        elif new_letter in guess:
                result = 'Already right!'
        else:
            for i in range(len(word)):
                if new_letter == word[i]:
                    guess[i] = new_letter
                    result = 'Right!'
            if result == 'Wrong!':
                errors.append(new_letter)
    return result
        #if new_letter
def draw_guess(scr, drawing):
    scr.attron(curses.color_pair(2))
    scr.attron(curses.A_BOLD)
    start_row = 17
    start_col = 47
    idx = 0
    scr.addstr(start_row, start_col - 6, 'Word:')
    for item in drawing:
        scr.addstr(start_row, start_col + idx, item)
        idx = idx + 2

def draw_errors(scr, drawing):
    scr.attron(curses.color_pair(1))
    scr.attron(curses.A_BOLD)
    start_row = 20
    start_col = 49
    idx = 0
    scr.addstr(start_row, start_col - 8, 'Errors:')
    for item in drawing:
        scr.addstr(start_row, start_col + idx, item)
        idx = idx + 2

def draw_message(scr, drawing):
    scr.attron(curses.color_pair(2))
    scr.attron(curses.A_BOLD)
    start_row = 22
    start_col = 47
    idx = 0
    for item in drawing:
        scr.addstr(start_row + idx, start_col, item)
        idx = idx + 1

def draw_status_bar(scr):
    scr.attron(curses.color_pair(1))
    scr.attron(curses.A_BOLD)
    status = "Press 1 to Exit"
    height, width = scr.getmaxyx()
    scr.addstr (height -1, (width//2)-(len(status)//2), status)

def main():
    curses.wrapper(draw_screen)

if __name__ == "__main__":
    main()
