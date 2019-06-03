#!/usr/bin/env python3
import time #Imports time module
import curses #Imports curses module
import random #Imports random module

def read_drawing(filename): #Reads the drawing, function is given the filename parameter
    drawing = [] #Makes a new list called drawing
    with open(filename) as f: #Opens the file using provided file name
        for line in f: #In every line
            line = line.rstrip('\n') #Strips the trailing end of line
            drawing.append(line) #Adds the line to end of the drawing list
    return drawing #Returns the list containing all drawing lines

def draw_title(scr, drawing): #Draws the title, function is given the screen object and drawing list as parameters
    scr.attron(curses.color_pair(1)) #Uses the first color pair
    scr.attron(curses.A_BOLD) #Makes the text bold
    start_row = 1 #Starts the text in the first row
    start_col = 37 #Starts the text in the 37th column
    idx = 0 #Variable idx equals to 0
    for item in drawing: #For each line in the drawing list
        scr.addstr(start_row + idx, start_col, item) #Draws the line in the current row
        idx = idx + 1 #Increases the distance from start_row by 1

def draw_echafaud(scr, drawing): #Draws the different hangman stages. function is given the screen object and drawing list as parameters
    scr.attron(curses.color_pair(2)) #Uses the second color pair
    scr.attron(curses.A_BOLD) #Makes the text bold
    start_row = 1 #Starts the text in the first row
    start_col = 1 #Starts the text in the first column
    idx = 0 #Variable idx equals to 0
    for item in drawing: #For each line in the file
        scr.addstr(start_row + idx, start_col, item) #Prints each line in the desired location
        idx = idx + 1 #Increases the distance from start_row by 1

def draw_screen(scr): #Draws the screen, function is given the screen object as a parameter
    title = read_drawing('res/title.txt') #Reads title.txt using the given path
    echafaud1 = read_drawing('res/echafaud1.txt') #Reads echaufaud1.txt using the given path
    echafaud2 = read_drawing('res/echafaud2.txt') #Reads echaufaud2.txt using the given path
    echafaud3 = read_drawing('res/echafaud3.txt') #Reads echaufaud3.txt using the given path
    echafaud4 = read_drawing('res/echafaud4.txt') #Reads echaufaud4.txt using the given path
    echafaud5 = read_drawing('res/echafaud5.txt') #Reads echaufaud5.txt using the given path
    echafaud6 = read_drawing('res/echafaud6.txt') #Reads echaufaud6.txt using the given path
    echafaud7 = read_drawing('res/echafaud7.txt') #Reads echaufaud7.txt using the given path
    echafaud8 = read_drawing('res/echafaud8.txt') #Reads echaufaud8.txt using the given path
    echafaud9 = read_drawing('res/echafaud9.txt') #Reads echaufaud9.txt using the given path
    echafaud10 = read_drawing('res/echafaud10.txt') #Reads echaufaud10.txt using the given path
    echafauds = [echafaud1, echafaud2, echafaud3, echafaud4, echafaud5, echafaud6, echafaud7, echafaud8, echafaud9, echafaud10] #Puts all of hangman stage variables into one list
    game_over = read_drawing('res/game_over.txt') #Reads game_over.txt using the given path
    rules = read_drawing('res/rules.txt') #Reads rules.txt using the given path
    key = 0 #Variable key equals to 0, it will contain the ASCII number of the letter pressed
    scr.clear() #Wipes the screen
    curses.start_color() #Initializes the curses library
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK) #Determines the first pair of colors
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK) #Determines the second pair of colors
    draw_title(scr,title) #Draws the title
    options = ["Spider-Man", "Catch Me If You Can", "Status Update", "Back To The Future"] #Defines the list of secret words
    w = random.choice(options) #Selects w as a random word from options
    word = [] #Contains the letters of the word that you have to guess
    guess = [] #Contains the underscores and special characters
    errors = [] #Contains the incorrect letters entered by the user
    word_work(w, word, guess) #Fills out word list using characters from the secret word. Fills out the guess list with underscores
    draw_guess(scr, guess) #Draws the text "Word:" using the guesses
    draw_errors(scr, errors) #Draws the errors
    draw_guess_left(scr, errors) #Draws the amount of guesses left using the list of errors
    draw_status_bar(scr) #Draws the status bar
    draw_category(scr) #Draws the category
    while '_' in guess: #While there are underscores in guess
        key = scr.getch() #Gets the code of the key that the user pressed on their keyboard
        letter = chr(key) #Converts the key code into an ASCII character
        letter_work(word, guess, errors, letter) #Checks whether the letter is right or wrong
        if len(errors) == 10: #If the length of errors equals to 10
            scr.clear() #Clears the screen
            draw_message(scr, game_over) #Draws the message
            scr.refresh() #Refreshes the screen
            time.sleep(2) #Waits for 2 seconds
            exit() #Exits the program
        if letter == '1': #If the letter equals to 1
            exit() #Exits the program
        if letter == '2': #If the letter equals to 2
            scr.clear() #Clears the screen
            draw_rules(scr, rules) #Displays the rules
            scr.refresh() #Refreshes the screen
            time.sleep(5) #Waits for 5 seconds
            scr.clear() #Clears the screen
        draw_title(scr,title) #Draws the title
        draw_guess(scr, guess) #Draws the guesses
        draw_errors(scr, errors) #Displays the errors
        draw_echafaud(scr, echafauds[len(errors)]) #Draws the necessary stage of the hangman
        draw_guess_left(scr, errors) #Displays the amount of guesses left
        draw_status_bar(scr) #Draws the status bar
        draw_category(scr) #Draws the category
    scr.clear() #Clears the screen
    draw_message(scr, game_over) #Draws the "game over" message
    scr.refresh() #Refreshes the screen
    time.sleep(2) #Waits for 2 seconds
    exit() #Exits the program

def word_work(str, word, guess): #Function for replacing secret characters with underscores
    for item in str: #For each character in the string
        item = item.upper() #Makes it uppercase
        word.append(item) #Adds it to the end of the word list
        if item.isalpha() != True : #If the character is not a letter
                guess.append(item) #Adds it to the end of guess
        else: #Otherwise
            guess.append('_') #Adds an underscore to the end of guess

def letter_work(word, guess, errors, new_letter): #Function for determining whether the guess if right or wrong
    result = 'Wrong!' #result starts off as "Wrong!"
    new_letter = new_letter.upper() #Makes the letter uppercase
    if new_letter.isalpha() != True: #If the character is not a letter
        result = 'Not a letter' #result is set to "Not a letter"
    else: #If the character is a letter
        if new_letter in errors: #If the letter is already an error
                result = 'Already wrong.' #result is set to "Already wrong."
        elif new_letter in guess: #If the letter was already correct
                result = 'Already right!' #result equals to "Already right!"
        else: #If the letter does not fall under any of those categories
            for i in range(len(word)): #For every letter in the word
                if new_letter == word[i]: #If the letter equals to a secret letter
                    guess[i] = new_letter #guess[i] is changed to that letter
                    result = 'Right!' #result is set to "Right!"
            if result == 'Wrong!': #If result equals to "Wrong!"
                errors.append(new_letter) #Add that letter to the end of the list of errors
    return result #Returns the result

def draw_guess(scr, guess): #Function for drawing the text before the dashes
    scr.attron(curses.color_pair(2)) #Uses the second color pair
    scr.attron(curses.A_BOLD) #Makes the text bold
    start_row = 17 #Starts on the 17th row from the top
    start_col = 48 #Starts on the 48th column
    idx = 0 #Variable idx is set to 0
    scr.addstr(start_row, start_col - 6, 'Word:') #Draws the text "Word:"
    for item in guess: #For each character
        scr.addstr(start_row, start_col + idx, item) #Draws the characters in the designated positions from the guess list
        idx = idx + 2 #idx is increased by 2. Letters are drawn with a space in between them.

def draw_errors(scr, errors): #Function for drawing the errors
    scr.attron(curses.color_pair(1)) #Uses the first color pair
    scr.attron(curses.A_BOLD) #Makes the text bold
    start_row = 18 #Starts on the 18th row from the top
    start_col = 50 #Starts on the 50th column
    idx = 0 #Variable idx is set to 0
    scr.addstr(start_row, start_col - 8, 'Errors:') #Draws the text "Errors:"
    for item in errors: #For each character
        scr.addstr(start_row, start_col + idx, item) #Draw the characters in the designated positions from the errors list
        idx = idx + 2 #idx is increased by 2. Letters are drawn with a space in between them.

def draw_message(scr, drawing): #Function for drawing the "Game Over!" message
    sub = scr.subwin(10,70, 10, 20) #Gives the coordinates for the box
    sub.box() #Draws a box around the text
    sub.attron(curses.color_pair(2)) #Uses the second color pair
    sub.attron(curses.A_BOLD) #Makes the text bold
    start_row = 1 #Starts the text in the 1st row of the box
    start_col = 5 #Starts the text in the 5th column of the box
    idx = 0 #Variable idx is set to 0
    for item in drawing: #For each line of the message
        sub.addstr(start_row + idx, start_col, item) #Prints each line, row by row
        idx = idx + 1 #idx is increased by 1

def draw_status_bar(scr): #Function for drawing the status bar (thing at the bottom of the screen)
    scr.attron(curses.color_pair(1)) #Uses the first color pair
    scr.attron(curses.A_BOLD) #Makes the text bold
    status = "Press 1 to Exit or 2 for Rules" #Assigns a sentence to the status variable
    height, width = scr.getmaxyx() #Gets the screen size in rows and columns
    scr.addstr (height -1, (width//2)-(len(status)//2), status) #Prints the message on the last line of the screen, in the middle

def draw_category(scr): #Function for drawing the category
    scr.attron(curses.color_pair(1)) #Uses the first color pair
    scr.attron(curses.A_BOLD) #Makes the text bold
    start_row = 16 #Starts the text on the 16th row
    start_col = 50 #Starts the text of the 50th row
    category = "Category: Movies" #Assigns text to the category variable
    scr.addstr (start_row, start_col -(len(category)//2), category) #Prints the text in the category variable at the specified position

def draw_guess_left(scr, errors): #Function for drawing the amount of guesses left
    scr.attron(curses.color_pair(2)) #Uses the first color pair
    scr.attron(curses.A_BOLD) #Makes the text bold
    left = "Guesses Left: " + str(10-len(errors)) #Variable is set to text reflecting the amount of guesses left
    if len(errors)>= 1: #If the length of errors is equal to or is bigger than 1
        left = left + ' ' #Left equals left plus a space. Used to remove the trailing zero from the number 10
    start_row = 19 #Starts on the 19th row
    start_col = 42 #Starts on the 42nd column
    scr.addstr (start_row, start_col, left) #Draws left in the designated position

def draw_rules(scr, drawing): #Function for drawing rules
    sub = scr.subwin(10,70, 10, 20) #Gives the coordinates of the box
    sub.box() #Draws the box
    sub.attron(curses.color_pair(2)) #Uses the second color pair
    sub.attron(curses.A_BOLD) #Makes the text bold
    start_row = 1 #Starts the text in the 1st row of the box
    start_col = 5 #Starts the text in the 5th column of the box
    idx = 0 #Variable idx is set to 0
    for item in drawing: #For each line in rules
        sub.addstr(start_row + idx, start_col, item) #Draws each line, column by column
        idx = idx + 1 #idx is increased by 1

def main(): #Main function of the program
    curses.wrapper(draw_screen) #Gives control to the curses library

if __name__ == "__main__": #If script is run as the main program (not as pytest)
    main() #Execute main
