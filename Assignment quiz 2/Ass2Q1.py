def longest_common_substring(s1, s2):
    """that takes two strings as parameters and returns 
    the longest common substring, using the algorithm 
    given in the notes"""
    
    return lcs(s1, s2, cache=None)
    
def lcs(s1, s2, cache=None):
    
    #Initialise variables
    s1_len, s2_len = len(s1), len(s2)

    #What does this do?
    if cache is None:
        cache = dict()
    #If both strings are empty return ""
    if s1_len == 0 or s2_len == 0:
        return ""
    #Elif the item the key(index) already in the cache, use the value(letter).
    elif (s1_len, s2_len) in cache.keys():
        return cache[(s1_len, s2_len)]
    else:
        #If the characters match, add the character and the prev cache string to the new cache value
        if s1[-1] == s2[-1]:
            cache[(s1_len, s2_len)] = lcs(s1[:-1], s2[:-1], cache) + s2[-1]
            return cache[(s1_len, s2_len)]
        else:
            #Take the max of the two cache values and add to cache
            cache[(s1_len, s2_len)] = max(lcs(s1, s2[:-1], cache), lcs(s1[:-1], s2, cache), key=len)
            return cache[(s1_len, s2_len)]
    
s1 = "Look at me, I can fly!"
s2 = "Look at that, it's a fly"
print(longest_common_substring(s1, s2))

s1 = "abcdefghijklmnopqrstuvwxyz"
s2 = "ABCDEFGHIJKLMNOPQRSTUVWXYS"
print(longest_common_substring(s1, s2))

s1 = "balderdash!"
s2 = "balderdash!"
print(longest_common_substring(s1, s2))

s1 = "glorious"
s2 = "algorithms"
print(longest_common_substring(s1, s2))
