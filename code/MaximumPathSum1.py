import math 
import bisect
import itertools
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

def ReciprocalCycles(d=1000):
	for x in range(7, d, 2):
		if x%3==0 or x%5==0:
			continue
		r = str(1/x).replace("0.","")
		print(r)

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

def CoinSum(n=200):
	print("Not done")

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

if __name__ == "__main__":
	SubStringDivisibility()
