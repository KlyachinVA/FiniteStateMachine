from nfa import NFA,NFADesign
from nfarule import NFARule,NFARuleBook

r1=NFARule(1,'a',2)
r2=NFARule(1,'',3)
r3=NFARule(2,'b',4)
r4=NFARule(2,'',5)
r5=NFARule(3,'b',4)
r6=NFARule(4,'b',5)
r7=NFARule(3,'b',4)
r8=NFARule(2,'',4)

text="aab"
rulebook = NFARuleBook([r1,r2,r3,r4,r5,r6])
#nfa=NFA(set([1]),set([4]),rulebook)
nfades=NFADesign([1],[5],rulebook)
#nfa.read_string(text)

#print nfa.is_accepting()
print nfades.is_accept(text)