from pyhanlp import *
if __name__ == '__main__':
    segment = HanLP.newSegment()
    sentences = [
        "北川景子参演了林诣彬导演的《速度与激情3》",
        "林志玲亮相网友:确定不是波多野结衣？",
        "龟山千广和近藤公园在龟山公园里喝酒赏花",
    ]
    for sentence in sentences:
        term_list=segment.seg(sentence)
        print(term_list)
        print([i.word for i in term_list])
        for i in term_list:
            print(i)
            print(i.word)
            print(i.offset)
            print(i.nature)
            print(len(i.word))