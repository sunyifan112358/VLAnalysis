import re
import time
import json

from session import Session
from run import Run
from key_stroke_action import KeyStrokeAction
from recommendation_action import RecommendationAction
from phase_action import PhaseAction
from priority_action import PriorityAction
from cleaning_action import CleaningAction

class LogParser(object):
    
    def __init__(self):
        self.session = None
        self.next_session_id = 1

        self.session_begin_re = re.compile(
            r'{"type":"session_begin", "data":{"game_id":"VistaLights", "player_id":"n/a", "session_id":"[0-9a-fA-F\-]+", "build_id":"", "version":"2.0", "condition":"", "client_time":"([0-9\.]+)", "details":{}}}'
            )

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

        self.key_stroke_action_re = re.compile(
            '{"type":"action", "data":{"run_id":"[0-9a-fA-F\-]+", '
            '"action_seqno":"[0-9]+", "type":"[0-9]+", '
            '"client_time":"([0-9\.E\-]+)", '
            '"details":{"current_time":"([0-9]+/[0-9]+/[0-9]+ '
            '[0-9]+:[0-9]+:[0-9]+(?: [AP]M)?)", "keystroke":"([A-Za-z0-9]+)", '
            '"mouse_x":"([0-9\.E\-]+)", "mouse_y":"([0-9\.E\-]+)"}}}')

        self.recommendation_action_re = re.compile(
            '{"type":"action", "data":{"run_id":"[0-9a-fA-F\-]+", '
            '"action_seqno":"[0-9]+", "type":"[0-9]+", '
            '"client_time":"([0-9\.E\-]+)", '
            '"details":{"current_time":"([0-9]+/[0-9]+/[0-9]+ '
            '[0-9]+:[0-9]+:[0-9]+(?: [AP]M)?)", "isAccepted":"(True|False)", '
            '"ship":"([0-9]+)", "priority":"([0-9]+)"*')

        self.phase_action_re = re.compile(
            '{"type":"action", "data":{"run_id":"[0-9a-fA-f\-]+", '
            '"action_seqno":"[0-9]+", "type":"[0-9]+", '
            '"client_time":"([0-9\.E\-]+)", '
            '"details":{"current_time":'
            '"([0-9]+/[0-9]+/[0-9]+ [0-9]+:[0-9]+:[0-9]+(?: [AP]M)?)", '
            '"phase":"(Decision|Simulation)"'
            '(, "money":"([0-9\.E\-]+)", '
            '"welfare":"([0-9\.E\-]+)")?'
            '}}}')

        self.priority_action_re = re.compile(
            '{"type":"action", "data":{"run_id":"[0-9a-fA-F\-]+", '
            '"action_seqno":"[0-9]+", "type":"[0-9]+", '
            '"client_time":"([0-9E\-\.]+)", "details":{"current_time":'
            '"([0-9]+/[0-9]+/[0-9]+ [0-9]+:[0-9]+:[0-9]+(?: [AP]M)?)", '
            '"ship_id":"([0-9]+)", "new_priority":"([0-9]+)"}}}')

        self.cleaning_action_re = re.compile(
            '{"type":"action", "data":{"run_id":"[0-9a-fA-f\-]+", '
            '"action_seqno":"[0-9]+", "type":"[0-9]+", "client_time":'
            '"([0-9\.\-E]+)", "details":{"current_time":'
            '"([0-9]+/[0-9]+/[0-9]+ [0-9]+:[0-9]+:[0-9]+(?: [AP]M)?)", '
            '"solution":"([a-zA-Z]+)"}}}')
    
    def parse(self, file_name):
        self.file_name = file_name
        file = open("raw_data/" + file_name)
        lines = file.readlines()

        for line in lines:
            # self.process_line(line)
            entry = json.loads(line)
            self.process_entry(entry)
            print entry

        session = self.session
        self.session = None
        return session

    def process_entry(self, entry):
        if entry['type'] == 'session_begin':
            self.create_session(entry)
        elif entry['type'] == "run_begin":
            self.create_run(entry)
        elif entry['type'] == "action":
            pass
        elif entry['type'] == "run_end":
            self.end_run(entry)
        else:
            # ignore
            pass


    def create_session(self, entry):
        self.session = Session()
        self.session.name = self.file_name[0:-5]

        self.session.id = self.next_session_id
        self.next_session_id += 1

        print("Session created: " + self.file_name)

    def create_run(self, entry):
        self.run = Run()
        print entry

        self.run.map_file = entry["data"]["details"]["map"]
        #
        # self.run.give_recommendation = (match.group(5) == 'True')
        # self.run.with_justification = (match.group(6) == 'True')
        #
        # self.run.start_real_time = float(match.group(2))

        self.session.add_run(self.run)

    def end_run(self, entry):
        # self.run.money = float(match.group(3))
        # self.run.welfare = float(match.group(4))
        # self.run.dock_utilization = float(match.group(5))
        # self.run.end_real_time = float(match.group(1))
        #
        # if self.run.map_file == 'houston_game_0':
        #     self.run.is_tutorial = True
        pass

    def try_key_stroke_action(self, line):
        match = self.key_stroke_action_re.match(line)
        if match != None:
            self.create_key_stroke_action(match)
            return True
        return False

    def create_key_stroke_action(self, match):
        action = KeyStrokeAction()
        action.real_time = float(match.group(1))
        action.virtual_time = self.parse_time(match.group(2))
        action.key = match.group(3)
        action.mouse_x = float(match.group(4))
        action.mouse_y = float(match.group(5))

        self.run.add_action(action)
        self.run.num_key_action += 1

    def parse_time(self, time_string):
        if 'M' in time_string:
            return time.strptime(time_string, "%m/%d/%Y %I:%M:%S %p")
        else:
            return time.strptime(time_string, "%m/%d/%Y %H:%M:%S")

    def try_recommendation_action(self, line):
        match = self.recommendation_action_re.match(line)
        if match != None:
            self.create_recommendation_action(match)
            return True
        return False

    def create_recommendation_action(self, match):
        action = RecommendationAction()
        action.real_time = float(match.group(1))
        action.virtual_time = self.parse_time(match.group(2))
        action.accepted = (match.group(3) == 'True')
        action.ship_id = int(match.group(4))
        action.priority = int(match.group(5))

        self.run.add_action(action)
        self.run.total_recommendation += 1
        if action.accepted:
            self.run.accepted_recommendation += 1

    def try_phase_action(self, line):
        match = self.phase_action_re.match(line)
        if match != None:
            self.create_phase_action(match)
            return True
        return False

    def create_phase_action(self, match):
        action = PhaseAction()
        action.real_time = float(match.group(1))
        action.virtual_time = self.parse_time(match.group(2))
        action.phase = match.group(3)

        if match.group(5):
            action.money = float(match.group(5))
            action.welfare = float(match.group(6))
        
        self.run.add_action(action)

    def try_priority_action(self, line):
        match = self.priority_action_re.match(line)
        if match != None:
            self.create_priority_action(match)
            return True
        return False

    def create_priority_action(self, match):
        action = PriorityAction()
        action.real_time = float(match.group(1))
        action.virtual_time = self.parse_time(match.group(2))
        action.ship_id = int(match.group(3))
        action.priority = int(match.group(4))
        self.run.add_action(action)

    def try_cleaning_action(self, line):
        match = self.cleaning_action_re.match(line)
        if match != None:
            self.create_cleaning_action(match)
            return True
        return False

    def create_cleaning_action(self, match):
        action = CleaningAction()
        action.real_time = float(match.group(1))
        action.virtual_time = self.parse_time(match.group(2))
        action.solution = match.group(3)
        self.run.add_action(action)
