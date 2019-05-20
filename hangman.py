#!/usr/bin/env python3
import time #Imports time module
import curses #Imports curses module
import random #Imports random module

def read_drawing(filename): #Function for reading the drawing, gives it the filename parameter
    drawing = [] #Makes a new list called drawing
    with open(filename) as f: #Opens the file
        for line in f: #In every line
            line = line.rstrip('\n') #Strips the enters
            drawing.append(line) #Add the line to drawing
    return drawing #Returns the value of drawing

def draw_title(scr, drawing): #Function for drawing the title
    scr.attron(curses.color_pair(1)) #Uses the first color pair
    scr.attron(curses.A_BOLD) #Makes the text bold
    start_row = 1
    start_col = 37
    idx = 0
    for item in drawing:
        scr.addstr(start_row + idx, start_col, item)
        idx = idx + 1

def draw_echafaud(scr, drawing): #Function for drawing the different hangman stages
    scr.attron(curses.color_pair(2))
    scr.attron(curses.A_BOLD)
    start_row = 1
    start_col = 1
    idx = 0
    for item in drawing:
        scr.addstr(start_row + idx, start_col, item)
        idx = idx + 1

def draw_screen(scr):
    title = read_drawing('res/title.txt') #
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
    rules = read_drawing('res/rules')
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
    left = []
    draw_guess_left(scr, left, errors)
    word_work(w, word, guess)
    draw_guess(scr, guess)
    draw_errors(scr, errors)
    draw_status_bar(scr)
    draw_category(scr)
    while '-' in guess:
        draw_guess_left(scr, left, errors)
        key = scr.getch()
        letter = chr(key)
        if letter == '1':
            exit()
        if letter == '2':
            scr.clear()
            draw_rules(scr, rules)
            scr.refresh()
            time.sleep(2)
            scr.clear()
        if len(errors) == 9:
            scr.clear()
            draw_message(scr, message)
            scr.refresh()
            time.sleep(2)
            exit()
        res = letter_work(word, guess, errors, letter)
        draw_guess(scr, guess)
        draw_errors(scr, errors)
        draw_echafaud(scr, echafauds[len(errors)])
        draw_guess_left(scr, left, errors)
    scr.clear()
    draw_message(scr, message)
    scr.refresh()
    time.sleep(2)
    exit()
    scr.refresh()




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
    sub = scr.subwin(10,70, 10, 20)
    sub.box()
    sub.attron(curses.color_pair(2))
    sub.attron(curses.A_BOLD)
    start_row = 1
    start_col = 5
    idx = 0
    for item in drawing:
        sub.addstr(start_row + idx, start_col, item)
        idx = idx + 1

def draw_status_bar(scr):
    scr.attron(curses.color_pair(1))
    scr.attron(curses.A_BOLD)
    status = "Press 1 to Exit or 2 for Rules"
    height, width = scr.getmaxyx()
    scr.addstr (height -1, (width//2)-(len(status)//2), status)

def draw_category(scr):
    scr.attron(curses.color_pair(1))
    scr.attron(curses.A_BOLD)
    category = "Category: Movies"
    height, width = scr.getmaxyx()
    scr.addstr (height//3, (width//3)-(len(category)//2), category)

def draw_guess_left(scr, drawing, errors):
    scr.attron(curses.color_pair(1))
    scr.attron(curses.A_BOLD)
    left = "Guesses Left: " + str(10-len(errors))
    if len(errors)>= 1:
        left = left + ' '
    height, width = scr.getmaxyx()
    scr.addstr (height//3, (width-16), left)

def draw_rules(scr, drawing):
    sub = scr.subwin(10,70, 10, 20)
    sub.box()
    sub.attron(curses.color_pair(2))
    sub.attron(curses.A_BOLD)
    start_row = 1
    start_col = 5
    idx = 0
    for item in drawing:
        sub.addstr(start_row + idx, start_col, item)
        idx = idx + 1

def main(): #Function for starting up the program
    curses.wrapper(draw_screen)

if __name__ == "__main__": #Starts the cycle
    main()
