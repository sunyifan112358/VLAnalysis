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
            count = 0
            for challenge in session.challenge:
                count += 1
                if challenge != None:
                    csv_file.write(
                        '' + str(challenge.money) + ', '
                        '' + str(challenge.welfare) + ', '
                        '' + str(challenge.dock_utilization) + ', '
                        '' + str(challenge.get_real_duration()) + ', '
                        '' + str(challenge.accepted_recommendation) + ', '
                        '' + str(challenge.total_recommendation) + ', '
                        '' + str(challenge.get_oil_cleaning_solution()) + ', '
                        '' + str(challenge.num_key_action) + '')
                else:
                    csv_file.write(
                        '' + str(None) + ', '
                        '' + str(None) + ', '
                        '' + str(None) + ', '
                        '' + str(None)+ ', '
                        '' + str(None) + ', '
                        '' + str(None) + ', '
                        '' + str(None)+ ', '
                        '' + str(None) + '')


                if count != 3:
                    csv_file.write(', ')
            csv_file.write('\n')
