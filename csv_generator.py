class CsvGenerator(object):

    def __init__(self):
        pass

    def generate(self, sessions):
        csv_file = open("data.csv", "w")
        csv_file.write(
                'c1.money, c1.welfare, c1.real_time, '
                'c2.money, c2.welfare, c2.real_time, '
                'c3.money, c3.welfare, c3.real_time'
                '\n')

        for session in sessions:
            c1 = session.challenge1
            c2 = session.challenge2
            c3 = session.challenge3
            csv_file.write(
                '' + str(c1.money) + ', '
                '' + str(c1.welfare) + ', '
                '' + str(c1.get_real_duration()) + ', '
                '' + str(c2.money) + ', '
                '' + str(c2.welfare) + ', '
                '' + str(c2.get_real_duration()) + ', '
                '' + str(c3.money) + ', '
                '' + str(c3.welfare) + ', ' 
                '' + str(c3.get_real_duration()) + ''
                '\n')
