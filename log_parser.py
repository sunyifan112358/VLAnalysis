import re

from session import Session
from run import Run

class LogParser(object):
    
    def __init__(self):
        self.session = None

        self.session_begin_re = re.compile(
            '{"type":"session_begin", "data":{"game_id":"VistaLights", ' +
            '"player_id":"[0-9a-fA-F\-]+", "session_id":"[0-9a-fA-F\-]+", ' +
            '"build_id":"", "version":"2.0", "condition":"", ' +
            '"client_time":"([0-9\.]+)", "details":{}}}')

        self.session_end_re = re.compile(
            '{"type":"session_end", "data":{"session_id":"[0-9a-fA-F/-]+", ' +
            '"run_count":"[0-9]+", "client_time":"[0-9\.]+", "details":{}}}')

        self.run_begin_re = re.compile(
            '{"type":"run_begin", "data":{"session_id":"[a-fA-F0-9\-]+", ' +
            '"run_id":"[a-fA-F0-9\-]+", "run_seqno":"([0-9]+)", ' +
            '"client_time":"([0-9\.]+)", "details":{"current_time":' +
            '"([0-9]+/[0-9]+/[0-9]+ [0-9]+:[0-9]+:[0-9]+(?: [AP]M)?)", ' +
            '"map":"(houston_game_[0-9])", ' +
            '"give_recommendation":"(True|False)", ' +
            '"with_justification":"(True|False)"}}}')

        self.run_end_re = re.compile(
            '{"type":"run_end", "data":{"run_id":"[0-9a-fA-f\-]+", ' +
            '"action_count":"[0-9]+", "client_time":"([0-9\.]+)", ' +
            '"details":{"current_time":' +
            '"([0-9]+/[0-9]+/[0-9]+ [0-9]+:[0-9]+:[0-9]+(?: [AP]M)?)", ' +
            '"budget":"([0-9\.\-E]+)", "welfare":"([0-9\.\-E]+)", ' +
            '"dock_utilization":"([0-9\.\-E]+)"}}}')
    
    def parse(self, file_name):
        self.file_name = file_name
        file = open("raw_data/" + file_name)
        lines = file.readlines()

        for line in lines:
            self.process_line(line)

        return self.session

    def process_line(self, line):
        if self.try_session_begin(line):
            return

        if self.try_run_begin(line):
            return

        if self.try_run_end(line):
            return

        if self.try_session_end(line):
            return

    def try_session_begin(self, line):
        match = self.session_begin_re.match(line)
        if match != None:
            self.create_session()
            return True
        return False

    def create_session(self):
        self.session = Session()
        self.session.name = self.file_name
        print("Session created: " + self.file_name)

    def try_session_end(self, line):
        if self.session_end_re.match(line) != None:
            self.end_session()
            return True
        return False

    def end_session(self):
        print("Session ended")
    
    def try_run_begin(self, line):
        match = self.run_begin_re.match(line) 
        if match != None:
            self.create_run(match)
            return True
        return False

    def create_run(self, match):
        self.run = Run()

        map_name = match.group(4)
        self.run.map_file = map_name
        if map_name == 'houston_game_0':
            self.run.is_tutorial = True
        elif map_name == 'houston_game_1':
            self.session.challenge1 = self.run
        elif map_name == 'houston_game_2':
            self.session.challenge2 = self.run
        elif map_name == 'houston_game_3':
            self.session.challenge3 = self.run

        self.run.give_recommendation = (match.group(5) == 'True')
        self.run.with_justification = (match.group(6) == 'True')

        self.run.start_real_time = float(match.group(2))

    def try_run_end(self, line):
        match = self.run_end_re.match(line)
        if match != None:
            self.end_run(match)
        
    def end_run(self, match):
        self.run.money = float(match.group(3))
        self.run.welfare = float(match.group(4))
        self.run.dock_utilization = float(match.group(5))
        self.run.end_real_time = float(match.group(1))

        self.run = None

    

        

