#coding=utf8
import re,collections

def kwords(text):
	return re.findall(r'[a-z]+',text.lower())

def fwords(kw):
	dt = collections.defaultdict(lambda:1)
	for k in kw:
		dt[k]+=1
	return dt

wordfreq = fwords(kwords(open('big.txt','r').read()))
abt = 'abcdefghijklmnopqrstuvwxyz'

def edits1(word):
	n = len(word)
	word1 = set([word[0:i] + word[i+1:] for i in range(n)] +
	[word[0:i] + word[i+1] + word[i] + word[i+2:] for i in range(n-1)] +
	[word[0:i] + w + word[i:] for i in range(n+1) for w in abt] +
	[word[0:i] + w + word[i+1:] for i in range(n)for w in abt]
	)
	return word1

def edits2(word):
	return set(w for ww in edits1(word) for w in edits1(ww) if w in wordfreq)

def rights(words):
	return set(w for w in words if w in wordfreq)

def correct(word):
	choices = rights([word]) or rights(edits1(word)) or rights(edits2(word))
	return max(choices,key = lambda x:wordfreq[x])

if __name__ == '__main__':
	import sys
	for i in sys.argv[1:]:
		print correct(i)
