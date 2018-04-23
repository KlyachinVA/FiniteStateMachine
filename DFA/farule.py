class FARule(object):
	def __init__(s,state,char,next_state):
		s.state=state
		s.char=char
		s.next_state=next_state
	def is_applies(s,state,char):
		return s.state==state and s.char==char
	def follow(s):
		return s.next_state
	def __str__(s):
		return str(s.state)+"--"+s.char+"-->"+str(s.next_state)
	
class DFARulebook(object):
	def __init__(s,rules):
		s.rules=rules
	def next_state(s,state,char):
		for rule in s.rules:
			if rule.is_applies(state,char):
				return rule.follow()
				