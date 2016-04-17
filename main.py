#!/usr/bin/python

import os

from log_parser import LogParser
from csv_generator import CsvGenerator
from action_csv_generator import ActionCsvGenerator
from money_welfare_figure import MoneyWelfareFigure
from money_distribution_figure import MoneyDistributionFigure
from money_scatter_figure import MoneyScatterFigure
from welfare_distribution_figure import WelfareDistributionFigure
from welfare_scatter_figure import WelfareScatterFigure
from real_time_distribution_figure import RealTimeDistributionFigure
from dendrogram_figure import DendrogramFigure
from acceptance_money_figure import AcceptanceMoneyFigure
from key_stroke_decision_figure import KeyStrokeDecisionFigure
from solution_money_figure import SolutionMoneyFigure
from solution_welfare_figure import SolutionWelfareFigure
from money_welfare_cluster_figure import MoneyWelfareClusterFigure
from bg_money_distribution_figure import BgMoneyDistributionFigure
from bg_welfare_distribution_figure import BgWelfareDistributionFigure
from bg_accept_rant_figure import BgAcceptanceRateFigure


def main():
    files = get_all_files()
    sessions = parse_all_sessions(files)
    
    for session in sessions:
        print(session)

    output_data_in_csv(sessions)
    plot_all_figures(sessions)

    for session in sessions:
        print(session)

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

    action_csv_generator = ActionCsvGenerator()
    action_csv_generator.generate(sessions)

def plot_all_figures(sessions):
    plot_dendrogram_figure(sessions, ['money', 'welfare'], [0])
    plot_dendrogram_figure(sessions, ['money', 'welfare'], [1])
    plot_dendrogram_figure(sessions, ['money', 'welfare'], [2])
    plot_dendrogram_figure(sessions, ['money'], [0, 1, 2])
    plot_dendrogram_figure(sessions, ['welfare'], [0, 1, 2])

    plot_money_welfare_figure(sessions)
    plot_money_distribution_figure(sessions)
    plot_money_scatter_figure(sessions)
    plot_welfare_distribution_figure(sessions)
    plot_welfare_scatter_figure(sessions)
    plot_real_time_distribution_figure(sessions)

    plot_acceptance_money_figure(sessions)
    plot_key_stroke_decision_figure(sessions)
    plot_solution_money_figure(sessions)
    plot_solution_welfare_figure(sessions)

    plot_money_welfare_cluster_figure(sessions)

    plot_bg_money_distribution_figure(sessions)
    plot_bg_welfare_distribution_figure(sessions)
    plot_bg_acceptance_rate_figure(sessions)

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

def plot_dendrogram_figure(sessions, items, challenge_number):
    figure = DendrogramFigure()
    figure.set_size(8, 6)
    figure.set_font_size(18)
    figure.initialize()
    figure.based_on_challenge_number(challenge_number)
    figure.based_on_item(items)
    figure.draw(sessions)
    figure.save_eps('dendrogram' + figure.get_tag_name())
    figure.save_png('dendrogram' + figure.get_tag_name())

def plot_acceptance_money_figure(sessions):
    figure = AcceptanceMoneyFigure()
    figure.set_size(8, 6)
    figure.set_font_size(18)
    figure.initialize()
    figure.draw(sessions)
    figure.save_eps('acceptance_money')
    figure.save_png('acceptance_money')

def plot_key_stroke_decision_figure(sessions):
    figure = KeyStrokeDecisionFigure()
    figure.set_size(8, 6)
    figure.set_font_size(18)
    figure.initialize()
    figure.draw(sessions)
    figure.save_eps('key_stroke_decision')
    figure.save_png('key_stroke_decision')

def plot_solution_money_figure(sessions):
    figure = SolutionMoneyFigure()
    figure.set_size(8, 6)
    figure.set_font_size(18)
    figure.initialize()
    figure.draw(sessions)
    figure.save_eps('solution_money')
    figure.save_png('solution_money')


def plot_solution_welfare_figure(sessions):
    figure = SolutionWelfareFigure()
    figure.set_size(8, 6)
    figure.set_font_size(18)
    figure.initialize()
    figure.draw(sessions)
    figure.save_eps('solution_welfare')
    figure.save_png('solution_welfare')

def plot_money_welfare_cluster_figure(sessions):
    figure = MoneyWelfareClusterFigure()
    figure.set_size(8, 6)
    figure.set_font_size(18)
    figure.initialize()
    figure.draw(sessions)
    figure.save_eps('money_welfare_cluster')
    figure.save_png('money_welfare_cluster')

def plot_bg_money_distribution_figure(sessions):
    figure = BgMoneyDistributionFigure()
    figure.set_size(8, 6)
    figure.set_font_size(18)
    figure.initialize()
    figure.draw(sessions)
    figure.save_eps('bg_money_distribution')
    figure.save_png('bg_money_distribution')

def plot_bg_welfare_distribution_figure(sessions):
    figure = BgWelfareDistributionFigure()
    figure.set_size(8, 6)
    figure.set_font_size(18)
    figure.initialize()
    figure.draw(sessions)
    figure.save_eps('bg_welfare_distribution')
    figure.save_png('bg_welfare_distribution')

def plot_bg_acceptance_rate_figure(sessions):
    figure = BgAcceptanceRateFigure()
    figure.set_size(8, 6)
    figure.set_font_size(18)
    figure.initialize()
    figure.draw(sessions)
    figure.save_eps('bg_acceptance_rate')
    figure.save_png('bg_acceptance_rate')

   


if __name__ == "__main__":
    main();
