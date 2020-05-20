class State:
    label = None
    edge_1 = None
    edge_2 = None


class NFA:
    initial_state = None
    accept_state = None

    def __init__(self, initial_state, accept_state):
        self.initial_state = initial_state
        self.accept_state = accept_state


def run_thompson(postfix):
    nfa_stack = []

    for c in postfix:
        if c == '.':
            nfa_2, nfa_1 = nfa_stack.pop(), nfa_stack.pop()
            nfa_1.accept_state.edge_1 = nfa_2.initial_state
            nfa_stack.append(NFA(nfa_1.initial_state, nfa_2.accept_state))
        elif c == '|':
            nfa_2, nfa_1 = nfa_stack.pop(), nfa_stack.pop()
            new_initial_state = State()
            new_initial_state.edge_1, new_initial_state.edge_2 = nfa_1.initial_state, nfa_2.initial_state
            new_accept_state = State()
            nfa_1.accept_state.edge_1, nfa_2.accept_state.edge_1 = new_accept_state, new_accept_state
            nfa_stack.append(NFA(new_initial_state, new_accept_state))
        elif c == '*':
            nfa = nfa_stack.pop()
            new_initial_state, new_accept_state = State(), State()
            new_initial_state.edge_1,  new_initial_state.edge_2 = nfa.initial_state, new_accept_state
            nfa.accept_state.edge_1,  nfa.accept_state.edge_2 = new_accept_state, nfa.initial_state
            nfa_stack.append(NFA(new_initial_state, new_accept_state))
        elif c == '+':
            nfa = nfa_stack.pop()
            new_initial_state, new_accept_state = State(), State()
            new_initial_state.edge_1 = nfa.initial_state
            nfa.accept_state.edge_1, nfa.accept_state.edge_2 = new_accept_state, nfa.initial_state
            nfa_stack.append(NFA(new_initial_state, new_accept_state))
        else:
            initial_state, accept_state = State(), State()
            initial_state.label,  initial_state.edge_1 = c, accept_state
            nfa_stack.append(NFA(initial_state, accept_state))
    return nfa_stack.pop()