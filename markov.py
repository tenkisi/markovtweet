# -*- coding: utf-8 -*-
import random

ngram = lambda text, n: [text[i:i+n] for i in xrange(len(text) - n + 1)]

flatten2D = lambda data: [flattened for inner in data for flattened in inner]

randelement = lambda x: x[random.randint(0, len(x) - 1)]

class Markov:
    def __init__(self, data, n):
        self.data = data
        self.n = n
    
    def markov(self, limit, firstword, lastword, getlength, lengthlimit=None, result=None): 
        if limit == 0:
            return [k for k in [i[0] for i in result[:-1]] + result[-1]]
        
        candidatelist = []
        if result != None:
            candidatelist = [candidate for candidate in self.data if result[-1][1:self.n] == candidate[0:self.n - 1]]
        else:
            result = []
            candidatelist = [candidate for candidate in self.data if candidate[0] == firstword]
       
        if candidatelist == []:
            result.append(randelement(self.data))
        else:
            result.append(randelement(candidatelist))
        
        wordcount = getlength([k for k in [i[0] for i in result[:-1]] + result[-1]])
        charlimitflag = lengthlimit == None or wordcount < lengthlimit
        if not charlimitflag:
            result = result[:-1]
        
        mrkv = lambda li: self.markov(li, firstword, lastword, getlength, lengthlimit, result)
        return mrkv(limit - 1) if charlimitflag and result[-1][-1] != lastword else mrkv(0)
        
