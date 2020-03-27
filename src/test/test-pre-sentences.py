import MySQLdb
from pyhanlp import *

nr_segment = HanLP.newSegment()


def load_sentences():
    db = MySQLdb.connect("127.0.0.1", 'root', '123456', 'ncp', charset='utf8')
    cursor = db.cursor()
    sql = 'select * from pre_context limit 1'
    cursor.execute(sql)
    sentences = cursor.fetchall()
    for docid, text, question, answer, person, organization, date_time, location, value in sentences:
        nrs = nr_recognition(text)
        nrs = statis(nrs)
        print(nrs)
    db.close()


def statis(nrs):
    nr_statis = {}
    for nr in nrs:
        word = nr['word']
        last_dic = nr['last']
        next_dic = nr['next']

        if len(last_dic) > 0:
            last_word = last_dic['word']
        if len(next_dic) > 0:
            next_word = next_dic['word']
        temp = nr_statis.get(word)
        if temp is None:
            temp = nr
            temp['count'] = 1
        else:
            temp['count'] += 1
        nr_statis[word] = temp
    return nr_statis


def nr_recognition(sentence):
    index = 0
    nrs = []
    term_list = nr_segment.seg(sentence)

    for i in range(len(term_list)):
        term = term_list[i]
        word = term.word
        nature = str(term.nature)
        last_word = {}
        next_word = {}
        if i > 0:
            last_term = term_list[i - 1]
            last_word = {'word': last_term.word, 'nature': str(last_term.nature)}
        if i < len(term_list) - 1:
            next_term = term_list[i + 1]
            next_word = {'word': next_term.word, 'nature': str(next_term.nature)}
        # temp = nrs.get(word)
        temp = {'word': word, 'nature': nature, 'last': last_word, 'next': next_word}
        # if temp is None:
        # else:
        #     temp['count'] += 1
        index += len(word)

        nrs.append(temp)
        # # 人名
        # if str(term.nature).startswith('nr'):
        #     persons.append(temp)
        # # 地名
        # elif str(term.nature).startswith('ns'):
        #     places.append(temp)
        # # 机构团体名
        # elif str(term.nature).startswith('nt') or str(term.nature).startswith('ni'):
        #     organizations.append(temp)

    return nrs


if __name__ == '__main__':
    load_sentences()
