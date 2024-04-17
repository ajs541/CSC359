'''This document contains the key functions created as part of Day 2's lab.'''

def PatternCount(Text, Pattern):
    '''Counts how many times the pattern occurs
    inside of Text.'''
    count = 0
    for i in range(len(Text) - len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count += 1
    return count

def FrequencyTable(Text, k):
    '''This function finds all k-mers and counts
    how many times each k-mer occurs in our
    map.'''
    freqMap = {}
    n = len(Text)
    for i in range(0, n-k+1):
        Pattern = Text[i:(i+k)]
        freqMap[Pattern] = freqMap.get(Pattern, 0) +1 
    return freqMap

def MaxMap(freqMap):
    return max(freqMap.values())

def FrequentWords(Text, k):
    '''This function searches a genome, Text, for
    the most frequent substrings of length k, 
    also called k-mers, that occur in the
    genome.'''
    frequentPatterns = []
    freqMap = FrequencyTable(Text,k)
    maxVal = MaxMap(freqMap)
    for Pattern in freqMap:
        if freqMap[Pattern] == maxVal:
            frequentPatterns.append(Pattern)
    return frequentPatterns

def ReverseComplement(ParentStrand):
    '''Returns the reverse complement of the parent strand'''
    basePairs = {'A':'T', 'T':'A','G':'C', 'C':'G'}
    complement = ""
    for nuc in ParentStrand:
        complement += basePairs[nuc]
    return complement[::-1]

def PatternMatch(genome, pattern):
    '''Finds all locations of pattern in genome.'''
    locations = []
    k = len(pattern)
    n = len(genome)
    for i in range(n-k+1):
        if genome[i:i+k] == pattern:
            locations.append(i)
    return locations

def FindClumps(Text, k, L, t):
    '''Find clumps uses a rolling window size of length
    L and finds any k-mers that occur at least t times
    inside the window.'''
    Patterns = set()
    n = len(Text)
    for i in range(n-L+1):
        Window = Text[i:L+i]
        freqMap = FrequencyTable(Window, k)
        for s in freqMap:
            if freqMap[s] >= t:
                Patterns.add(s)
    return Patterns