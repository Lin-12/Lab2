from shunting_yard import convert, metachar
from thompsons import run_thompson


def reg_match(infix, string, case_insens=False):
    if case_insens:
        infix = infix.lower()
        string = string.lower()
    infix = check_concat(infix)
    postfix = convert(infix)
    nfa = run_thompson(postfix)

    cur_states, nxt_states = set(), set()

    cur_states |= current_states(nfa.initial_state)

    for character in string:
        for state in cur_states:
            if state.label == character:
                nxt_states |= current_states(state.edge_1)  # add the edge's state to the next set of states

        cur_states, nxt_states = nxt_states, set()  # set current set of states to the next state of states

    return nfa.accept_state in cur_states  # returns true if there is an accept state at the end of matching


def current_states(state):
    state_set = set()
    state_set.add(state)

    if state.label is None:  # empty state, follow edge and add to set
        if state.edge_1 is not None:
            state_set |= current_states(state.edge_1)
        if state.edge_2 is not None:
            state_set |= current_states(state.edge_2)

    return state_set


def check_concat(infix):
    new_infix = ""
    operators = {**metachar, '(': 60, ')': 60}
    index = 0

    for c in infix:
        if index + 1 != len(infix):  # if c is not last character
            if c not in operators and infix[index + 1] not in operators:  # if both character are not operators
                new_infix += c + '.'
            else:
                new_infix += c
        else:
            new_infix += c

        index += 1

    return new_infix