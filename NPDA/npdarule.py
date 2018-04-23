class PDAConfiguration:
    def __init__(s,state,stack):
        s.state=state
        s.stack=stack
    def __str__(s):
        return str([s.state,s.stack])
    # def __eq__(s,ac):
        # return s.state == ac.state #and s.stack == ac.stack
    def __ne__(s,ac):
        return s.state != ac.state or s.stack != ac.stack
class PDARule:
    def __init__(s,state,char,next_state,pop_char,push_chars):
        s.state=state
        s.char=char
        s.next_state=next_state
        s.push_chars=push_chars
        s.pop_char=pop_char
    def is_applies(s,config,char):
        #print s.state, s.pop_char, s.push_chars
        if(config and len(config.stack)>0): return s.state==config.state and s.pop_char==config.stack[-1] and (s.char == char)
        else: return False		
    def follow(s,config):
        #print "Old config=",config
        nconfig=PDAConfiguration(s.next_state,s.next_stack(config))
        #print "New config",nconfig
        return nconfig

    def next_stack(s,config):
        newstack=list(config.stack)
        if(config.stack): newstack.pop()
        
        for char in s.push_chars:
            newstack.append(char)
        #print newstack
        return newstack
        
class NPDARuleBook:
    def __init__(s, rules):
        s.rules=rules
    def next_config(s,configs,char):
        new_configs=set()
        for config in configs:
            new_configs=new_configs | set(s.follow_rules_for(config,char))
        #print new_configs
        return new_configs
    def follow_rules_for(s,config,char):
        nconfigs=map(lambda rule: rule.follow(config), s.rule_for(config,char))	
        #print map(lambda config: config.state,configs)
        return nconfigs		
    def rule_for(s,config,char):
        adm_rules=[]
        for rule in s.rules:
            if rule.is_applies(config,char):
                adm_rules.append(rule)
        #print "ADM: stack= ",config.stack,"|",map(lambda rule:[rule.state,rule.char,rule.next_state] , adm_rules)
        return adm_rules
				
    def follow_free_moves(s,configs):
        more_configs=s.next_config(configs,'')
        
        f=True
        for cnf in more_configs:
            #print cnf.stack
            flag=False
            for conf in configs:
                if cnf.state == conf.state and cnf.stack == conf.stack : 
                    flag=True
            if flag == False: 
                f=False
                break
        if f: return configs
        else:
            return s.follow_free_moves(configs|more_configs)
            #return configs|more_configs
            
    
