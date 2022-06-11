# s = "abBAcC"
# i = 0
# while i < len(s)-1:
#     if ((s[i].islower() and s[i+1].isupper()) or (s[i].isupper() and s[i+1].islower())) and s[i].lower()==s[i+1].lower():
#         s = s.replace(s[i]+s[i+1],'',1)
#         i = -1
#     i += 1
# print(s)

from queue import PriorityQueue
q = PriorityQueue()

def findRelativeRanks(score: list):

    rank = ["Gold Medal","Silver Medal","Bronze Medal","",""]

    for i in range(len(score)):
        q.put(score[i])

    score_queue = []
    for i in range(len(score)):
        score_queue.append(q.get())
    score_queue = score_queue[::-1]

    dictionary = {}
    answer = []

    for i, j in zip(score_queue, rank):
        dictionary[i] = j

    for i in score:
        i = dictionary[i]
        answer.append(i)

    print(answer)

findRelativeRanks([10,3,8,9,4])
# score = [10,3,8,9,4]
# ranks = ["Gold Medal","Silver Medal","Bronze Medal"] 
# for i in range(4, len(score)+1):
#     ranks.append(str(i))
# dic, ans = {}, []
# for i, j in zip(sorted(score, reverse=True), ranks):
#     dic[i] = j
# ans = [dic[i] for i in score]
# print(ans)