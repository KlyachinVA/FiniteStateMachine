class PDAConfiguration:
    def __init__(s,state,stack):
        s.state=state
        s.stack=stack

class PDARule:
    def __init__(s,state,char,next_state,pop_char,push_chars):
        s.state=state
        s.char=char
        s.next_state=next_state
        s.push_chars=push_chars
        s.pop_char=pop_char
    def is_applies(s,config,char):
        #print s.state, s.pop_char, s.push_chars
        if(config): return s.state==config.state and s.pop_char==config.stack[-1] and s.char == char
        else: return False		
    def follow(s,config):
        return PDAConfiguration(s.next_state,s.next_stack(config))

    def next_stack(s,config):
        config.stack.pop()
        popped_stack=config.stack
        for char in s.push_chars:
            config.stack.append(char)
        return config.stack
        
class DPDARuleBook:
    def __init__(s, rules):
        s.rules=rules
    def next_config(s,config,char):
        rule=s.rule_for(config,char)
        if rule : return rule.follow(config)		
		
    def rule_for(s,config,char):
        for rule in s.rules:
            if rule.is_applies(config,char):
                #print rule.state
                return rule

        