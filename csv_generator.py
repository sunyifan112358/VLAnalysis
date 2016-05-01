class CsvGenerator(object):

    def __init__(self):
        pass

    def generate(self, sessions, global_stat):
        csv_file = open("data.csv", "w")
        csv_file.write(
                'file, '
                'session_id, '
                'tag,'
                'c1.money, c1.welfare, '
                'c1.pri_money, c1.pri_welfare, '
                'c1.dock_utilization, '
                'c1.real_time, '
                'c1.decision_time, '
                'c1.accp_recommendation, '
                'c1.total_recommendation, '
                'c1.priority_change, '
                'c1.priority_change(1-3), '
                'c1.priority_change(4-8), '
                'c1.priority_change(9-99), '
                'c1.solution, '
                'c1.win, '
                'c1.num_key_action, '
                'c2.money, c2.welfare, '
                'c2.pri_money, c2.pri_welfare, '
                'c2.dock_utilization, '
                'c2.real_time, '
                'c2.decision_time, '
                'c2.accp_recommendation, '
                'c2.total_recommendation, '
                'c2.priority_change, '
                'c2.priority_change(1-3), '
                'c2.priority_change(4-8), '
                'c2.priority_change(9-99), '
                'c2.solution, '
                'c2.win, '
                'c2.num_key_action, '
                'c3.money, c3.welfare, '
                'c3.pri_money, c3.pri_welfare, '
                'c3.dock_utilization, '
                'c3.real_time, '
                'c3.decision_time, '
                'c3.accp_recommendation, '
                'c3.total_recommendation, '
                'c3.priority_change, '
                'c3.priority_change(1-3), '
                'c3.priority_change(4-8), '
                'c3.priority_change(9-99), '
                'c3.solution, '
                'c3.win, '
                'c3.num_key_action'
                '\n')

        for session in sessions:
            csv_file.write(
                '' + str(session.name) + ', '
                '' + str(session.id) + ', '
                '' + str(session.bg_tag) + ', ')
            count = 0
            for challenge in session.challenge:
                count += 1
                csv_file.write(
                    '' + str(challenge.money) + ', '
                    '' + str(challenge.welfare) + ', '
                    '' + str(challenge.get_pri_money(count - 1, global_stat)) + ', '
                    '' + str(challenge.get_pri_welfare(count - 1, global_stat)) + ', '
                    '' + str(challenge.dock_utilization) + ', '
                    '' + str(challenge.get_real_duration()) + ', '
                    '' + str(challenge.get_total_decision_time()) + ', '
                    '' + str(challenge.accepted_recommendation) + ', '
                    '' + str(challenge.total_recommendation) + ', '
                    '' + str(challenge.get_num_priority_change()) + ', '
                    '' + str(challenge.get_num_priority_change(1, 3)) + ', '
                    '' + str(challenge.get_num_priority_change(4, 8)) + ', '
                    '' + str(challenge.get_num_priority_change(9, 99)) + ', '
                    '' + str(challenge.get_oil_cleaning_solution()) + ', '
                    '' + str(session.is_win(count - 1)) + ', '
                    '' + str(challenge.num_key_action) + '')
                if count != 3:
                    csv_file.write(', ')
            csv_file.write('\n')
