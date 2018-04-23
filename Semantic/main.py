from Semantic import *

s=Add(Number(12),Mul(Number(12),Add(Number(2),Number(3))))
print s
M=MachineE(s,{})
M.run()
n=Number(122)
M=MachineE(LessThen(n,s),{})
M.run()
M=MachineE(Add(Number(15),Variable("x")),{"x":Number(100)})
M.run()
MachineS(Assign("a",Add(Variable("a"),Number(1))),{"a":Number(2)}).run()
MachineS(If(Variable("x"),Assign("y",Number(1)),Assign("y",Number(2))),{"x":Boolean(True)}).run()
MachineS(While(LessThen(Variable("x"),Number(5)),Assign("x",Mul(Variable("x"),Number(3)))),{"x":Number(1)}).run()
