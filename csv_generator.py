class CsvGenerator(object):

    def __init__(self):
        pass

    def generate(self, sessions):
        csv_file = open("data.csv", "w")
        csv_file.write(
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
            c1 = session.challenge1
            c2 = session.challenge2
            c3 = session.challenge3
            csv_file.write(
                '' + str(c1.money) + ', '
                '' + str(c1.welfare) + ', '
                '' + str(c1.dock_utilization) + ', '
                '' + str(c1.get_real_duration()) + ', '
                '' + str(c1.accepted_recommendation) + ', '
                '' + str(c1.total_recommendation) + ', '
                '' + str(c1.get_oil_cleaning_solution()) + ', '
                '' + str(c1.num_key_action) + ', '
                '' + str(c2.money) + ', '
                '' + str(c2.welfare) + ', '
                '' + str(c2.dock_utilization) + ', '
                '' + str(c2.get_real_duration()) + ', '
                '' + str(c2.accepted_recommendation) + ', '
                '' + str(c2.total_recommendation) + ', '
                '' + str(c2.get_oil_cleaning_solution()) + ', '
                '' + str(c2.num_key_action) + ', '
                '' + str(c3.money) + ', '
                '' + str(c3.welfare) + ', ' 
                '' + str(c3.dock_utilization) + ', '
                '' + str(c3.get_real_duration()) + ', '
                '' + str(c3.accepted_recommendation) + ', '
                '' + str(c3.total_recommendation) + ', '
                '' + str(c3.get_oil_cleaning_solution()) + ', '
                '' + str(c3.num_key_action) + ''
                '\n')
