#coding:utf-8

m1 = {
    'A':{
        '1':['A'],
        '0':['B']
    },
    'B':{
        '1':['C'],
        '0':['B']
    },
    'C':{
        '1':['C'],
        '0':['C']
    }
}

m2 = {
    'D':{
        '1':['E'],
        '0':['D']
    },
    'E':{
        '1':['D'],
        '0':['E']
    },
}

# print(m2.pop('D'))

transitions = {}

for keys_1 in m1:
    for keys_2 in m2:
        new_state = keys_1+keys_2
        transitions[new_state] = {
            '1':[m1[keys_1]['1'][0]+ m2[keys_2]['1'][0]],
            '0':[m1[keys_1]['0'][0]+ m2[keys_2]['0'][0]]
        }
        # print(transitions)

print(transitions)