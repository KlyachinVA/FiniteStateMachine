
class Number(object):
    def __init__(s,value):
        s.value=value
    def __str__(s):
        return str(s.value)
    def reducable(s): return False		


	
class Add(object):
    def __init__(s,l,r):
        s.left=l
        s.right=r
    def __str__(s):
        return "("+str(s.left)+" + "+str(s.right)+")"
    def reducable(s): return True
    def reduce(s,env):
        res=None
       
        if(s.left.reducable()):
            
            res=Add(s.left.reduce(env),s.right)
        elif(s.right.reducable()):
            res= Add(s.left,s.right.reduce(env))
        else: res=Number(s.left.value + s.right.value)
        return res


	
	
class Mul(object):
    def __init__(s,l,r):
        s.left=l
        s.right=r
    def __str__(s):
        return str(s.left)+" * "+str(s.right)
    def reducable(s): return True
    def reduce(s,env):
        res=None
       
        if(s.left.reducable()):
            
            res=Mul(s.left.reduce(env),s.right)
        elif(s.right.reducable()):
            res= Mul(s.left,s.right.reduce(env))
        else: res=Number(s.left.value * s.right.value)
        return res
class Boolean(object):
    def __init__(s,v):
        s.value=v
    def __str__(s):
        return str(s.value)
    def reducable(s):
        return False
class LessThen(object):
    def __init__(s,l,r):
        s.left=l
        s.right=r
    def __str__(s):
        return str(s.left)+" < "+ str(s.right)
    def reducable(s):
        return True
    def reduce(s,env):
        res=None
        if s.left.reducable():
            res=LessThen(s.left.reduce(env),s.right)
        elif s.right.reducable():
            res=LessThen(s.left,s.right.reduce(env))
        else: res= Boolean(s.left.value < s.right.value)
        return res
class Variable(object):
    def __init__(s,n):
        s.name=n
    def __str__(s):
        return str(s.name)
    def reducable(s):
        return True
    def reduce(s,env):
        return env[s.name]
		
class DoNothing(object):
    def __str__(s):
        return "do-nothing"
    def reducable(s):
        return False
class Assign(object):
    def __init__(s,n,exp):
        s.name=n	
        s.expression=exp
    def __str__(s):
        return str(s.name)+" = "+str(s.expression)
    def reducable(s):
        return True
    def reduce(s,env):
        if s.expression.reducable():
            return [Assign(s.name,s.expression.reduce(env)),env]
        else:
            new_env=dict(env)
            new_env[s.name]=s.expression
            return [DoNothing(),new_env]
class If(object):
    def __init__(s,cond,cons,alter):
        s.condition=cond
        s.consequence=cons
        s.alternative=alter
    def __str__(s):
        return "if ("+str(s.condition)+") {"+str(s.consequence) +" } else {" + str(s.alternative) +"}"
    def reducable(s):
        return True
    def reduce(s,env):
        if s.condition.reducable():
            return [If(s.condition.reduce(env),s.consequence,s.alternative),env]
        else:
            if s.condition.value: return [s.consequence,env]
            else: return [s.alternative,env]
			
class Sequence(object):
    def __init__(s,fr,se):
        s.first=fr
        s.second=se
    def __str__(s):
        return str(s.first)+"; "+str(s.second)
    def reducable(s):
        return True
    def reduce(s,env):
        if type(s.first) == DoNothing: return [s.second,env]
        else:
            red_first, red_env = s.first.reduce(env)
            return [Sequence(red_first,s.second),red_env]
class While(object):
    def __init__(s,cond,body):
        s.condition=cond
        s.body=body
    def __str__(s):
        return "while("+str(s.condition)+") {"+str(s.body)+"}"
    def reducable(s):
        return True
    def reduce(s,env):
        return [If(s.condition,Sequence(s.body,s),DoNothing()),env]
class MachineE(object):
    def __init__(s,e,env):
        s.expression=e
        s.environment=env
    def step(s):
        s.expression = s.expression.reduce(s.environment)
    def run(s):
        while s.expression.reducable():
            print s.expression
            s.step()
        print s.expression
		
class MachineS(object):
    def __init__(s,st,env):
        s.statement=st
        s.environment=env
    def step(s):
        s.statement,s.environment = s.statement.reduce(s.environment)
    def run(s):
        while s.statement.reducable():
            print s.statement , s.print_env(s.environment)
            s.step()
        print s.statement , s.print_env(s.environment)
		
    def print_env(s,env):
        res="{"
        for k in env:
            res+="<<"+k+"="+str(env[k])+">> "	
        return res	+ "}"		