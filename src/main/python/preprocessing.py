#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb
from pyhanlp import *

if __name__ == '__main__':
    segment = HanLP.newSegment()
    db = MySQLdb.connect("127.0.0.1", 'root', '123456', 'ncp', charset='utf8')
    cursor = db.cursor()
    sql = 'select * from pre_context limit 1,1'
    cursor.execute(sql)
    results = cursor.fetchall()
    print('Error: unable to fetch data')


    for docid, text, question, answer, person, organization, date_time, location, value in results:
        term_list = segment.seg(text)
        for term in term_list:
            if term.nature == 'ns':
                print(term.word)
            if term.nature == '':
                print(term.word)
            # print(word.word)
            # print(word.nature)
            # print(len(word.word))