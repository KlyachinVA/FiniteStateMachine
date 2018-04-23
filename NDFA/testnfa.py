from nfa import NFA,NFADesign
from nfarule import NFARule,NFARuleBook

r1=NFARule(1,'a',1)
r2=NFARule(1,'b',1)
r3=NFARule(1,'b',2)
r4=NFARule(2,'a',3)
r5=NFARule(3,'a',4)
r6=NFARule(2,'b',3)
r7=NFARule(3,'b',4)
r8=NFARule(2,'',4)

text="b"
rulebook = NFARuleBook([r3,r4,r5,r6,r7,r8])
nfa=NFA(set([1]),set([4]),rulebook)
nfades=NFADesign([1],[4],rulebook)
nfa.read_string(text)

print nfa.is_accepting()
print nfades.is_accept(text)