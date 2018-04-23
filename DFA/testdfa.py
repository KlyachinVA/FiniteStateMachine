from farule import DFARulebook, FARule
from dfa import DFA,DFADesign


rulebook=DFARulebook([
FARule(1,'a',2),FARule(1,'b',1),
FARule(2,'a',2),FARule(2,'b',3),
FARule(3,'a',3),FARule(3,'b',3)])

print rulebook.next_state(1,'a')
print rulebook.next_state(1,'b')
print rulebook.next_state(2,'b')

dfa=DFA(1,[3],rulebook)

dfa.read_str("bba")
print dfa.is_finish()

dfad=DFADesign(1,[3],rulebook)
print dfad.is_accept("a")
print dfad.is_accept("baa")
print dfad.is_accept("baba")

