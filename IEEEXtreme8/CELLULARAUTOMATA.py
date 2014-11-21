import sys

#inp = sys.stdin.read()


def make_dict(rule):
    ruledict = {}
    rulebinit = iter(('{:08b}'.format(int(rule))))
    for left in (True, False):
        for middle in (True, False):
            for right in (True, False):
                ruledict[(left, middle, right)] = bool(int(next(rulebinit)))
    return ruledict

def convert_states(decstate, cell_amount):
    return [bool(int(x)) for x in ('{:0'+ str(cell_amount) + 'b}').format(decstate)]

def previous_states(states, index):
    prev_states = []
    for i in (-1,0,1):
        if index+i < 0 or index+i >= len(states):
            prev_states.append(False)
        else:
            prev_states.append(states[index+i])
    return prev_states

def run_auto(ruledict, iter_amount, cell_amount, start_states):
    states_states = []
    prev_states = convert_states(start_states, cell_amount)
    states_states.append(prev_states)
    for i in range(0, iter_amount-1):
        next_states = []
        for index, cell in enumerate(prev_states):
            left, middle, right = previous_states(prev_states, index)
            #if index == 0:
                #print('{0}, {1}, {2} -> {3}'.format(left, middle, right, ruledict[(left,middle,right)]))
            next_cur_state = ruledict[(left, middle, right)]
            next_states.append(next_cur_state)
        if next_states == states_states[-1]:
            #print(next_states, states_states) #REMOVE THIS LATER PLS
            states_states.append(next_states)
            break
        states_states.append(next_states)
        prev_states = next_states
    return states_states

def leftify_string(numb):
    numb = str(numb)
    amount_of_spaces = 4 - len(numb)
    return numb + amount_of_spaces*' '

def print_auto(states_states):
    for index, states in enumerate(states_states):
        state_string = ''.join(['*' if state == True else ' ' for state in states])
        if index < (len(states_states) - 1):
            print('{0}-{1}-'.format(leftify_string(index+1), state_string))
        else:
            print('{0}-{1}-\n'.format(leftify_string(index+1), state_string))


def main():
    #inp = "30 20 8 16"
    inp = "0 20 8 10"
    rule, iter_amount, cell_amount, start_states = (int(x) for x in inp.split())
    ruledict = make_dict(rule)
    states_states = run_auto(ruledict, iter_amount, cell_amount, start_states)
    #print(states_states)
    print_auto(states_states)
    #print(ruledict)
    #return ruledict

main()
