#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def topic_union(mema,memb):
    sub_count = 0
    for i in range(len(mema)):
        if mema[i] == '1' or memb[i] == '1':
            sub_count += 1
    return sub_count
    

def acmTeam(topic):
    # Write your code here
    # members = dict()
    # mem_idx = 0
    # for mem in topic:
    #     members[mem_idx] = [i for i in range(len(mem)) if int(mem[i]) == 1]
    #     mem_idx+=1
    # teams = dict()
    # for j in members.keys():
    #     for k in members.keys():
    #         if j!=k and tuple(set([j,k])) not in teams:
    #             teams[tuple(set([j,k]))] = list(set(members[j]+members[k]))
    # max_key, max_topics = max(teams.items(), key = lambda x: len(set(x[1])))
    # team_count =0 
    # for k,v in teams.items():
    #     if v == max_topics:
    #         team_count += 1
    # return len(max_topics), team_count
    
    knowledge = []
    for i in range(len(topic)):
        for j in range(i+1,len(topic)):
            knowledge.append(topic_union(topic[i], topic[j]))
    max_topics_known = max(knowledge)
    op_teams = len([x for x in knowledge if x == max_topics_known])
    return max_topics_known, op_teams
        
        
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
