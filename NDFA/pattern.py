from nfa import NFADesign
from nfarule import NFARuleBook,NFARule

class Pattern(object):
    def matches(s,str):
        return s.to_nfa_design().is_accept(str)
class Empty(Pattern):
    def __init__(s):
        pass
    def to_nfa_design(s):
        start_state = object()
        accept_states = [start_state]
        rulebook= NFARuleBook([])
        return NFADesign([start_state],accept_states,rulebook)

class Literal(Pattern):
    def __init__(s,char): s.char=char
    def to_nfa_design(s):
        start_state = object()
        accept_state = object()
        rule=NFARule(start_state,s.char,accept_state)
        rulebook= NFARuleBook([rule])
        return NFADesign([start_state],[accept_state],rulebook)
class Concatenate(Pattern):
    def __init__(s,first,second):
        s.first=first
        s.second=second
    def to_nfa_design(s):
        first_nfa= s.first.to_nfa_design()
        second_nfa=s.second.to_nfa_design()
        v=second_nfa.start_states[0]
        
        start_states=first_nfa.start_states
        accept_states=second_nfa.accept_states
        rules=first_nfa.rulebook.rules + second_nfa.rulebook.rules 	
        extra_rules = map(lambda state: NFARule(state,'',v) , first_nfa.accept_states)		
        rulebook= NFARuleBook(rules + extra_rules)
        return NFADesign(start_states,accept_states,rulebook)
		
class Choose(Pattern):
    def __init__(s,first,second):
        s.first=first
        s.second=second
    def to_nfa_design(s):
        first_nfa= s.first.to_nfa_design()
        second_nfa=s.second.to_nfa_design()
        start_state=object()
        accept_states = first_nfa.accept_states + second_nfa.accept_states
        rules=first_nfa.rulebook.rules + second_nfa.rulebook.rules
        v1=first_nfa.start_states[0]
        
        v2=second_nfa.start_states[0]
        
        extra_rules=[NFARule(start_state,'',v1) , NFARule(start_state,'',v2)]
        rulebook= NFARuleBook(rules + extra_rules)
        
        return NFADesign([start_state],accept_states,rulebook)

class Repeat(Pattern):
    def __init__(s,pattern):
        s.pattern=pattern
    def to_nfa_design(s):
        nfa=s.pattern.to_nfa_design()
        start_state=object()
        v=nfa.start_states[0]
        accept_states = nfa.accept_states + [v]
        #print "rr",start_state, accept_states
        rules=nfa.rulebook.rules	
        
        
        extra_rules=map(lambda acstate: NFARule(acstate,'',v),nfa.accept_states )+[NFARule(start_state,'',v)]
        rulebook= NFARuleBook(rules + extra_rules)
        
        return NFADesign([start_state],accept_states,rulebook)
		
		
print Choose(Literal('a'),Literal('b')).matches('c')
nfa=Concatenate(Literal('a'),Choose(Empty(),Literal('b'))).to_nfa_design()

pattern=Repeat(Concatenate(Literal('a'),Choose(Literal('a'),Literal('b'))))
#pattern=Repeat(Literal('a'))
print pattern.matches('ababaa')