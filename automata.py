import re
#EU QUE FIZ NA AULA DE REDES :D
def automataParser(states, initial, final, word, autamataDescription):
    print(initial)
    print(final)
    print(word)

    current = (initial)
    result  = ""
    
    for l in word:
        

        print(autamataDescription[current][int(l)])
        current = autamataDescription[current][int(l)]
        
        print("l: ", l)
        print("Current: ",current)

    if current == final:
        result = ""
    else:
        result = "não"

    return result



states     = ("a", "b", "c")
initial    = "a"
final      = "b"
transition = ""
origin     = ""
destination= ""
value      = ""

#autamataDescription = {'a': ['b', 'a'], 'b': ['a', 'b']}
autamataDescription = {'a': ['a', 'b', 'c'], 'b': ['b', 'a', 'b'], 'c': ['c', 'c', 'a']}
#autamataDescription = {}



inp = input()

while inp:
    if inp.startswith("estados"):
        states = (re.split("(\W+(\,)?)", inp)[-4], re.split("(\W+(\,)?)", inp)[-1])
    elif inp.startswith("inicial"):
        initial = inp.split()[1]
    elif inp.startswith("aceita"):
        final   = inp.split()[1]

    else:
        [origin, destination, value] = inp.split()
        value = int(value)

        if origin not in autamataDescription:
            autamataDescription[origin] = []
        autamataDescription[origin].insert(value, destination)
        


    print("States: ", states)
    print("Initial: ", initial)
    print("States: ", final)

    print("Origin: ", origin)
    print("Destination: ", destination)
    print("Value: ", value)

    print(autamataDescription)

    inp = input()

word = str(input())
print ("A palavra %s aceita" % automataParser(states, initial, final, word, autamataDescription))