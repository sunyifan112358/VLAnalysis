#!/usr/bin/python

import os

from log_parser import LogParser
from money_welfare_figure import MoneyWelfareFigure
from money_distribution_figure import MoneyDistributionFigure
from money_scatter_figure import MoneyScatterFigure
from welfare_distribution_figure import WelfareDistributionFigure

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
    plot_money_distribution_figure(sessions)
    plot_money_scatter_figure(sessions)
    plot_welfare_distribution_figure(sessions)

def plot_money_welfare_figure(sessions):
    figure = MoneyWelfareFigure()
    figure.set_size(8, 6)
    figure.set_font_size(18)
    figure.initialize()
    figure.draw(sessions)
    figure.save_eps("money_welfare")

def plot_money_distribution_figure(sessions):
    figure = MoneyDistributionFigure()
    figure.set_size(8, 6)
    figure.set_font_size(18)
    figure.initialize()
    figure.draw(sessions)
    figure.save_eps('money_distribution')

def plot_money_scatter_figure(sessions):
    figure = MoneyScatterFigure()
    figure.set_size(8, 6)
    figure.set_font_size(18)
    figure.initialize()
    figure.draw(sessions)
    figure.save_eps('money_scatter')

def plot_welfare_distribution_figure(sessions):
    figure = WelfareDistributionFigure()
    figure.set_size(8, 6)
    figure.set_font_size(18)
    figure.initialize()
    figure.draw(sessions)
    figure.save_eps('welfare_distribution')



if __name__ == "__main__":
    main();
