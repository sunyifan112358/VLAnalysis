#!/usr/bin/python

import os

from log_parser import LogParser
from global_stat import GlobalStat
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
from acceptance_welfare_figure import AcceptanceWelfareFigure
from key_stroke_decision_figure import KeyStrokeDecisionFigure
from solution_money_figure import SolutionMoneyFigure
from solution_welfare_figure import SolutionWelfareFigure
from money_welfare_cluster_figure import MoneyWelfareClusterFigure
from bg_money_distribution_figure import BgMoneyDistributionFigure
from bg_welfare_distribution_figure import BgWelfareDistributionFigure
from bg_accept_rant_figure import BgAcceptanceRateFigure
from action_type_figure import ActionTypeFigure
from decision_matrix_figure import DecisionMatrixFigure
from decision_phase_acceptance_figure import DecisionPhaseAcceptanceFigure
from solution_scatter_figure import SolutionScatterFigure


def main():
    files = get_all_files()
    sessions = parse_all_sessions(files)
    
    global_stat = GlobalStat()
    global_stat.calculate(sessions)

    output_data_in_csv(sessions, global_stat)
    plot_all_figures(sessions, global_stat)


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

def output_data_in_csv(sessions, global_stat):
    csv_generator = CsvGenerator()
    csv_generator.generate(sessions, global_stat)

    action_csv_generator = ActionCsvGenerator()
    action_csv_generator.generate(sessions)

def plot_all_figures(sessions, global_stat):
    plot_dendrogram_figure(sessions, global_stat, ['money', 'welfare'], [0], 3)
    plot_dendrogram_figure(sessions, global_stat, ['money', 'welfare'], [1], 3)
    plot_dendrogram_figure(sessions, global_stat, ['money', 'welfare'], [2], 3)
    plot_dendrogram_figure(sessions, global_stat, ['money', 'welfare'], [0, 1, 2], 3)
    plot_dendrogram_figure(sessions, global_stat, ['money'], [0, 1, 2], 3)
    plot_dendrogram_figure(sessions, global_stat, ['welfare'], [0, 1, 2], 3)
    plot_dendrogram_figure(sessions, global_stat, ['action_type'], [0, 1, 2], 5)
    plot_dendrogram_figure(sessions, global_stat, ['action_type'], [0], 4)
    plot_dendrogram_figure(sessions, global_stat, ['action_type'], [1], 5)
    plot_dendrogram_figure(sessions, global_stat, ['action_type'], [2], 5)
    plot_dendrogram_figure(sessions, global_stat, ['action_matrix'], [0], 8,
            False)

    plot_money_welfare_figure(sessions, global_stat, [0])
    plot_money_welfare_figure(sessions, global_stat, [1])
    plot_money_welfare_figure(sessions, global_stat, [2])
    plot_money_welfare_figure(sessions, global_stat, [0, 1, 2])

    plot_money_distribution_figure(sessions)
    plot_money_scatter_figure(sessions)
    plot_welfare_distribution_figure(sessions)
    plot_welfare_scatter_figure(sessions)
    plot_real_time_distribution_figure(sessions)

    plot_acceptance_money_figure(sessions, True)
    plot_acceptance_money_figure(sessions, False)
    plot_acceptance_welfare_figure(sessions, True)
    plot_acceptance_welfare_figure(sessions, False)

    plot_key_stroke_decision_figure(sessions)
    plot_solution_money_figure(sessions)
    plot_solution_welfare_figure(sessions)

    plot_money_welfare_cluster_figure(sessions)

    plot_bg_money_distribution_figure(sessions)
    plot_bg_welfare_distribution_figure(sessions)
    plot_bg_acceptance_rate_figure(sessions)

    plot_action_type_figure(sessions, 0)
    plot_action_type_figure(sessions, 1)
    plot_action_type_figure(sessions, 2)

    plot_decision_phase_acceptance_figure(sessions)
    plot_solution_scatter_figure(sessions)

    for i in range(len(sessions)):
        plot_decision_matrix(sessions, i, 0)



def plot_money_welfare_figure(sessions, global_stat, challenge_number):
    figure = MoneyWelfareFigure()
    figure.set_size(12, 12)
    figure.set_font_size(18)
    figure.set_challenge_number(challenge_number)
    figure.initialize()
    figure.draw(sessions, global_stat)
    figure.save_eps("money_welfare_" + str(challenge_number))
    figure.save_png("money_welfare_" + str(challenge_number))
    figure.close()

def plot_money_distribution_figure(sessions):
    figure = MoneyDistributionFigure()
    figure.set_size(8, 6)
    figure.set_font_size(18)
    figure.initialize()
    figure.draw(sessions)
    figure.save_eps('money_distribution')
    figure.save_png('money_distribution')
    figure.close()

def plot_money_scatter_figure(sessions):
    figure = MoneyScatterFigure()
    figure.set_size(8, 6)
    figure.set_font_size(18)
    figure.initialize()
    figure.draw(sessions)
    figure.save_eps('money_scatter')
    figure.save_png('money_scatter')
    figure.close()

def plot_welfare_distribution_figure(sessions):
    figure = WelfareDistributionFigure()
    figure.set_size(8, 6)
    figure.set_font_size(18)
    figure.initialize()
    figure.draw(sessions)
    figure.save_eps('welfare_distribution')
    figure.save_png('welfare_distribution')
    figure.close()

def plot_welfare_scatter_figure(sessions):
    figure = WelfareScatterFigure()
    figure.set_size(8, 6)
    figure.set_font_size(18)
    figure.initialize()
    figure.draw(sessions)
    figure.save_eps('welfare_scatter')
    figure.save_png('welfare_scatter')
    figure.close()

def plot_real_time_distribution_figure(sessions):
    figure = RealTimeDistributionFigure()
    figure.set_size(8, 6)
    figure.set_font_size(18)
    figure.initialize()
    figure.draw(sessions)
    figure.save_eps('real_time_distribution')
    figure.save_png('real_time_distribution')
    figure.close()

def plot_dendrogram_figure(sessions, global_stat, 
        items, challenge_number, threshold, enable_whiten = True):
    figure = DendrogramFigure()
    figure.set_size(8, 5)
    figure.set_font_size(18)
    figure.initialize()
    figure.based_on_challenge_number(challenge_number)
    figure.based_on_item(items)
    figure.set_threshold(threshold)

    if enable_whiten:
        figure.enable_whiten()

    figure.draw(sessions, global_stat)
    figure.save_eps('dendrogram' + figure.get_tag_name())
    figure.save_png('dendrogram' + figure.get_tag_name())
    figure.close()

def plot_acceptance_money_figure(sessions, win):
    figure = AcceptanceMoneyFigure()
    figure.set_size(8, 6)
    figure.set_font_size(18)
    if win:
        figure.SkipChallenge1Lose()
    else:
        figure.SkipChallenge1Win()
    figure.initialize()
    figure.draw(sessions)

    file_name = "acceptance_money_c1_win"
    if not win:
      file_name = "acceptance_money_c1_lose"
    figure.save_eps(file_name)
    figure.save_png(file_name)
    figure.close()

def plot_acceptance_welfare_figure(sessions, win):
    figure = AcceptanceMoneyFigure()
    figure.set_size(8, 6)
    figure.set_font_size(18)
    figure.UseWelfare()
    if win:
        figure.SkipChallenge1Lose()
    else:
        figure.SkipChallenge1Win()
    figure.initialize()
    figure.draw(sessions)

    file_name = "acceptance_welfare_c1_win"
    if not win:
      file_name = "acceptance_welfare_c1_lose"
    figure.save_eps(file_name)
    figure.save_png(file_name)
    figure.close()

def plot_key_stroke_decision_figure(sessions):
    figure = KeyStrokeDecisionFigure()
    figure.set_size(8, 6)
    figure.set_font_size(18)
    figure.initialize()
    figure.draw(sessions)
    figure.save_eps('key_stroke_decision')
    figure.save_png('key_stroke_decision')
    figure.close()

def plot_solution_money_figure(sessions):
    figure = SolutionMoneyFigure()
    figure.set_size(8, 4)
    figure.set_font_size(18)
    figure.initialize()
    figure.draw(sessions)
    figure.save_eps('solution_money')
    figure.save_png('solution_money')
    figure.close()


def plot_solution_welfare_figure(sessions):
    figure = SolutionWelfareFigure()
    figure.set_size(8, 4)
    figure.set_font_size(18)
    figure.initialize()
    figure.draw(sessions)
    figure.save_eps('solution_welfare')
    figure.save_png('solution_welfare')
    figure.close()

def plot_money_welfare_cluster_figure(sessions):
    figure = MoneyWelfareClusterFigure()
    figure.set_size(8, 6)
    figure.set_font_size(18)
    figure.initialize()
    figure.draw(sessions)
    figure.save_eps('money_welfare_cluster')
    figure.save_png('money_welfare_cluster')
    figure.close()

def plot_bg_money_distribution_figure(sessions):
    figure = BgMoneyDistributionFigure()
    figure.set_size(8, 6)
    figure.set_font_size(18)
    figure.initialize()
    figure.draw(sessions)
    figure.save_eps('bg_money_distribution')
    figure.save_png('bg_money_distribution')
    figure.close()

def plot_bg_welfare_distribution_figure(sessions):
    figure = BgWelfareDistributionFigure()
    figure.set_size(8, 6)
    figure.set_font_size(18)
    figure.initialize()
    figure.draw(sessions)
    figure.save_eps('bg_welfare_distribution')
    figure.save_png('bg_welfare_distribution')
    figure.close()

def plot_bg_acceptance_rate_figure(sessions):
    figure = BgAcceptanceRateFigure()
    figure.set_size(8, 6)
    figure.set_font_size(18)
    figure.initialize()
    figure.draw(sessions)
    figure.save_eps('bg_acceptance_rate')
    figure.save_png('bg_acceptance_rate')
    figure.close()

def plot_action_type_figure(sessions, challenge_number):
    figure = ActionTypeFigure()
    figure.set_challenge_number(challenge_number)
    figure.set_size(8, 5)
    figure.set_font_size(18)
    figure.initialize()
    figure.draw(sessions)
    figure.save_eps('action_type_rate_' + str(challenge_number))
    figure.save_png('action_type_rate_' + str(challenge_number))
    figure.close()

def plot_decision_matrix(sessions, session_id, challenge_id):
    session = sessions[session_id]

    if len(session.challenge) <= challenge_id:
        return
    challenge = session.challenge[challenge_id]

    figure = DecisionMatrixFigure()
    figure.set_size(8, 5)
    figure.set_font_size(18)
    figure.initialize()
    figure.draw(session, challenge)
    figure.save_eps('decision_matrix_' + str(session.name) + '_' +
            str(challenge_id))
    figure.save_png('decision_matrix_' + str(session.name) + '_' +
            str(challenge_id))
    figure.close()

 
def plot_decision_phase_acceptance_figure(sessions):
    figure = DecisionPhaseAcceptanceFigure()
    figure.set_size(8, 6)
    figure.set_font_size(18)
    figure.initialize()
    figure.draw(sessions)
    figure.save_eps('decision_phase_acceptance_figure')
    figure.save_png('decision_phase_acceptance_figure')
    figure.close()


def plot_solution_scatter_figure(sessions):
    figure = SolutionScatterFigure()
    figure.set_size(8, 5)
    figure.set_font_size(18)
    figure.initialize()
    figure.draw(sessions)
    figure.save_eps('solution_scatter_figure')
    figure.save_png('solution_scatter_figure')
    figure.close()




if __name__ == "__main__":
    main();
