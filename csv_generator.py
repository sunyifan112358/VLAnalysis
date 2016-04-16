class CsvGenerator(object):

    def __init__(self):
        pass

    def generate(self, sessions):
        csv_file = open("data.csv", "w")
        csv_file.write(
                'session_id, '
                'tag,'
                'c1.money, c1.welfare, '
                'c1.dock_utilization, '
                'c1.real_time, '
                'c1.accp_recommendation, '
                'c1.total_recommendation, '
                'c1.solution, '
                'c1.num_key_action, '
                'c2.money, c2.welfare, '
                'c2.dock_utilization, '
                'c2.real_time, '
                'c2.accp_recommendation, '
                'c2.total_recommendation, '
                'c2.solution, '
                'c2.num_key_action, '
                'c3.money, c3.welfare, '
                'c3.dock_utilization, '
                'c3.real_time, '
                'c3.accp_recommendation, '
                'c3.total_recommendation, '
                'c3.solution, '
                'c3.num_key_action'
                '\n')

        for session in sessions:
            csv_file.write(
                '' + str(session.id) + ', '
                '' + str(session.bg_tag) + ', ')
            for challenge in session.challenge:
                csv_file.write(
                    '' + str(challenge.money) + ', '
                    '' + str(challenge.welfare) + ', '
                    '' + str(challenge.dock_utilization) + ', '
                    '' + str(challenge.get_real_duration()) + ', '
                    '' + str(challenge.accepted_recommendation) + ', '
                    '' + str(challenge.total_recommendation) + ', '
                    '' + str(challenge.get_oil_cleaning_solution()) + ', '
                    '' + str(challenge.num_key_action) + '')
                if challenge != session.challenge[2]:
                    csv_file.write(', ')
            csv_file.write('\n')
