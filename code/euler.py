def bigIntSum(n):
   l = 1L
   for x in range(0,n):
      l *= 2
   print(l)
   li = [int(x) for x in list(str(l))]
   print(sum(li))



if __name__ == "__main__":
    bigIntSum(1000)
