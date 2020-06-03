import nfa
from nfa import log_nfa

class Regex(object):
    def __init__(self, input_string, pattern_string):
        self.input_string = input_string
        self.pattern_string = pattern_string
        self.graph = None

    def match(self):
        pattern_string = self.pattern_string
        input_string = self.input_string
        nfa_machine = nfa.pattern(pattern_string)
        self.graph = log_nfa(nfa_machine)
        return nfa.match(input_string, nfa_machine)

    def match_All(self):
        ins = self.input_string
        for i in range(len(self.input_string)):
            result = self.match()
            if result:
                break
            self.input_string = self.input_string[1:]
        # if match failure ,return error
        if len(result)==0:
            return "ERROR"
        return "".join(result)



