from npdarule import PDAConfiguration,PDARule, NPDARuleBook
from npda import NPDA,NPDADesign

r1=PDARule(1,'a',1,'$',['$','a'])
r2=PDARule(1,'a',1,'a',['a','a'])
r3=PDARule(1,'a',1,'b',['b','a'])
r4=PDARule(1,'b',1,'$',['$','b'])
r5=PDARule(1,'b',1,'a',['a','b'])
r6=PDARule(1,'b',1,'b',['b','b'])
r7=PDARule(1,'',2,'$',['$'])
r8=PDARule(1,'',2,'a',['a'])
r9=PDARule(1,'',2,'b',['b'])
r10=PDARule(2,'a',2,'a',[])
r11=PDARule(2,'b',2,'b',[])
r12=PDARule(2,'',3,'$',['$'])


rulebook=NPDARuleBook([r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12])

npda_des= NPDADesign(1,'$',[3],rulebook)
print npda_des.is_accept("baab")