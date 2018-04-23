class NFA:
    def __init__(s,current_states,accept_states,rulebook):
        s.current_states=current_states
        s.accept_states=accept_states
        s.rulebook=rulebook
        s.add_empty_passes()
    def add_empty_passes(s):
        emptystates=s.rulebook.follow_free_moves(s.current_states)
        s.current_states=s.current_states | emptystates

    def is_accepting(s):
        return len(s.current_states.intersection(s.accept_states))>0
    def read_char(s,char):
        s.current_states=s.rulebook.next_states(s.current_states,char)
        s.add_empty_passes()
    def read_string(s,str):
        for char in str:
            s.read_char(char)

class NFADesign(object):
	def __init__(s,start_states,accept_states,rulebook):
		s.start_states=start_states
		s.accept_states=accept_states
		s.rulebook=rulebook
	def to_nfa(s):
		return NFA(set(s.start_states),set(s.accept_states),s.rulebook)
	def is_accept(s,str):
		nfa=s.to_nfa()
		nfa.read_string(str)
		return nfa.is_accepting()
        
