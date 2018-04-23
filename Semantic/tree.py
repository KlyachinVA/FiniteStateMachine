from Semantic import *


a={'type':'Number','value':12, 'left':None, 'right':None}
b={'type':'Number','value':34, 'left':None, 'right':None}
c={'type':'Number','value':4, 'left':None, 'right':None}
d={'type':'Number','value':7, 'left':None, 'right':None}
plus1={'type':'Operation', 'value':'+', 'left':None, 'right':None}
plus2={'type':'Operation', 'value':'+', 'left':None, 'right':None}
mult1={'type':'Operation', 'value':'*', 'left':None, 'right':None}

plus1['left']=a
plus1['right']=plus2
plus2['left']=mult1
plus2['right']=d
mult1['left']=b
mult1['right']=c

syntax_tree = plus1

def make_node(node):
	if node["type"]=='Operation':
		if node['value']=='+': return Add(None,None)
		if node['value']=='*': return Mul(None,None)
	if node["type"]=="Number": return Number(node["value"])

def make_tree(tree):
	stack=[]
	stack_expr=[]
	stack.append(tree)
	res_expr=make_node(tree)
	stack_expr.append(res_expr)
	while(len(stack)>0):
			elem= stack.pop()
			expr=stack_expr.pop()
			if elem['left']: 
				l=make_node(elem["left"])
				if expr.reducable(): 
					expr.left=l
					stack.append(elem['left'])
					stack_expr.append(l)
			if elem['right']: 
				r=make_node(elem["right"])
				if expr.reducable(): 
					expr.right=r
					stack.append(elem['right'])
					stack_expr.append(r)
	return res_expr

s=make_tree(syntax_tree)
M=MachineE(s,{})
M.run()	
	