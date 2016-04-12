#!/usr/bin/python

import os
from log_parser import LogParser
from money_welfare_figure import MoneyWelfareFigure

def main():
    files = get_all_files()
    sessions = parse_all_sessions(files)

    for session in sessions:
        print(session)

    mwFigure = MoneyWelfareFigure()
    mwFigure.set_size(8, 6)
    mwFigure.initialize()
    mwFigure.draw(sessions)
    mwFigure.show()
    
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

if __name__ == "__main__":
    main();
