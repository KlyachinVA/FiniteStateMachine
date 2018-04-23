class DFA(object):
	def __init__(s,cur_state,accept_states,rulebook):
		s.cur_state=cur_state
		s.accept_states=accept_states
		s.rulebook=rulebook
	def is_finish(s):
		return s.cur_state in s.accept_states
	def read_char(s,ch):
		s.cur_state=s.rulebook.next_state(s.cur_state,ch)
	def read_str(s,str):
		for ch in str:
			s.read_char(ch)
class DFADesign(object):
	def __init__(s,start_state,accept_states,rulebook):
		s.start_state=start_state
		s.accept_states=accept_states
		s.rulebook=rulebook
	def to_dfa(s):
		return DFA(s.start_state,s.accept_states,s.rulebook)
	def is_accept(s,str):
		dfa=s.to_dfa()
		dfa.read_str(str)
		return dfa.is_finish()
	
