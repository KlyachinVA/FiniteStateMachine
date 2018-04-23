from pdarule import PDAConfiguration,PDARule, DPDARuleBook
from dpda import DPDA

r1=PDARule(1,'(',2,'$',['$','b'])
r2=PDARule(2,'(',2,'b',['b','b'])
r3=PDARule(2,')',2,'b',[])
r31=PDARule(2,'(',2,'$',['$','b'])
r4=PDARule(2,'',1,'$',['$'])

rulebook=DPDARuleBook([r1,r2,r3,r31,r4])

dpda= DPDA(PDAConfiguration(1,['$']),[1],rulebook)
# print dpda.is_accept()
# print dpda.cur_config.stack
# dpda.read_char('(')
# print dpda.cur_config.stack
# dpda.read_char(')')
# print dpda.cur_config.stack
# dpda.read_char('')
# print dpda.cur_config.stack

dpda.read_string('()(())((())');
print dpda.is_accept()