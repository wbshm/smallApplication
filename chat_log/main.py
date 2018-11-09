import re

import jieba.analyse
from wordcloud import WordCloud

# import matplotlib


if __name__ == '__main__':
    # print("answer:"+",".join(result))

    fileName = 'yanglinde'
    fileName = 'dingyong'
    # f=open("./lvyou.txt","rb")
    f = open("./log/%s.txt" % fileName, "r", encoding='utf-8')
    filter = re.sub('\n(19|20)[0-9]{2}-[0|1][0-9]-[0-3]?[0-9] (.*)?\n', '', f.read())

    tags = jieba.analyse.extract_tags(sentence=filter.replace('\n', ''), topK=500, withWeight=True)
    print(tags)
    amoy = WordCloud(
        background_color="white",  # 背景颜色
        max_words=500,  # 显示最大词数
        font_path="C:/Windows/Fonts/STHUPO.TTF",  # 使用字体
        # min_font_size=4,
        # max_font_size=15,
        width=800,  # 图幅宽度
        height=600
    )
    amoy.generate_from_frequencies(dict(tags))
    amoy.to_file("./wordCloud/%s.png" % fileName)
    exit(1)
