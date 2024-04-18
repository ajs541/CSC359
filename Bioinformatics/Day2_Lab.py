'''This document contains the key functions created as part of Day 2's lab.'''
import matplotlib.pyplot as plt

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

def skew(text):
    sCountList = []
    sCount = 0
    length = len(text)
    for i in range(length):
        if text[i] == 'C':
            sCount -= 1
        elif text[i] == 'G':
            sCount += 1
        sCountList.append(sCount)
    return sCountList

ecoli = open("EColi.fasta.txt", 'r').read().split()
ecoli = "".join(ecoli)

def minimizeSkew(text):
    minimum = 0
    locations = []
    count = 1
    for i in skew(text):
        if i < minimum:
            minimum = i
            locations = [count]
        elif i==minimum:
            locations.append(count)
        count+=1
    return locations

def hammingDist(textA, textB):
    dist = 0
    length = len(textA)
    for i in range(length):
        if textA[i] != textB[i]:
            dist+=1
    return dist

def approxPatternCount(text, pattern, d):
    count = 0
    t = len(text)
    p = len(pattern)
    for i in range(t-p+1):
        patternTwo = text[i:i+p]
        if hammingDist(pattern, patternTwo) <= d:
            count += 1
    return count

def approxMatch(genome, pattern, d):
    '''Finds all locations of pattern in genome.'''
    locations = []
    k = len(pattern)
    n = len(genome)
    for i in range(n-k+1):
        patternTwo = genome[i:i+k]
        if hammingDist(pattern, patternTwo) <= d:
            locations.append(i)
    return locations

def neighbors(pattern, d):
    nucTides = {'A','C','G','T'}
    if d==0:
        return {pattern}
    if len(pattern)==1:
        return nucTides
    progNeighbors = neighbors(pattern[1:], d)
    
    bors = set()
    for i in progNeighbors:
        if hammingDist(pattern[1:], i) < d:
            bors.update([nuc + i for nuc in nucTides])
        else:
            bors.add(pattern[0] + i)
    
    return bors

def freqWordsWithMisMatch(text, k, d):
    
    patterns = []
    freqMap = {}
    n = len(text)
    
    for i in range(n-k+1):
        pattern = text[i:i+k]
        bors = neighbors(pattern, d)
        for j in bors:
            nB = j
            freqMap[nB] = freqMap.get(nB, 0) + 1
    m = MaxMap(freqMap)
    for key in freqMap:
        if freqMap[key] == m:
            patterns.append(key)
    return patterns

def freqWordsWithMisMatchRC(text, k, d):
    
    patterns = []
    freqMap = {}
    n = len(text)
    
    for i in range(n-k+1):
        pattern = text[i:i+k]
        bors = neighbors(pattern, d)
        for j in bors:
            nB = j
            reverseNB = ReverseComplement(j)
            freqMap[nB] = freqMap.get(nB, 0) + 1
            freqMap[reverseNB] = freqMap.get(reverseNB, 0) + 1
    m = MaxMap(freqMap)
    for key in freqMap:
        if freqMap[key] == m:
            patterns.append(key)
    return patterns

