import math 
import bisect
import itertools
from collections import Counter
from fractions import gcd
import timeit
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
	return str(n) == str(n)[::-1]

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

def LychrelNumbers():
	lych = 0
	for i in range(1, 10000):
		n = i
		x = False 
		counter = 0
		while not x:
			n = n + reverseAdd(n)
			x = isPalindrome(n)
			counter+=1
			if counter >= 50:
				break
		if not x:
			lych+=1
	print(lych)

def reverseAdd(n):
	return int(str(n)[::-1])
	
def PowerfulDigitSum():
	m = 0
	for i in range(1,100):
		for j in range(1,100):
			powerSum = sum_digits(i ** j)
			if powerSum > m:
				m = powerSum
	print(m)
			
def sum_digits(n):
	s = 0
	while n:
		s += n % 10
		n //= 10
	return s

def SquareRootConvergents():
	numerator = 7
	denominator = 5
	count = 0
	for i in range(2,1000):
		numerator, denominator = numerator + 2*denominator, numerator+denominator
		if len(str(numerator)) > len(str(denominator)):
			count+=1
	print(count)

def SpiralPrimes():
	primes = 0
	counter = 1
	length = 0
	for i in range(2,100000,2):
		length = i+1
		for y in range(4):
			counter+=i
			if is_prime(counter):
				primes+=1
		if primes*100 / (length*2-1) < 10:
			break
	print(length)

def XorDecryption():
	f = open("p059_cipher.txt")
	lines = f.readlines()
	f.close()
	numbers = [(int(y) for y in x.split(",")) for x in lines]
	numbers = list(numbers[0])
	words = ["the","be","is", "a", "though"]
	text = ""
	for a in range(97,123):
		for b in range(97,123):
			for c in range(97,123):
				text = ""
				for i in range(0, len(numbers)):
					if i % 3 == 0:
						text+= chr(numbers[i]^a)
					elif i%3==1:
						text+= chr(numbers[i]^b)
					elif i%3==2:
						text+= chr(numbers[i]^c)
				if all(x in text for x in words):
					print(text)
					print(sum([ord(x) for x in list(text)]))
					print((a,b,c))
					return
def CyclicalFigurateNumbers():
	func = [lambda x:x*x , lambda x:x*(3*x-1)/2 , lambda x:x*(2*x-1) , lambda x:x*(5*x-3)/2 , lambda x:x*(3*x-2)]
	perms = list(itertools.permutations(range(5)))
	for p in perms:
		l = []
		for t in range(43,200):
			triang = int(t*(t+1)/2)
			if triang % 100 < 10 or triang < 1000:
				continue
			if triang > 10000:
				break
			l.append([triang])
		counter = 1
		for x in list(p):
			for i in range(1,200):
				s = int(func[x](i))
				if s < 1000 or s >= 10000 or s%100 < 10:
					continue
				add_number(l, s, counter)
			counter+=1
			l = remove_short_lists(l, counter)
		if len(l) >= 1:
			for x in range(len(l)):
				if l[x][-1]%100==int(l[x][0]/100):
					print(sum(l[x]))

def remove_short_lists(l, n):
	li = []
	for x in l:
		if len(x) >= n:
			li.append(x)
	return li


def add_number(l, n, m):
	for x in range(len(l)):
		if len(l[x])>m:
			continue
		if n%100==int(l[x][0]/100):
			l.append([n] + l[x])
		if l[x][-1]%100==int(n/100):
			l.append([x]+[n])
	return l

def is_cube(n):
	return int(round(n**(1/3))) ** 3 == n

def CubicPermutations():
	counter=14
	d = {} 
	s = ""
	l = ['0']*15
	while True:
		counter+=1
		cube = counter ** 3
		s = ''.join(sorted(str(cube),reverse=True)) 
		l.append(s)
		if s in d:
			d[s] += 1
		else:
			d[s] = 1
		if d[s] == 5:
			print(s)
			break
	i = l.index(s)
	print(i**3)

def PowerfulDigitCounts():
	power = 1
	s = 0
	while True:
		counter = 1
		length = len(str(counter**power))
		while length <= power:
			if length == power:
				s+=1
			counter+=1
			length = len(str(counter**power))
		power+=1
		print(s)
		if s >= 49:
			break
			

def OddPeriodSquareRoots():
	odds = 0
	for s in range(1,10001):
		m = 0
		d = 1
		a = int(s**0.5)
		an = a
		l = []
		counter = 0
		while True:
			m = int(d*an-m)
			d = int((s-m**2)/d)
			if d == 0:
				break
			an = int((a+m)/d)
			if (an,m,d) in l:
				break
			l.append((an,m,d))
		if len(l)%2==1:
			odds+=1
	print(odds)

def ConvergentsOfE():
	a,b = 2,3
	n = 2
	for i in range(2,100):
		if i%3==2:
			x = n*b+a
			a = b
			b = x
			n+=2
		else:
			b = b+a
			a = b-a
	print(sum([int(i) for i in list(str(b))]))

def continued_fraction(s):
	m = 0
	d = 1
	a = int(s**0.5)
	an = a
	l = []
	l.append((an,m,d))
	li = [an]
	while True:
		m = int(d*an-m)
		d = int((s-m**2)/d)
		if d == 0:
			break
		an = int((a+m)/d)
		if (an,m,d) in l:
			break
		l.append((an,m,d))
		li.append(an)
	return li

def DiophantineEquation():
	cubes = []
	biggest = []
	d = 0
	for i in range(2,1001):
		if i**2 < 1001:
			cubes.append(i**2)
		if i in cubes:
			continue
		m,d,a = 0,1,int(math.sqrt(i))
		num1, num = 1, a
		den1, den = 0,1

		while num**2-i*den**2 != 1:
			m = int(d*a-m)
			d = int((i-m**2)/d)
			a = int(((math.sqrt(i))+m)/d)
			num2 = num1
			num1 = num
			den2 = den1
			den1 = den
			num = a*num1 + num2
			den = a*den1 + den2
		if num>d:
			biggest.append((num,i))
			d=num

	print(sorted(biggest, reverse=True)[0])

def Magic5GonRing():
	l_low = list(itertools.permutations(range(1,6)))
	l_hi = list(itertools.permutations(range(6,11)))
	sol = []
	for l in l_low:
		for p in l_hi:
			v=l[-1]+l[0]+p[-1]
			bol = True
			for x in range(4):
				if l[x]+l[x+1]+p[x] != v:
					bol=False
			if bol:
				sol.append((p,l))
	m = []
	for a,b in sol:
		x, y = list(a),list(b)
		val = 11
		i = -1
		for v in range(5):
			if x[v] < val:
				val = x[v]
				i = v
		s = ""
		for index in range(i,i-5,-1):
			if index != 4:
				s+=str(x[index]) + str(y[index+1]) + str(y[index])
			else:
				s+=str(x[index]) + str(y[0]) + str(y[index])
		if len(s) == 16:
			m.append(int(s))
	print(sorted(m, reverse=True))

	
def TotientMaximum():
	i = 1
	p = 1
	s = 2
	m,v=0,0
	primes = [1] + rwh_primes1(10**3)
	for x in range(2, len(primes)):
		s=s*primes[x]
		if s > 10**6:
			break
		p+=1
		i = bisect.bisect_left(primes, s)
		q = s//int(i-p)
		if q>m:
			m=q
			v=s
	print(v,m)

def totient(n):
	if is_prime(n):
		return n-1
	primes = rwh_primes1(int(n/2)+1)
	s = set()
	for q in primes:
		if n%q==0:
			s.add(q)
	for q in s:
		n = n*(1-(1/q))
	return int(n)

def TotientPermutation():
	least = []
	primes = rwh_primes1(int(10**3.5)*2)
	i = bisect.bisect_left(primes, int(10**3.5))-1
	q = i-1
	while i < len(primes):
		s = i
		x = primes[i]*primes[s]
		while primes[s]*x > 10**7:
			if x > 10**7:
				s-=1
				x=primes[i]*primes[s]
				continue
			y = (primes[i]-1)*(primes[s]-1)
			if sorted(list(str(x))) == sorted(list(str(y))):
				least.append((x/y,x))
			s-=1
			x=primes[i]*primes[s]
		i+=1
	while primes[q]**3 > 10**7:
		s = q
		x = primes[q]*primes[s]
		while primes[s]*x > 10**7:
			if x > 10**7:
				s-=1
				x=primes[i]*primes[s]
				continue
			y=(primes[q]-1)*(primes[s]-1)
			if sorted(list(str(x))) == sorted(list(str(y))):
				least.append((x/y, x))
			s-=1
			x=primes[q]*primes[s]
		q-=1
	print(sorted(least)[0])

def OrderedFractions():
	fracts = []
	u,v = 3,7
	i = 1
	while i*v < 10**6:
		i+=1
	i-=1
	u = u*i - 1 
	print(u)

def relative_primes(n):
	if is_prime(n):
		return []
	primes = rwh_primes1(int(n/2)+1)
	s = set()
	for q in primes:
		if n%q==0:
			s.add(q)
	return s

def CountingFractions():
	l = [0]*(10**6+1)
	s = 0
	for i in range(2,10**6+1):
		x = l[i]
		if x > 0:
			s+=x
			print(i)
			continue
		t = relative_primes(i)
		v = i
		for u in t:
			v = int(v*(u-1)/u)
		for u in t:
			y = i*u
			while y < 10**6:
				l[y]=v*int(y/i)
				y = y*u
		if not t:
			s+=i-1
		else:
			s += v
	print(s)

def CountingFractions2():
	N = 10**6+1

	a = list(range(N))
	b = [0]*N

	for p in range(2,N):
		if b[p]:
			continue
		a[p] -= 1
		for j in range(p+p,N,p):
			b[j] = 1
			a[j] -= a[j]//p
	print(sum(a)-1)

def CountingFractionsInRange():
	n1, d1, n2, d2 = 1, 3, 1, 2
	n = [0] * 12001
	for d in range(1, 12001):
		n[d] += -1*((-n2*d)//d2) + ((-n1*d)//d1) -1
		n[2*d::d] = [k-n[d] for k in n[2*d::d]]
	print(sum(n))

def factorial_sum(n):
	l = [int(i) for i in str(n)]
	fact = [1]
	for i in range(1,10):
		fact.append(i *fact[-1])
	return sum([fact[x] for x in l])

def DigitFactorialChains():
	s = 0
	for i in range(10**3,10**6):
		f = factorial_sum(i)
		l = [i]
		while f not in l:
			l.append(f)
			f = factorial_sum(f)
		if len(l)==60:
			s+=1
	print(s)

def SingularIntegerRightTriangles():
	num = 1500001
	li = [0]*num
	score = 0
	for m in range(2,int((num/2)**0.5)):
		for n in range(1,m):
			if ((n+m)%2)==1 and gcd(n,m)==1:
				a = m*m + n*n
				b = m*m - n*n
				c = 2 * m * n
				p = a+b+c
				while p < num:
					li[p]+=1
					if li[p] == 1: score+=1
					if li[p] == 2: score-=1
					p+=a+b+c
	print(score)

def CountingSummations():
	p = []
	p.append(1)
	n = 1
	while n<=100:
		i = 0
		penta = 1
		p.append(0)
		sign = [1, 1,-1,-1]
		while penta <= n:
			p[n] += sign[i%4] * p[n-penta]
			i+=1
			j = int(i/2 + 1)
			j = j if i % 2 == 0 else -1*j
			penta = int(j*(j*3-1)/2)
		n+=1
	print(p[100]-1)
	return p

def CountingPrimes():
	print("Not done")
	primes = rwh_primes(100000)

def PathSumTwoWays():
	f = open("p081_matrix.txt")
	lines = f.readlines()
	f.close()
	l = []
	c = 0
	for line in lines:
		l.append([])
		for x in line.split(","):
			l[c].append((int(x), 0))
		c+=1
	(a, b) = l[79][79]
	l[79][79] = (a, a)
	for x in range(79,-1,-1):
		for y in range(79,0,-1):
			(a,b) = l[x][y]
			(n,m) = l[x][y-1]
			(j,k) = l[x-1][y] if x>0 else (99999,1)
			if m == 0 or b+n<m:
				l[x][y-1] = (n, b+n)
			if k == 0 or b+j<k:
				l[x-1][y] = (j, b+j)
	print(l[0][0])

class node:
	def __init__(self, i, j, value, goal, prev=0):
		self.i = i
		self.j = j
		self.goal = goal
		self.value = value
		self.prev = prev
	def __eq__(self, other):
		if type(other) is node:
			return self.i == other.i and self.j == other.j
		return False
	def __lt__(self, other):
		return self.fx() < other.fx()
	def fx(self):
		return self.gx() + self.hx()
	def gx(self):
		if self.prev==0:
			return self.value
		return self.prev.gx() + self.value
	def hx(self):
		return 0
	def update(self, other):
		self.prev = other.prev

def AStar(matrix, start, goal):
	closed = []
	openSet = []
	(i, j) = start
	n = node(i, j, matrix[i][j], goal)
	openSet.append(n)
	(g1, g2) = goal
	while openSet:
		current = openSet.pop(0)
		if current.i==g1 and current.j==g2:
			return current
		closed.append(current)
		i, j = current.i, current.j
		neighbors = []
		a, b = i-1, i+1
		c, d = j-1, j+1
		if a>=0:
			neighbors.append(node(a,j,matrix[a][j],goal,current))
		if b<len(matrix):
			neighbors.append(node(b,j,matrix[b][j],goal,current))
		if c>=0:
			neighbors.append(node(i,c,matrix[i][c],goal,current))
		if d<len(matrix[0]):
			neighbors.append(node(i,d,matrix[i][d],goal,current))
		for neighbor in neighbors:
			if neighbor in closed:
				continue
			if neighbor not in openSet:
				openSet.append(neighbor)
			else:
				n = openSet.index(neighbor)
				if openSet[n].gx() > neighbor.gx():
					openSet[n].update(neighbor)

		openSet = sorted(openSet)
	print("failed")

def ShortestPath():
	f = open("p083_matrix.txt")
	lines = f.readlines()
	f.close()
	matrix = []
	c = 0
	for line in lines:
		matrix.append([])
		for x in line.split(","):
			matrix[c].append(int(x))
		c+=1
	
	n = AStar(matrix,(0,0),(79,79))
	print(n.fx())

def PathSumThreeWays():
	matrix = [ [0] + [int(y) for y in x.strip().split(",")] + [0] for x in open("p082_matrix.txt").readlines()] 
	print(AStar(matrix,(0,0),(79,81)).fx())

def SquareRootDigitalExpansion():
	x = 0
	for i in range(2,100):
		b = 5
		a = 5*i
		q = int(i**0.5)
		if q*q==i:
			continue
		while len(str(b))<108:
			if a>=b: a, b = a-b, b+10
			elif a<b: a, b = a*100, b*10-45
		l = list(str(b))
		for v in range(0,100):
			x+=int(l[v])
	print(x)

def CountingRectangles():
	j = 2
	x,y,z = 0,0,2*10**6
	for i in range(2,500):
		for j in range(i,1000):
			s = int(((i+1)*i/2)*((j+1)*j/2))
			diff = 2*10**6 - s
			if diff < 0 and diff*-1 > z:
				break
			diff = diff if diff > 0 else diff*-1
			if diff < z:
				x,y,z=i,j,diff
	print(x*y)
	print(z)

if __name__ == "__main__":
	CountingRectangles()
