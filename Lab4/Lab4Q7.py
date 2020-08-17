def find_pit(seq):
    n = len(seq)
    return helper(seq, 0, n-1, n)

def helper(seq, l, r, n):
    m = (l+r)//2 
    if (m == 0 or seq[m-1] >= seq[m]) and (m == n-1 or seq[m+1] >= seq[m]):
        return m
    elif m > 0 and seq[m-1] < seq[m]:
        return helper(seq, l, m-1, n)
    else: 
        return helper(seq, m+1, r, n)
    
#print(find_pit([5, 4, 5]))

#print(find_pit([10]))

#print(find_pit([10, 7, 5, 4]))

#import random
#import math
    
#class StingySequence:
    #"""Encapsulates a list and records the number of reads."""
    #def __init__(self, iterable):
        #self.array = list(iterable)
        #self.access_count = 0

    #def __getitem__(self, index):
        #if type(index) is int:
            #self.access_count += 1
            #return self.array[index]
        #elif type(index) is slice:
            #self.access_count += sum(1 for _ in self.array[index])
            #return self.array[index]
        #else:
            #raise TypeError("Only integer and slice indexing is supported.")

    #def __len__(self):
        #return len(self.array)


#def test_pit_finder():
    #n = 1000
    #num_instances = 300
    #c = 10
    #seqs = [StingySequence(random.randint(0,50) for _ in range(n))
            #for _ in range(num_instances)]
    #print(all(_is_pit(seq, find_pit(seq)) for seq in seqs))
    ## The following should hold for a large enough n:
    #print(all(seq.access_count <= c * math.log2(n) for seq in seqs))
        
#test_pit_finder()
