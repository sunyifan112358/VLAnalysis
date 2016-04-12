#!/usr/bin/python

import os
from log_parser import LogParser
from money_welfare_figure import MoneyWelfareFigure

def main():
    files = get_all_files()
    sessions = parse_all_sessions(files)

    for session in sessions:
        print(session)

    plot_all_figures(sessions)

def get_all_files():
    files = os.listdir("raw_data")
    return files
    
def parse_all_sessions(files):
    logParser = LogParser();
    sessions = [];
    
    for file in files:
        session = logParser.parse(file)
        sessions.append(session)
        
    return sessions

def plot_all_figures(sessions):
    plot_money_welfare_figure(sessions)

def plot_money_welfare_figure(sessions):
    figure = MoneyWelfareFigure()
    figure.set_size(8, 6)
    figure.initialize()
    figure.draw(sessions)
    figure.show()

if __name__ == "__main__":
    main();
