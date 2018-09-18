#encoding=utf-8
import os


import jieba
s="欧几里得度量（也称欧氏距离）是一个通常采用的距离定义，指在m维空间中两个点之间的真实距离，或者向量的自然长度（即该点到原点的距离）。在二维和三维空间中的欧氏距离就是两点之间的实际距离。"
s1 = "这只皮靴号码大了。那只号码合适"
s2 = "这只皮靴号码不小，那只更合适"
#s1_seg='/'.join([x for x in jieba.cut(s1,cut_all=True) if x!=''])
s1_lst=[x for x in jieba.cut(s1,cut_all=True) if x!='']
s1_set=set(s1_lst)


#s2_seg='/'.join([x for x in jieba.cut(s2,cut_all=True) if x!=''])
s2_lst=[x for x in jieba.cut(s2,cut_all=True) if x!='']
s2_set=set(s2_lst)
print(s1_lst)
print(s2_lst)
# print("词集合：")
# print(s1_set.union(s2_set))
word_dict=dict()
i=0
for word in s1_set.union(s2_set):
    word_dict[word]=i
    i+=1
print(word_dict)
def word_to_vec(word_dict,s1_lst):
    s1_vector=[0]*word_dict.__len__()
    word_count1 = dict()
    for word in s1_lst:
        if word_count1.get(word) == None:
            word_count1[word] = 1
        else:
            word_count1[word] += 1
    for word,freq in word_count1.items():
        wid=word_dict[word]
        s1_vector[wid]=freq
    return  s1_vector
s1_vector=word_to_vec(word_dict,s1_lst)
print(s1_vector)
s2_vector=word_to_vec(word_dict,s2_lst)
print(s2_vector)