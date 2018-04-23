from npdarule import PDAConfiguration
 
class NPDA:
    def __init__(s,cur_configs, accept_states, rulebook):
        s.cur_configs=set(cur_configs)
        s.accept_states=accept_states
        s.rulebook=rulebook
        s.add_empty_passes()
        #for c in s.cur_configs: print c
    def add_empty_passes(s):
        for c in s.cur_configs: print c
        print "--------------"
        curconfigs=list(s.cur_configs)
        #emptyconfigs = s.rulebook.next_config(curconfigs,'')
        #for c in emptyconfigs: print c
        emptyconfigs=s.rulebook.follow_free_moves(s.cur_configs)
        s.cur_configs=s.cur_configs | emptyconfigs
        #for c in s.cur_configs: print c
        #print "-----------------"
    def is_accept(s):
        flag=False
        for config in s.cur_configs:
            if config.state in s.accept_states: flag=True
        return flag
    def read_char(s,char):
                
        newconfigs=s.rulebook.next_config(s.cur_configs,char)
        
        #print "EMPT::",map(lambda c: [c.state,c.stack],emptyconfigs)
        s.cur_configs = newconfigs
        s.add_empty_passes()
        #print char,': ',map(lambda conf: [conf.state,conf.stack], s.cur_configs)
        #print map(lambda conf: conf.stack, s.cur_configs)
    def read_str(s,str):
        for char in str:
            
            s.read_char(char)
        s.read_char('')
    # def curr_configs(s):
        # return s.rulebook.follow_free_moves(s.cur_configs)
 
class NPDADesign:
    def __init__(s,start_state,bottom_char,accept_states,rulebook):
        s.start_state=start_state
        s.bottom_char=bottom_char
        s.accept_states=accept_states
        s.rulebook=rulebook
    def is_accept(s,str):
        npda=s.to_npda()
        npda.read_str(str)
        return npda.is_accept()
    def to_npda(s):
        start_config=PDAConfiguration(s.start_state,[s.bottom_char])
        return NPDA([start_config],s.accept_states,s.rulebook)
