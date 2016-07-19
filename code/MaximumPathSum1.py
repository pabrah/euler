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


if __name__ == "__main__":
	QuadraticPrimes()
