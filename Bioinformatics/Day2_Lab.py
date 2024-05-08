'''This document contains the key functions created as part of Day 2's lab.'''
import matplotlib.pyplot as plt
import numpy as np
import math

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

def count(dna):
    l=len(dna[0])
    matrix: np.ndarray = np.zeros((4,l))
    for i in range(l):
        dict = {'A':0, 'C':0, 'G':0, 'T':0}
        for seq in dna:
            dict[seq[i]]+=1
        j=0
        for key in dict:
            matrix[j,i]=dict[key]
            j+=1
    return matrix

def profile(dna):
    return count(dna)*(1/4)

def entropy(profile):
    col = len(profile[0])
    matrix = np.zeros((1,col))
    for i in range(col):
        temp = []
        for j in range(4):
            if profile[j,i]>0:
                temp.append(profile[j,i])
        sum = 0
        for k in temp:
            sum += k * (math.log2(k))
        if sum == 0:
            matrix[0,i] = sum
        else:
            matrix[0,i] = -sum
    return matrix

def get_kmers(dna,k):
    return list(set([dna[i:i+k] for i in range(len(dna)-k+1)]))
def MotifEnumeration(Dna, k, d):
    # Brute force algorithm for motif finding.
    # Given a collection of strings Dna and an integer d,
    # a k-mer is a (k,d)-motif if it appears in every string from
    # Dna with at most d mismatches.
    patterns = set()
    for pattern in get_kmers(Dna[0],k):
        for pat in neighbors(pattern,d):
            match_all = True
            for dna in Dna[1:]: # Check each string of DNA
                # Need to see if any neighbors of our pattern are in t
                match_all = match_all and any([neighbor in dna for neighbor in neighbors(pat,d)])
            if match_all: # if
                patterns.update([pat])
    return patterns

def distBetweenPatternAndStrings(pattern, dnaList):
    k = len(pattern)
    dist = 0
    for dna in dnaList:
        hDist = math.inf
        for kmer in get_kmers(dna,k):
            if hDist > hammingDist(pattern, kmer):
                hDist = hammingDist(pattern, kmer)
        dist+=hDist
    return dist

def score(motifList, dnaList):
    dict = {}
    for motif in motifList:
        dict[motif]=distBetweenPatternAndStrings(motif, dnaList)
    return dict

def allString(k):
    string = ""
    for _ in range(k):
        string+="A"
    return(list(neighbors(string, k)))

def medianString(dna, k):
    dist = math.inf
    patterns = allString(k)
    for i in range(len(patterns)):
        pattern = patterns[i]
        if dist > distBetweenPatternAndStrings(pattern, dna):
            dist = distBetweenPatternAndStrings(pattern, dna)
            median = pattern
    return median

def countPseudo(dna):
    return count(dna)+1

def profilePseudo(dna):
    return count(dna)*(1/8)

def consensus(seqList):
    pro = profilePseudo(seqList)
    l = len(pro)
    final = ""
    for i in range(l):
        posMax = 0
        pos = ""
        for j in range(4):
            if pro[j,i] > posMax:
                posMax = pro[j,i]
                if j==0:
                    pos="A"
                elif j==1:
                    pos="C"
                elif j==2:
                    pos="G"
                elif j==3:
                    pos="T"
        final+=pos
    return final