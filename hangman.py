#!/usr/bin/env python3

import curses

title = []

def read_title():
    drawing = []
    with open('title.txt') as f:
        for line in f:
            line = line.rstrip('\n')
            drawing.append(line)
    return drawing

def draw_title(scr, drawing):
    scr.attron(curses.color_pair(1))
    scr.attron(curses.A_BOLD)
    start_row = 2
    start_col = 13
    idx = 0
    for item in drawing:
        scr.addstr(start_row + idx, start_col, item)
        idx = idx + 1
    

def draw_screen(scr):
    key = 0
    scr.clear()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    draw_title(scr,title)
    scr.refresh()
    while (key != ord('q')):
        key = scr.getch()

def main():
    title = read_title()
    curses.wrapper(draw_screen)
    
if __name__ == "__main__":
    main()
    
