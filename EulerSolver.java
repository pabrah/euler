/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package eulersolver;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author A53300
 */
public class EulerSolver {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        //System.out.println(multiplesOf3And5(1000)+"");
        //long sum = primeFactor(600851475143L);
        //print("" + sum);
        //print(palindrome());
        //print(evenlyDivisible(20)+"");
        //print(squareDiff(100) + "");
        //print(primeNumber(10001)+"");
        //print(adjecentDigits(13)+"");
        //print(pythagorianTriplet(1000)+"");
        //print(sumPrimesUnder(2000000) + "");
        //print(productAdjecentNumers(4));
        //print(highlyDivisibleTriangular(500) +"");
        //print(largeSum());
        print(gridMovement(20)+"");
    }
    
    public static long gridMovement(int n)
    { 
        long sum = 2;

        for(int i = 1; i<n; i++)
        {
            long product = 1L;
            long divider = 1L;
            for(int j=1;j<=i;j++)
            {
                product *= n-j+1;
                divider *= j;
            }
            sum += (product/divider)*(product/divider);
        }
        return sum;
    }
    
    private static String largeSum()
    {
        try{
            File f = new File("src\\eulersolver\\largeSum.txt");
            BufferedReader in = new BufferedReader(new FileReader(f));
            String line = in.readLine();
            List<BigInteger> b = new ArrayList<>();
            while(line != null)
            {
                BigInteger big = new BigInteger(line);
                b.add(big);
                line = in.readLine();
            }
            while(b.size()>1)
            {
                List<BigInteger> helper = new ArrayList();
                int size = b.size();
                for(int i = 0; i < (int)(size+1)/2; i++)
                {
                    if(i == size-i-1)
                        helper.add(b.get(i));
                    else
                        helper.add(b.get(i).add(b.get(size-i-1)));
                }
                print(helper.size());
                b = helper;
            }
            BigInteger result = b.get(0);
            return result.toString();
            /*for(int i = 1; i < b.size();i++)
            {
                result = result.add(b.get(i));
            }
            return result.toString();*/
        }
        catch(Exception e)
        {
            e.printStackTrace();
            return "Exception ";
        }
    }
    
    private static long highlyDivisibleTriangular(int n)
    {
        int counter = 1;
        long sum = 0;
        List divisors = new ArrayList();
        for(int i = 0; i<n; i++)
        {
            sum+=counter++;
        }
        while(divisors.size()<n)
        {
            sum+=counter++;
            divisors = new ArrayList();
            int x = 1;
            while(!divisors.contains(x) && x<Math.sqrt(sum))
            {
                if(sum%x==0){
                    divisors.add(x);
                    divisors.add(sum/x);
                }
                x++;
            }
            print(divisors.size()+"");
        }
        return sum;
    }
    
    private static int productAdjecentNumers(int n)
    {
        String s = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08\n" +
            "49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00\n" +
            "81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65\n" +
            "52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91\n" +
            "22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80\n" +
            "24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50\n" +
            "32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70\n" +
            "67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21\n" +
            "24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72\n" +
            "21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95\n" +
            "78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92\n" +
            "16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57\n" +
            "86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58\n" +
            "19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40\n" +
            "04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66\n" +
            "88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69\n" +
            "04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36\n" +
            "20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16\n" +
            "20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54\n" +
            "01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48";
        String[] strArray = s.split("\n");
        String[][] strArray2 = new String[20][20];
        for(int i = 0; i<strArray.length;i++)
        {
            strArray2[i] = strArray[i].split(" ");
        }
        int[][] numArray = new int[20][20];
        for(int i = 0; i < strArray.length; i++)
        {
            for(int j=0; j < strArray2[i].length;j++)
            {
                
                numArray[i][j] = Integer.parseInt(strArray2[i][j]);
                //print(numArray[i][j]);
            }
        }
        int max = 0;
        for(int i = 0; i < strArray.length-n;i++)
        {
            for(int j=0; j<numArray[i].length-n;j++)
            {
                //print(numArray[i][j]);
                int down = 1;
                int right = 1;
                int diagonal = 1;
                int diagUp = 1;
                for(int x = 0; x<n;x++)
                {
                    down *= numArray[i+x][j];
                    right *= numArray[i][j+x];
                    diagonal *= numArray[i+x][j+x];
                    if(i+n-x>=0)
                        diagUp *= numArray[i+n-x][j+x];
                    //print(down);
                }
                if(down>max){
                    max = down;
                  //  print(max);
                }
                if(right>max){
                    max=right;
                    //print(max);
                }
                if(diagonal>max){
                    max = diagonal;
                    //print(max);
                }
                if(diagUp>max){
                    max = diagUp;
                }
            }
        }
        return max;
    }
    
    private static long sumPrimesUnder(int n)
    {
        int[] primArray = new int[n];
        for(int i =0;i<primArray.length;i++)
            primArray[i]=0;
        int x = 2;
        long sum = 0;
        while (x < n)
        {
            int i = 0;
            while(primArray[i] != 0){
                if(x%primArray[i]==0)
                {
                    i=0;
                    x++;
                }
                else
                    i++;
            }
            if(x>n)
                break;
            sum += x;
            primArray[i]=x++;
            print(primArray[i]);
        }
        return sum;
    }
    
    private static String pythagorianTriplet(int n){
        double c = 0;
        for(int b=1;b<n;b++)
        {
            for(int a=0;a<b;a++){
                c = Math.sqrt(a*a + b*b);
                if(a+b+c==n)
                    return "a:" + a + " b:" + b + " c:" + c + "a*b*c:" + a*b*c;
            }
        }
        return "";
    }
    
    private static long adjecentDigits(int n){
        String s = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450";
        char[] str = s.toCharArray();
        long max = 0;
        for(int i=0;i<s.length()-n;i++){
            long product = 1;
            for(int j=i;j<i+n;j++){
                product *= (int)str[j]-(int)'0';
            }
            if(product > max)
                max = product;
            
        }
        return max;
    
    }    
    private static int primeNumber(int n){
        int[] primArray = new int[n];
        for(int i =0;i<n;i++)
            primArray[i]=0;
        primArray[0]=2;
        primArray[1]=3;
        primArray[2]=5;
        int counter = 3;
        int x = 6;
        while(counter<n){
            for(int i = 0; i<primArray.length;i++){
                int num = 1;
                if(primArray[i]!=0 ){
                    num = primArray[i];
                    int s = x%num;
                    if(s==0){
                        x++;
                        i=0;
                    }
                }
                else
                    break;
            }
            primArray[counter++]=x;
            //print(counter + ": " + primArray[counter-1]);
        }
        return primArray[n-1];
    }
    
    private static int squareDiff(int n){
        int sumSquare=0;
        int squareSum=0;
        for(int i=1;i<=n;i++){
            sumSquare+=i*i;
            squareSum+=i;
        }
        squareSum=squareSum*squareSum;
        return sumSquare-squareSum;
    }
    
    private static int evenlyDivisible(int m){
        int i=1;
        while(true)
        {
            boolean b=true;
            for(int x=1;x<=m;x++)
            {
                if(i%x!=0){
                    b=false;
                    break;
                }
                
            }
            if(!b)
                i++;
            else
                return i;
        }
 
    }
    
    private static int multiplesOf3And5(int max){
        int sum = 0;
        for(int i = 1; i<max;i++){
            if(i%3==0 || i%5==0)
                sum += i;
        }
        return sum;
    }
    
    private static int fibonacciSum(int x, int y){
        if((x+y)%2==0)
            return x+y+fibonacciSum(y, x+y);
        if((x+y)<4000000)
            return fibonacciSum(y, x+y);
        return 0;
    }
    
    private static long primeFactor(long x){
        long largest = 0;
        for(long i=1; i<=x;i++)
        {
            if(x%i==0){
                largest = i;
                x=x/i;
                i=1;
            }
        }
        return largest;
    }
    
    private static String palindrome(){
        String max="";
        int p=0;
        for(int i=999;i>99;i--){
            if(i*999<p)
                return max;
            for(int j=999;j>99;j--)
            {
                String pal = i*j + "";
                char[] chars = pal.toCharArray();
                String rev = "";
                for(int x =chars.length-1; x>=0;x--)
                {
                    rev += chars[x];
                }
                if(pal.equals(rev)){
                    if(i*j>p){
                        max = pal;
                        p=i*j;
                    }
                }
                    
            }
        }
        return max;
    }
    
    private static void print(int i){
        print(i+"");
    }
    
    private static void print(String s)
    {
        System.out.println(s);
    }
}
