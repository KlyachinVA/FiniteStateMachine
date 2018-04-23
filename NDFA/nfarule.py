class NFARule(object):
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
	
class NFARuleBook:
    def __init__(s,rules):
        s.rules=rules
    def next_states(s,states,char):
        newstates=set()
        for state in states:
            s.rules_for(state,char,newstates)
        return newstates
    
		
    def rules_for(s,state,char,nstates):
	    
        for rule in s.rules:
            if(rule.is_applies(state,char)):
                nstates.add(rule.follow())
 
    def follow_free_moves(s,states):
        more_states=s.next_states(states,'')
        f=True
        for st in more_states:
            flag=False
            for sts in states:
                if st == sts: 
                    flag=True
            if flag == False: 
                f=False
                break
        if f: return states
        else:
            return s.follow_free_moves(states|more_states)
 