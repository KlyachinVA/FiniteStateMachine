class DPDA:
    def __init__(s,cur_config,accept_states, rulebook):
        s.cur_config=cur_config
        s.accept_states=accept_states
        s.rulebook=rulebook
    def read_char(s,char):
        s.cur_config=s.rulebook.next_config(s.cur_config,char)
    def is_accept(s):
        if(s.cur_config): return s.cur_config.state in s.accept_states
        else: return False
    def read_string(s,str):
        for char in str:
            s.read_char(char)
            if s.cur_config : 
                pass
                #print s.cur_config.state
                #print s.cur_config.stack
        s.read_char('')
