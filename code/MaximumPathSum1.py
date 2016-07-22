import math 
import bisect
import itertools
from collections import Counter
def MaximumPathSum1(numRows):
	f=open('p067_triangle.txt')
	lines=f.readlines()
	f.close()
	lines=[[int(n) for n in line.split(' ')] for line in lines]
	print(lines)
	MAX=len(lines)
	for y in range(MAX-2, -1, -1):
		for x in range(y+1):
			lines[y][x]+=max(lines[y+1][x],lines[y+1][x+1])
	print(lines)
	print(lines[0][0])

def NamesScores():
	f=open('p022_names.txt')
	lines = f.readlines()
	f.close()
	names = []
	for line in lines:
		n = line.split(',')
		for x in n:
			bisect.insort_left(names, x.replace('"',''))
	result = 0
	for i in range(len(names)):
		result += nameValue(names[i])*(i+1)
	print(result)

def nameValue(name):
	result = 0
	for x in list(name):
		result += ord(x)-64
	return result

def CountingSundays():
	nonleap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	day1 = 1+sum(nonleap)%7
	count = 0
	for x in range(100):
		for i in range(12):
			if((x+1)%4==0):
				day1 += leap[i]
			else:
				day1 += nonleap[i]
			day1 = day1%7
			if(day1==0):	
				count+=1
	if(day1==0):
		count-=1
	print(count)

def FactorialDigitSum(n):
	s = 0
	num = math.factorial(n)
	while num:
		s += num %10
		num //= 10
	print(s)

def AmicableNumbers(n):
	s = 0
	for x in range(1, n, 1):
		if(d(x) != x and d(d(x)) == x):
			s += x
	print(s)

def d(n):
	s = 0
	for x in range(1, int((n+2)/2), 1):
		if(n%x==0):
			s+=x
	return s

def NonAbundantSums():
	MAX = 28124
	abundant = []
	sumAbund = []
	for x in range(MAX-1,-1, -1):
		if(d(x) > x):
			abundant.append(x)
			for i in range(len(abundant)-1,-1,-1):
				r = x+abundant[i]
				if r >= MAX:
					break
				sumAbund.append(x+abundant[i])
	s = set(sumAbund)
	print(sum(range(MAX)) - sum(s))

def LexicographicPermutations():
	perm =itertools.permutations([0,1,2,3,4,5,6,7,8,9]) 
	counter = 1
	for x in perm:
		if(counter < 1000000):
			counter+=1
		else:
			print(x)
			break

def DigitFiboNumber(n=1000):
	a = 1
	b = 1
	index = 3
	while True:
		c = a+b
		if(len(str(c))>=n):
			print(c)
			print(str(c))
			print(len(str(c)))
			break
		a = b
		b = c
		index += 1
	print(index)

def ReciprocalCycles():
	seq = 0
	li = []
	for i in range(2, 1000):
		remain = []
		r = 1%i
		r = 10*r
		remain.append(r)
		counter = 0
		bol = True
		while r%i != 0:
			r = (r%i)
			while r < i:
				r = r*10
			if r in remain:
				x = len(remain)-remain.index(r)
				li.append((i, x))
				break
			remain.append(r)
			if len(remain) >= i:
				break
	seq = 0
	m = 0
	for i in li:
		(x, y) = i
		if y > seq:
			seq = y
			m = x
	print((m, seq))

def QuadraticPrimes(ne=1000):
	nn = ne*-1 + 1
	foo = lambda x, y, z : x * x + y*x + z
	numPrimesInRow = 0
	values = (0,0,0)
	for i in range(nn,ne,1):
		for j in range(nn,ne,1):
			n = 0
			while is_prime(foo(n, i, j)):
				if(n>numPrimesInRow):
					numPrimesInRow = n
					values = (n, i, j)
				n+=1
	print(values)
	(n, i, j) = values
	print(i*j)

def is_prime(n):
	if n == 2 or n == 3: return True
	if n < 2 or n%2 == 0: return False
	if n < 9: return True
	if n%3 == 0: return False
	r = int(n**0.5)
	f = 5
	while f <= r:
		if n%f == 0: return False
		if n%(f+2) == 0: return False
		f +=6
	return True  

def NumberSpiralDiagonals(n=1001):
	spiral = []
	for i in range(n):
		l = []
		for j in range(n):
			l.append(0)
		spiral.append(list(l))

	value = n*n
	done = False
	(i,j) = (0,n-1)
	while not done:
		while spiral[i][j] == 0:
			spiral[i][j] = value
			value-=1
			j-=1
			if j<0:
				break
		j+=1
		i+=1
		while spiral[i][j] == 0:
			spiral[i][j] = value
			value-=1
			i+=1
			if i > n-1:
				break
		i-=1
		j+=1
		while spiral[i][j] == 0:
			spiral[i][j] = value
			value-=1
			j+=1
			if j > n-1:
				break
		j-=1
		i-=1
		while spiral[i][j] == 0:
			spiral[i][j] = value
			value-=1
			i-=1
		i+=1
		j-=1
		if value < 1:
			done = True
	s = 0
	for i in range(n):
		s += spiral[i][i]
		s += spiral[i][n-1-i]
	s-=1
	print(s)
	
def DistinctPowers(start=2,finish=100):
	powers = []
	for i in range(start, finish+1):
		for j in range(start, finish+1):
			powers.append(i**j)
	print(len(set(powers)))

def DigitFifthPowers(n=5):
	pows = []
	for i in range(10, 1000000, 1):
		x = 0
		for s in list(str(i)):
			x += int(s) ** n
		if x == i:
			pows.append(i)
	print(sum(pows))

def PandigitalProducts():
	product = 0
	products = set()
	for i in range(2, 10000):
		for j in range(2, 10000):
			product = i * j
			if(len(str(product) + str(i) + str(j)))>9:
				break
			if test(i,j,product):
				a = len(products)
				products.add(product)
	print(sum(products))


def test(p1, p2, prod):
	l = list(str(prod) + str(p1) + str(p2))
	if len(l) == 9:
		i = 1
		for x in sorted(l):
			if int(x) != i:
				return False
			i+=1
		return True
	return False

def DigitFactorials(n=10000000):
	ground = 10
	facts = []
	i = ground
	while i < n:
		fact = factorials(i)
		if fact>i:
			ground+=10
			i = ground
			continue
		if i > fact+math.factorial(9):
			ground+=10
			i=ground
			continue
		elif i==fact:
			facts.append(i)
		if (i+1)%10==0:
			ground+=10
		i+=1
	print(sum(facts))


def factorials(n):
	l = list(str(n))
	s = 0
	for i in l:
		s += math.factorial(int(i))
	return s

def CircularPrimes():
	circ = []
	for i in range(2, 1000000):
		if is_prime(i):
			x = rotateNumber(i)
			if x == i and len(str(x)) > 2: 
				continue
			prime = True
			while x != i:
				if not is_prime(x):
					prime = False
				x = rotateNumber(x)
			if prime:
				circ.append(i)

	print(len(circ))

def rotateNumber(n):
	l = list(str(n))
	l.append(l[0])
	l = l[1:]
	x = ''.join(l)
	if "0" in x: 
		return n
	return int(x)

def DoubleBasePalindromes(n=585):
	pals = []
	for n in range(1, 1000000):
		a = baseN(n, 2)
		if isPalindrome(n) and isPalindrome(a):
			pals.append(n)
	print(sum(pals))

def isPalindrome(n):
	l = list(str(n))
	x = len(l)-1
	if(l[0]=="0" or l[x]=="0"):
		return False
	b = True
	for a in range(x+1):
		if l[a] != l[x-a]:
			b = False
			break
	if not b:
		return False
	return True

def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
	return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

def TruncatablePrimes():
	primes = []
	index = 10
	while len(primes) < 11: 
		if is_prime(index):
			left = list(str(index))
			right = list(str(index))
			left = left[1:]
			right = right[:-1]
			b = True
			while len(left) > 0 and len(right) > 0:
				if not is_prime(int(''.join(left))) or not is_prime(int(''.join(right))):
					b = False
				left = left[1:]
				right = right[:-1]
			if b:
				primes.append(index)
		index+=1
	print(sum(primes))

def PandigitalMultiples():
	i = 2
	l = []
	n = 1000000
	while i * 3 < n:
		s = ""
		x = 1
		while len(s) < 9:
			s += str(x*i)
			x+=1
		if ''.join(sorted(s)) == "123456789":
			l.append([int(s), i])
		i+=1
	print(sorted(l)[-1][0])

def IntegerRightTriangles():
	n=120
	b=1
	length = 0
	index = 0
	for a in range(1, 1001):
		l = []
		for i in range(int(a/2)):
			for j in range(int(a/2)):
				if (i*i + j*j) ** 0.5 + i + j == a:
					l.append((i,j,a))
		if(len(l) >= length):
			index = a
			length = len(l)
	print(index)
	print(length/2)

def ChamperConstant():
	l = list(''.join([str(x) for x in range(1000000)]))
	s = 1
	for i in range(7):
		s *= int(l[10 ** i])
	print(s)
		
def PandigitalPrime():
	for i in range(9,0,-1):
		l = [str(x) for x in range(1,i+1)]
		x = list(itertools.permutations(l))
		for a in range(len(x)-1,-1,-1):
			b = list(x[a])
			if is_prime(int(''.join(b))):
				print(''.join(b))
				return

def CodedTriangleNumbers():
	l = [int(0.5*i*(i+1)) for i in range(1,100)]
	l.insert(0,0)
	f=open('p042_words.txt')
	lines=f.readlines()
	f.close()
	for line in lines:
		lines=[str(n).replace('"','') for n in line.split(',')] 
	num = 0
	for x in lines:
		try:
			l.index(nameValue(x))
			num+=1
		except ValueError:
			continue
	print(num)

def SubStringDivisibility():
	l = [str(i) for i in range(10)]
	perms = list(itertools.permutations(l))
	divs = [2,3,5,7,11,13,17]
	total = 0
	for a in range(len(perms)):
		x = list(perms[a])
		b = True
		for i in range(1,8):
			s = x[i:i+3]
			if int(''.join(s)) % divs[i-1] != 0:
				b = False
				break
		if b:
			total += int(''.join(x))
	print(total)

def PantogenNumbers():
	l = [int(x*(x*3-1)/2) for x in range(1,3000)]
	o = [] 
	cont = [None] * (l[-1]+1)
	for a in l:
		cont[a] = 1
	for a in l:
		holder = 0
		for b in l:
			if b - holder > a:
				break
			holder = b
			c = a+b
			d = b-a
			if d < 0:
				d = d*-1
			if cont[d] == 1 and c < len(cont) and cont[c] == 1:
				o.append((d, c))
				print(d, c)

	print(o)

def TriangPentaHexa():
	hexa = [int(x*(x*2-1)) for x in range(144, 40000)]
	l = set(hexa)
	exists = []
	del hexa
	penta = [int(x*(x*3-1)/2) for x in range(285, 40000)]
	for x in penta:
		a = len(l)
		l.add(x)
		if a == len(l):
			print(x)
			exists.append(x)
	del penta
	del l
	triang = [int(x*(x+1)/2) for x in range(100000)]
	for x in range(len(triang)):
		for y in exists:
			if(triang[x] == y):
				print(triang[x])
				del triang
				del exists
				print("done")
				return
	del triang
	del exists
	print("done")

def GoldbachConjecture():
	primes = []
	oddComp = []
	for x in range(2,10000000):
		if is_prime(x) :
			primes.append(x)
		elif x % 2 == 1:
			oddComp.append(x)
	for x in oddComp:
		goldbach = False
		for prime in primes:
			if prime > x-2:
				break
			for i in range(1, int((x-prime)/2 +2)):
				if x == prime + 2 * i * i :
					goldbach = True
		if not goldbach :
			print(x)
			break


def getPrimesUnder(n):
	primes = []
	for x in range(2, n):
		if is_prime(x):
			primes.append(x)
	return primes

def getDistinctPrimeFactors(n):
	l = set()
	if n % 2 == 0 :
		l.add(2)
		while n % 2 == 0:
			n = n / 2
	if n % 3 == 0:
		l.add(3)
		while n % 3 == 0:
			n = n/3
	
	f = 5
	while f <= n:
		if n%f == 0: 
			n = n / f
			l.add(f)
			continue
		if n%(f+2) == 0:
			n = n / (f+2)
			l.add(f+2)
			continue
		f +=6
	return l

def DistinctPrimeFactors(n=4):
	for x in range(400, 1000000, n):
		if len(getDistinctPrimeFactors(x)) == n:
			consecutive = 0
			first = 0
			for i in range(x-n, x+n,1):
				if len(getDistinctPrimeFactors(i)) == n:
					consecutive += 1
					if first == 0:
						first = i
					if consecutive == n:
						print(first)
						return
				else:
					consecutive = 0
					first = 0

def SelfPowers():
	print(str(sum([x**x for x in range(1,1000)]))[-10:])

def PrimePermutations():
	for x in range(1488,10000):
		perms = list(itertools.permutations(list(str(x))))
		a = x+3330
		b = x+3330*2
		if not is_prime(x) or not is_prime(a) or not is_prime(b):
			continue
		abool = False
		bbool = False
		for p in perms:
			if a == int(''.join(list(p))):
				abool = True
			if b == int(''.join(list(p))):
				bbool = True

		if abool and bbool:
			print(str(x) + str(a) + str(b))
			return

def ConsecutivePrimeSum():
	primes = getPrimesUnder(1000000)
	m = 0
	c = 0
	for x in primes:
		n = 0
		consecutive = []
		s = sum(consecutive)
		while s < x:
			consecutive.append(primes[n])
			s = sum(consecutive)
			br = False
			if s == x:
				if len(consecutive) > m:
					m = len(consecutive)
					c = x
					break
			while s > x:
				consecutive = consecutive[1:]
				s = sum(consecutive)
				if len(consecutive) < m-2:
					br = True
			if br :
				break
			if s == x:
				if len(consecutive) > m:
					m = len(consecutive)
					c = x
					break

			n+=1
			s = sum(consecutive)
	print((c, m))

def CoinSums():
	coins = [1, 2, 5, 10, 20, 50, 100, 200]
	m = [0 for x in range(201)]
	m[0] = 1
	for coin in coins:
		for x in range(coin, 201):
			m[x] += m[x-coin]
	
	print(m[200])

def CoinPartition():
	p = []
	p.append(1)
	n = 1
	while True:
		i = 0
		penta = 1
		p.append(0)
		sign = [1, 1,-1,-1]
		while penta <= n:
			p[n] += sign[i%4] * p[n-penta]
			p[n] = p[n] % 10**6
			i+=1
			j = int(i/2 + 1)
			j = j if i % 2 == 0 else -1*j
			penta = int(j*(j*3-1)/2)
		if p[n] == 0:
			print(n)
			break
		n+=1

def DigitCancellingFractions():
	l = 1
	k = 1
	for i in range(10,100):
		if i%10==0 or i%11==0:
			continue
		for y in range(i+1,100):
			if y%10==0 or y%11==0:
				continue
			li = removeDigit(i, y)
			if len(li) == 0:
				continue
			a = int(li[0])
			b = int(li[1])
			if a/b == i/y:
				l = l*a
				k = k*b
	if k%l==0:
		print(k/l)

def removeDigit(n, m):
	l = []
	s = list(str(n))
	t = list(str(m))
	if s[0] in t:
		l.append(s[1])
		t.remove(s[0])
		l.append(t[0])
	elif s[1] in t:
		l.append(s[0])
		t.remove(s[1])
		l.append(t[0])
	return l

def PermutedMultiples():
	i = 1
	tens = 1
	while True:
		bol = True
		s = list(str(i))
		if int(i/tens) > 1:
			tens=tens*10
			i = tens
			continue
		for a in range(2,7):
			t = list(str(i*a))
			if sorted(s) != sorted(t):
				bol=False
				break
		if bol:
			break
		i+=1
	print(i)

def CombinatoricSelections():
	m = 0
	s = 1
	for i in range(20,101):
		for j in range(1, i):
			if math.factorial(i)/(math.factorial(j)*math.factorial(i-j)) > 10**6:
				m+=1
	print(m)

def PokerHands():
	f=open('p054_poker.txt')
	lines = f.readlines()
	f.close()
	hands = (line.split() for line in lines)
	values = {r:i for i,r in enumerate('23456789TJQKA', start=2)}
	print( "Project Euler 54 Solution =", sum(hand_rank(hand[:5]) > hand_rank(hand[5:]) for hand in hands))

	
def hand_rank(hand):
	values = {r:i for i,r in enumerate('23456789TJQKA',start=2)}
	straights = [(v, v-1, v-2, v-3, v-4) for v in range(14,5,-1)] + [(14,5,4,3,2)]
	ranks = [(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(),(),(3,2),(4,1)]
	score = list(zip(*sorted(((v, values[k]) for
		k,v in Counter(x[0] for x in hand).items()), reverse=True)))
	score[0] = ranks.index(score[0])
	if len(set(card[1] for card in hand)) == 1: score[0] = 5  # flush
	if score[1] in straights: 
		score[0] = 8 if score[0] == 5 else 4  # str./str. flush
		if score[1] == (14,5,4,3,2): 
			score[1] = (5,4,3,2,1)
	return score

def PrimeDigitReplacement():
	primes = rwh_primes1(10**7)
	print("Starting")
	counter = 1
	for i in primes: 
		for j in range(0,2):
			s = str(i)
			if s[0] == str(j):
				continue
			n = s.count(str(j))
			if n <= 1:
				continue
			count = 0
			for x in range(0,10):
				s = str(i)
				s = s.replace(str(j),str(x))
				if int(s) in primes:
					count+=1
				if 10-x+count < 7:
					break
			if count >= 8:
				print(i)
				return
		if counter % 10*3 == 0:
			print(i)
		counter+=1
		
def rwh_primes1(n):
    sieve = [True] * int(n/2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[int(i/2)]:
            sieve[int(i*i/2)::i] = [False] * int((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in range(1,int(n/2)) if sieve[i]]

if __name__ == "__main__":
	PrimeDigitReplacement()
