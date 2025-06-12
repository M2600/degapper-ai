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
        