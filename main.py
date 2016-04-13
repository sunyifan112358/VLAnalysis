#!/usr/bin/python

import os

from log_parser import LogParser
from csv_generator import CsvGenerator
from money_welfare_figure import MoneyWelfareFigure
from money_distribution_figure import MoneyDistributionFigure
from money_scatter_figure import MoneyScatterFigure
from welfare_distribution_figure import WelfareDistributionFigure
from welfare_scatter_figure import WelfareScatterFigure
from real_time_distribution_figure import RealTimeDistributionFigure
from dendrogram_figure import DendrogramFigure
from acceptance_money_figure import AcceptanceMoneyFigure

def main():
    files = get_all_files()
    sessions = parse_all_sessions(files)

    for session in sessions:
        print(session)

    output_data_in_csv(sessions)

    plot_all_figures(sessions)

def get_all_files():
    all_files = os.listdir("raw_data")
    files = []
    for f in all_files:
        if f.endswith('.json'):
            files.append(f)
    print(files)
    return files
    
def parse_all_sessions(files):
    logParser = LogParser();
    sessions = [];
    
    for file in files:
        session = logParser.parse(file)
        sessions.append(session)
        
    return sessions

def output_data_in_csv(sessions):
    csv_generator = CsvGenerator()
    csv_generator.generate(sessions)

def plot_all_figures(sessions):
    plot_money_welfare_figure(sessions)
    plot_money_distribution_figure(sessions)
    plot_money_scatter_figure(sessions)
    plot_welfare_distribution_figure(sessions)
    plot_welfare_scatter_figure(sessions)
    plot_real_time_distribution_figure(sessions)
    plot_dendrogram_figure(sessions)
    plot_acceptance_money_figure(sessions)

def plot_money_welfare_figure(sessions):
    figure = MoneyWelfareFigure()
    figure.set_size(8, 6)
    figure.set_font_size(18)
    figure.initialize()
    figure.draw(sessions)
    figure.save_eps("money_welfare")
    figure.save_png("money_welfare")

def plot_money_distribution_figure(sessions):
    figure = MoneyDistributionFigure()
    figure.set_size(8, 6)
    figure.set_font_size(18)
    figure.initialize()
    figure.draw(sessions)
    figure.save_eps('money_distribution')
    figure.save_png('money_distribution')

def plot_money_scatter_figure(sessions):
    figure = MoneyScatterFigure()
    figure.set_size(8, 6)
    figure.set_font_size(18)
    figure.initialize()
    figure.draw(sessions)
    figure.save_eps('money_scatter')
    figure.save_png('money_scatter')

def plot_welfare_distribution_figure(sessions):
    figure = WelfareDistributionFigure()
    figure.set_size(8, 6)
    figure.set_font_size(18)
    figure.initialize()
    figure.draw(sessions)
    figure.save_eps('welfare_distribution')
    figure.save_png('welfare_distribution')

def plot_welfare_scatter_figure(sessions):
    figure = WelfareScatterFigure()
    figure.set_size(8, 6)
    figure.set_font_size(18)
    figure.initialize()
    figure.draw(sessions)
    figure.save_eps('welfare_scatter')
    figure.save_png('welfare_scatter')

def plot_real_time_distribution_figure(sessions):
    figure = RealTimeDistributionFigure()
    figure.set_size(8, 6)
    figure.set_font_size(18)
    figure.initialize()
    figure.draw(sessions)
    figure.save_eps('real_time_distribution')
    figure.save_png('real_time_distribution')

def plot_dendrogram_figure(sessions):
    figure = DendrogramFigure()
    figure.set_size(8, 6)
    figure.set_font_size(18)
    figure.initialize()
    figure.draw(sessions)
    figure.save_eps('dendrogram')
    figure.save_png('dendrogram')

def plot_acceptance_money_figure(sessions):
    figure = AcceptanceMoneyFigure()
    figure.set_size(8, 6)
    figure.set_font_size(18)
    figure.initialize()
    figure.draw(sessions)
    figure.save_eps('acceptance_money')
    figure.save_png('acceptance_money')


if __name__ == "__main__":
    main();
