class NFA:
    def __init__(self, states, alphabet, transitions, initial_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions  # {(state, symbol): {next_states}}
        self.initial_state = initial_state
        self.accept_states = accept_states

    def accepts(self, input_string):
        """
        Check if the NFA accepts the input string.
        """
        # Start with a set containing the initial state
        current_states = {self.initial_state}
        
        for symbol in input_string:
            next_states = set()
            for state in current_states:
                # Get the next states for (state, symbol), if any
                if (state, symbol) in self.transitions:
                    next_states |= self.transitions[(state, symbol)]
            current_states = next_states
        
        # Check if any of the current states is an accept state
        return any(state in self.accept_states for state in current_states)

# Example usage
states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'qf'}
alphabet = {':','/','S','h','u','p','c','q','f','#','@','?'}
transitions = {
    ('q0','S'):{'q1'},
    ('q1',':'):{'q2','q9'},
    ('q2','/'):{'q3'},
    ('q3','/'):{'q4','q6'},
    ('q4','u'):{'q5'},
    ('q5','@'):{'q6'},
    ('q6','h'):{'q7', 'q9'},
    ('q7',':'):{'q8'},
    ('q8','p'):{'q9'},
    ('q9','c'):{'q10','qf'},
    ('q10','?'):{'q11'},
    ('q10',"#"):{"q14"},
    ('q11','q'):{'q12', 'qf'},
    ('q12',"#"):{"q13"},
    ('q13','f'):{"qf"},
    ('q14','f'):{"qf"},
}
initial_state = 'q0'
accept_states = {'qf'}

nfa = NFA(states, alphabet, transitions, initial_state, accept_states)

# Test the NFA with some input strings
print(nfa.accepts("S:c"))  # True
print(nfa.accepts("S://u@h:pc?q#f"))  # True
print(nfa.accepts("S://u@h:p"))  # False