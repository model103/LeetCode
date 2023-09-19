from collections import defaultdict
import math

def get_tfidf(d, w, t, articles):
    tf_dict = defaultdict(int)
    inf_list = []
    for i in range(d):
        inf_list.append(set())
        for word in articles[i]:
            tf_dict[word] += 1
            inf_list[i].add(word)

    res = 0
    for word, fre in tf_dict.items():
        tf = fre / (d * w)
        j = 0
        for a_set in inf_list:
            if word in a_set:
                j += 1
        if tf * math.log(d / (j + 1)) > t:
            res = 1
            break
    return res


n = int(input())
output = []
for i in range(n):
    d, w, t = map(float, input().split(' '))
    articles = []
    d = int(d)
    for _ in range(d):
        articles.append(input().split(' '))
    output.append(get_tfidf(d, w, t, articles))
for o in output:
    print(o)
