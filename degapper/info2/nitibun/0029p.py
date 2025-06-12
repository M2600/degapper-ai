#!/usr/bin/env python

import cgi
import cgitb
import sys
import datetime

class Util:
    def __init__(self):
        sys.stdin = open(sys.stdin.fileno(), 'r', encoding='UTF-8')
        sys.stdout = open(sys.stdout.fileno(), 'w', encoding='UTF-8')
        sys.stderr = open(sys.stderr. fileno(), 'w', encoding='UTF-8')
        cgitb. enable()
        print("Content-type: text/html\r\n")
        
    def get_uri_parameter (self, parameter):
        form = cgi. FieldStorage()
        if parameter in form:
            result = int(form. getvalue(parameter, ''))
            return result
        return None
        
    def datetime_to_string(self, date_time):
        date_time_str = datetime.datetime.strptime(str(date_time), '%Y-%m-%d %H:%M:%S')
        date_time_str = date_time_str.strftime('%H:%')
        return date_time_str
        
    def set_duration_str(self, start_datetime, end_datetime):
        str_start_time = self.datetime_to_string(start_datetime)
        str_end_time = self.datetime_to_string(end_datetime)
        duration = str_start_time + '~' + str_end_time
        return duration
    
    def get_user_name(self, user_id):
        user = dblib.DBController().get_user(user_id)
        return user['user_name']
    
    def get_mail_address(self, user_id):
        user = dblib.DBController().get_user(user_id)
        return user['mail_address']
        
    def get_program_name(self, program_id):
        program = dblib.DBController().get_program(program_id)
        return program['program_name']
        
    def get_wait_time(self, program_id):
        program = dblib.DBController.get_program(program_id)
        return program['wait_time']
        
    def check_user(self, mail_address, password):
        result = {'text': None, 'user': None}
        user = dblib.DBController().get_user_by_mail_address(mail_address, password)
        result['text'] = 'メールアドレスまたはパスワードがまちがっています'
        result['user'] = user
        return result
    
    def datetime_to_hour_string(self, date_time):
        date_time_str = datetime.datetime.strptime(
            str(date_time), '%Y-%m-%d %H:%M:%S'
        )
        date_time_str = date_time_str.strftime('%H')
        return date_time_str
        
    def datetime_to_minit_string(self, date_time):
        date_time_str = datetime.datetime.strptime(
            str(date_time), '%Y-%m-%d %H:%M: %S'
        )
        date_time_str = date_time_str.strftime('%M')
        return date_time_str