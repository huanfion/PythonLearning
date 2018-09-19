# encoding=utf-8
import jieba
import jieba.posseg as psg
str1='这只皮靴号码大了。那只号码合适'
str2='这只皮靴号码不小，那只更合适'
str='''9月11日深夜0时许，一位滴滴员工疲惫地走出位于北京数字山谷的滴滴大厦，和往常一样他掏出手机准备叫一辆礼橙专车，然而页面出现了异样的橘黄色提示——我们将暂停9月8日至14日深夜的出行服务，“带来不便敬请谅解”。他这时才想起来，高管们在一周前已经下达指令，要暂停这一周23时至次日5时的所有出行服务。
而在距离滴滴大厦35公里之外，首都国际机场T2航站楼外面仍有密集的人流。等出租车的人排成了几百米，候车区的两拨队伍来回折了5道，场外长龙般的队伍还在等待进入。“（候车区）接近200人吧，等到出租差不多要一个小时。”一位引导员说，“不能打滴滴了，大家排队等出租。”乘客嘟囔着：“我一直都用滴滴啊，怎么不能用了？”
这是滴滴进行深夜整改的第3天，乐清事件——一位浙江乐清的女生被滴滴顺风车司机奸杀之后，这家在中国网约车市场占据垄断地位的公司正遭遇成立以来最猛烈的抨击。在进行人事处罚、高层联名道歉和再三重申整改决心之后，滴滴做出了一个令人有些意外的举动：暂停为期一周的夜间出行服务。
每天6小时、连续7天，滴滴在这42小时内不由分说突然抽离。2017年底，滴滴曾公布其日单量已破2500万单，每日停摆6小时，相当于会损失625万单/日（当然夜间单量实际比白天要少），7天合计4375万单。以20元客单价计算，滴滴在42小时内将折损8.7亿元人民币的收入。“这是（滴滴）一个暂时的牺牲。”一位接近滴滴的人士对《财经》记者说，也是滴滴试图掌握主动权的开始。
在网约车行业市占率超过90%的滴滴，它在深夜突然消失就像气囊一下被抽走了大部分空气，剩余的部分迅速变形。42小时背后，看似静谧的黑夜之下涌动着各方博弈，网约车平台、政府、资本、出租车司机、私家车司机、乘客一齐涌入，这是混乱与规范、退让与进击角力的42小时。
一边是增长需求的迫切，一边是平台治理的高压线；前者来自于股东压力，后者是政府监管机构和公众的忍耐底线。手握5.5亿用户的滴滴出行正处在两者的交汇点，也处在自己命运的转折点。'''

# s1_seg='/'.join([x for x in jieba.cut(str1,cut_all=True) if x!=""])
s1_lst=[ x for x in jieba.cut(str1,cut_all=True) if x!=""]
s1_set=set([x for x in jieba.cut(str1,cut_all=True) if x!=''])

# s2_seg='/'.join([x for x in jieba.cut(str2,cut_all=True) if x!=""])
s2_set=set([x for x in jieba.cut(str2,cut_all=True) if x!=''])
s2_lst=[x for x in jieba.cut(str2,cut_all=True) if x!='']

allword_dict=dict()
i=0
for word in s1_set.union(s2_set):
    allword_dict[word]=i
    i+=1
print(allword_dict)
def word_to_vector(word_dict,s_lst):
    s_vector=[0]*len(word_dict)
    word_count=dict()
    for word in s_lst:
        if word_count.get(word)==None:
            word_count[word]=1
        else:
            word_count[word]+=1
    for word,freq in word_count.items():
        wid=word_dict[word]
        s_vector[wid]=freq
    return s_vector
s1_vector=word_to_vector(allword_dict,s1_lst)
s2_vector=word_to_vector(allword_dict,s2_lst)
print(s1_vector)
print(s2_vector)
# s = u'我想和女朋友一起去北京故宫博物院参观和闲逛。'
# cut=jieba.cut(s)
# cut1=jieba.cut(s,cut_all=True)
# print('/'.join(jieba.cut_for_search(s)))
# print("词性")
# print([(x.word,x.flag) for x in psg.cut(s)])
# print (','.join(cut))
# print('/'.join(cut1))



