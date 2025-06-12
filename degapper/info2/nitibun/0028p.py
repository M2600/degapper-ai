#!/usr/bin/env python

import MySQLdb
import MySQLinfo

class DBController:
    def _init_(self):
        self.conn = MySQLdb.connect(
            user=MySQLinfo.mysql_info['user'],
            passwd=MySQLinfo.mysql_info['passwd'],
            host=MySQLinfo.mysql_info['host'],
            db=MySQLinfo.mysql_info['db'],
        )
        # Encoding
        self.conn.set_character_set('utf8')
        self.cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
        
    def get_floor (self):
        sql = "select * from mst_floor"
        self.cur.execute(sql)
        return self.cur.fetchall()
        
    def get_event(self):
        sql = "select + from mst_event where start_datetime < now() and end_datetime > now()"
        self.cur .execute(sql)
        return self.cur.fetchone()
        
    def get_program_list(self, floor_id):
        sql = "select * from mst_program where floor_id = " + str(floor_id)
        self.cur.execute(sql)
        return self.cur.fetchall()
    def get_program(self, program_id):
        sql = "select * from mst_program where program_id = " + str(program_id)
        self.cur.execute(sql)
        return self.cur.fetchone()
    
    def get_program_detail_list(self, progran_id):
        sql = "select + from mst_program_detail where program_id = " + str(program_id)
        self.cur.execute(sql)
        return self.cur.fetchall()
        
    def get_program_detail(self, detail_id):
        sql = "select * from mst_program_detail where detail_id = " + str(detail_id)
        self.cur.execute(sql)
        return self.cur.fetchone()
        
    def get_user (self, user_id):
        sql = "select + from user where user_id = " + str(user_id)
        self.cur.execute(sql)
        return self.cur.fetchone()
        
    def get_user_by_mail_address(self, mail_address, password):
        sql = "select * from user where mail_address='{0}' and password='{1}'".format(str(mail_address), str(password))
        self.cur.execute(sql)
        return self.cur.fetchone()
        
    def get_user_by_mail_address_only(self, mail_address):
        sql = "select * from user where mail_address='{0}".format(str(mail_address))
        self.cur.execute(sql)
        return self.cur.fetchone()
        
    def get_program_list_by_user_id(self, user_id):
        sql = "select * from mst_program where admin_user_id = " + str(user_id)
        self.cur.execute(sql)
        return self.cur.fetchall()
        
    def update_wait_time(self, program_id, wait_time):
        sql = "update mst_program set update_datetime=now(), wait_time='{0}' where program_id='{1}'".format(str(wait_time), str(program_id))
        self.cur.execute(sql)
        self.conn.commit()