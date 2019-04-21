#!/usr/bin/env python3
import time
import curses

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
    start_row = 2
    start_col = 17
    idx = 0
    for item in drawing:
        scr.addstr(start_row + idx, start_col, item)
        idx = idx + 1

def draw_echafaud(scr, drawing):
    scr.attron(curses.color_pair(2))
    scr.attron(curses.A_BOLD)
    start_row = 8
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
    n = 0
    key = 0
    scr.clear()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    draw_title(scr,title)
    for i in range(10):
        required = echafauds[i]
        draw_echafaud(scr, required)
        scr.refresh()
        time.sleep(1)
    while (key != ord('q')):
        key = scr.getch()

def main():
    curses.wrapper(draw_screen)

if __name__ == "__main__":
    main()
