import sys
import re

# f=open("ex.txt", "r")

# contents = f.readlines()

states = initial = final = ""


def fileParser(fileName):
    f = open(fileName, "r")
    file_content = f.readlines()

    states = final = []
    initial = ""
    transitions = {}

    for line in file_content:
        line = line.replace(",", "")
        splitted = line.split()

        if line.startswith("estados"):
            states = splitted[1:]
            
        elif line.startswith("inicial"):
            initial = splitted[1]

        elif line.startswith("aceita"):
            final = splitted[1:]

        elif len(splitted) == 3 and splitted[0] in states and splitted[1] in states:
            current_state, target_state, next_state = splitted

            if current_state not in transitions:
                transitions[current_state] = {}

            if next_state not in transitions[current_state]:
                transitions[current_state][next_state] = []

            transitions[current_state][next_state].append(target_state)
    
    return (states, initial, final, transitions)


def wordParser(states, initial, final, transitions, word):
    currentStates = [initial]
    newCurrentStates = []
    accepted = "não "

    print("{} {: >20}".format("Estados", "Palavra"))

    for index in range(len(word)):
        for currentState in currentStates:
            newCurrentStates.append(transitions[currentState][word[index]][0])

        print("{} {: >20}".format(currentStates, word[index:]))

        currentStates = newCurrentStates
        newCurrentStates = []

    for states in currentStates:
        if states in final and accepted != "":
            accepted = ""

    return "\nA palavra {}foi aceita".format(accepted)


states, initial, final, transitions = fileParser(sys.argv[1])

word = sys.argv[2]

print("States: ", states)
print("Initial: ", initial)
print("Final: ", final)
print("Transition: ", transitions)


print(wordParser(states, initial, final, transitions, word))
