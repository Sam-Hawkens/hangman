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
    start_row = 1 #Starts the text in the first row
    start_col = 37 #Starts the text in the 37th column
    idx = 0 #Variable idx equals to 0
    for item in drawing: #For each character in the drawing
        scr.addstr(start_row + idx, start_col, item) #Add to the screen each character, row by row
        idx = idx + 1 #idx gets bigger by 1

def draw_echafaud(scr, drawing): #Function for drawing the different hangman stages
    scr.attron(curses.color_pair(2)) #Uses the second color pair
    scr.attron(curses.A_BOLD) #Makes the text bold
    start_row = 1 #Starts the text in the first row
    start_col = 1 #Starts the text in the first column
    idx = 0 #Variable idx equals to 0
    for item in drawing:
        scr.addstr(start_row + idx, start_col, item)
        idx = idx + 1 #idx gets bigger by 1

def draw_screen(scr): #Function for drawing the screen
    title = read_drawing('res/title.txt') #Gives the directory for title.txt and reads it
    echafaud1 = read_drawing('res/echafaud1.txt') #Gives the directory for echafaud1.txt and reads it
    echafaud2 = read_drawing('res/echafaud2.txt') #Gives the directory for echafaud2.txt and reads it
    echafaud3 = read_drawing('res/echafaud3.txt') #Gives the directory for echafaud3.txt and reads it
    echafaud4 = read_drawing('res/echafaud4.txt') #Gives the directory for echafaud4.txt and reads it
    echafaud5 = read_drawing('res/echafaud5.txt') #Gives the directory for echafaud5.txt and reads it
    echafaud6 = read_drawing('res/echafaud6.txt') #Gives the directory for echafaud6.txt and reads it
    echafaud7 = read_drawing('res/echafaud7.txt') #Gives the directory for echafaud7.txt and reads it
    echafaud8 = read_drawing('res/echafaud8.txt') #Gives the directory for echafaud8.txt and reads it
    echafaud9 = read_drawing('res/echafaud9.txt') #Gives the directory for echafaud9.txt and reads it
    echafaud10 = read_drawing('res/echafaud10.txt') #Gives the directory for echafaud10.txt and reads it
    echafauds = [echafaud1, echafaud2, echafaud3, echafaud4, echafaud5, echafaud6, echafaud7, echafaud8, echafaud9, echafaud10]
    message = read_drawing('res/message.txt') #Gives the directory for message.txt and reads it
    rules = read_drawing('res/rules.txt') #Gives the directory for rules.txt and reads it
    n = 0 #Variable n equals to 0
    key = 0 #Variable key equals to 0
    scr.clear() #Wipes the screem
    curses.start_color()
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK) #Determines the first pair of colors
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK) #Determines the second pair of colors
    draw_title(scr,title)
    options = ["Endgame", "Marvel", "Iron Man", "Harry Potter", "Gryffindor"] #Defines the list options; these are all of the secret words
    w = random.choice(options) #Makes w a random word from options
    word =[] #Defines the list word as an empty list
    guess = [] #Defines the list guess as an empty list
    errors = [] #Defines the list errors as an empty list
    left = [] #Defines the list left as an empty list
    draw_guess_left(scr, left, errors) #Draws the amount of guesses left and uses the necessary parameters
    word_work(w, word, guess) #Draws the dashes and uses the necessary parameters
    draw_guess(scr, guess) #Draws the  text "Word:" and uses the necessary parameters
    draw_errors(scr, errors) #Draws the errors and uses the necessary parameters
    draw_status_bar(scr) #Draws the status bar and uses the necessary parameters
    draw_category(scr) #Draws the catergory and uses the necessary parameters
    while '-' in guess: #While there are hyphens in guess
        draw_guess_left(scr, left, errors)
        key = scr.getch() #Gets the key pressed
        letter = chr(key)
        if letter == '1': #If the letter equals to 1
            exit() #Exits the program
        if letter == '2': #If the letter equals to 2
            scr.clear() #Clears the screen
            draw_rules(scr, rules)
            scr.refresh() #Refreshes the screen
            time.sleep(2) #Waits for 2 seconds
            scr.clear() #Clears the screen
        if len(errors) == 9: #If the length of errors equals to 9; this may seem strange but this is how the program works
            scr.clear() #Clears the screen
            draw_message(scr, message) #Draws the message and uses the necessary parameters
            scr.refresh()
            time.sleep(2) #Waits for 2 seconds
            exit() #Exits the program
        res = letter_work(word, guess, errors, letter)
        draw_guess(scr, guess)
        draw_errors(scr, errors)
        draw_echafaud(scr, echafauds[len(errors)])
        draw_guess_left(scr, left, errors)
    scr.clear() #Clears the screen
    draw_message(scr, message) #Draws the message
    scr.refresh() #Refreshes the screen
    time.sleep(2) #Waits for 2 seconds
    exit() #Exits the program
    scr.refresh() #Refreshes the screen




def word_work(str, word, guess): #Function for drawing the dashes
    for item in str:
        item = item.upper()
        word.append(item)
        if item.isalpha() != True :
            guess.append(item)
        else:
            guess.append('-')

def letter_work(word, guess, errors, new_letter): #Function for determining what category a category falls under: Not a letter, Right, Wrong, Already Right, or Already Wrong
    result = 'Wrong!' #Result is "Wrong!""
    new_letter = new_letter.upper() #Makes the letter uppercase
    if new_letter.isalpha() != True: #If the character is not a letter
        result = 'Not a letter' #Result equals to Not a letter
    else: #If the character is a letter
        if new_letter in errors: #If the letter is already an error
                result = 'Already wrong.' #Result equals to Already Wrong
        elif new_letter in guess: #Or if the letter is already correct
                result = 'Already right!' #Result equals to already right
        else: #If the letter does not fall under those two categories
            for i in range(len(word)): #For every letter in the word
                if new_letter == word[i]: #If the letter equals to the letter
                    guess[i] = new_letter
                    result = 'Right!'
            if result == 'Wrong!':
                errors.append(new_letter)
    return result
        #if new_letter
def draw_guess(scr, drawing): #Function for drawing the text before the dashes
    scr.attron(curses.color_pair(2)) #Uses the second color pair
    scr.attron(curses.A_BOLD) #Makes the text bold
    start_row = 17 #Starts the text in the 17th row
    start_col = 47 #Starts the text in the 47th column
    idx = 0 #Variable idx equals to 0
    scr.addstr(start_row, start_col - 6, 'Word:')
    for item in drawing:
        scr.addstr(start_row, start_col + idx, item)
        idx = idx + 2 #idx gets bigger by 2

def draw_errors(scr, drawing): #Function for drawing the errors
    scr.attron(curses.color_pair(1)) #Uses the first color pair
    scr.attron(curses.A_BOLD) #Makes the text bold
    start_row = 20 #Starts the text in the 20th row
    start_col = 49 #Starts the text in the 49th column
    idx = 0 #Variable idx equals to 0
    scr.addstr(start_row, start_col - 8, 'Errors:') 
    for item in drawing:
        scr.addstr(start_row, start_col + idx, item)
        idx = idx + 2 #idx gets bigger by 2

def draw_message(scr, drawing): #Function for drawing the "Game Over!" message
    sub = scr.subwin(10,70, 10, 20)
    sub.box()
    sub.attron(curses.color_pair(2)) #Uses the second color pair
    sub.attron(curses.A_BOLD) #Makes the text bold
    start_row = 1 #Starts the text in the first row
    start_col = 5 #Starts the text in the 5th column
    idx = 0 #Variable idx equals to 0
    for item in drawing:
        sub.addstr(start_row + idx, start_col, item)
        idx = idx + 1 #idx gets bigger by 1

def draw_status_bar(scr): #Function for drawing the status bar (thing at the bottom of the screen)
    scr.attron(curses.color_pair(1)) #Uses the first color pair
    scr.attron(curses.A_BOLD)
    status = "Press 1 to Exit or 2 for Rules"
    height, width = scr.getmaxyx()
    scr.addstr (height -1, (width//2)-(len(status)//2), status)

def draw_category(scr): #Function for drawing the different hangman stages
    scr.attron(curses.color_pair(1)) #Uses the first color pair
    scr.attron(curses.A_BOLD) #Makes the text bold
    category = "Category: Movies"
    height, width = scr.getmaxyx()
    scr.addstr (height//3, (width//3)-(len(category)//2), category)

def draw_guess_left(scr, drawing, errors): #Function for drawing the amount of guesses left
    scr.attron(curses.color_pair(1)) #Uses the first color pair
    scr.attron(curses.A_BOLD) #Makes the text bold
    left = "Guesses Left: " + str(10-len(errors))
    if len(errors)>= 1:
        left = left + ' '
    height, width = scr.getmaxyx()
    scr.addstr (height//3, (width//2), left)

def draw_rules(scr, drawing): #Function for drawing rules
    sub = scr.subwin(10,70, 10, 20)
    sub.box()
    sub.attron(curses.color_pair(2)) #Uses the second color pair
    sub.attron(curses.A_BOLD) #Makes the text bold
    start_row = 1 #Starts the text in the first row
    start_col = 5 #Starts the text in the fifth column
    idx = 0 #Variable idx equals to 0
    for item in drawing: #For each character in rules
        sub.addstr(start_row + idx, start_col, item) #Draw each letter, column by column
        idx = idx + 1 #idx gets bigger by 1

def main(): #Function for starting up the program
    curses.wrapper(draw_screen)

if __name__ == "__main__": #Starts the cycle
    main()
