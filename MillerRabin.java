public class Primo{
    public static void main(String[] args) {
        int k = 4; //iterations
        System.out.println("Todos os primos menores que 100:\n");
        for (int i = 1; i < 100; i++)
            if (isPrime(i, k))
                System.out.println(i);

    }
    // function to do modular exponentiation, returns (x^y) % p
     static int modularExp(int x, int y, int p) {
        int result = 1; // Initialize result
        x = x % p;   // Update x if it is more than or
                    // equal to p
        while (y > 0){
            // If y is odd, multiply x with result
            if ((y & 1) == 1)
                result = (result * x) % p;
            // y must be even now
            y = y >> 1; // y = y/2
            x = (x * x) % p;
        }
        return result;
    }
    //returns true if n is probably prime.
    static boolean millerTest (int d, int n){
        // d is an odd number such that d*2<sup>r</sup> = n-1
        // for some r >= 1
        int a = 2 + (int)(Math.random() % (n - 4));
        int x = modularExp(a, d, n);
        if (x == 1 || x == n-1)
            return true;
        while (d != n-1)
        {
            x = (x * x) % n;
            d *= 2;

            if (x == 1)	 return false;
            if (x == n-1) return true;
        }
        // Return composite
        return false;
    }
    //odd integer to be tested for primality, Miller-Rabin test
    // It returns false if number is composite and returns true if number
    // is probably prime. k is an input parameter that determines
    // accuracy level. Higher value of k indicates more accuracy.
    static boolean isPrime(int number, int k){
        if (number <= 1 || number == 4)
            return false;
        if (number <= 3) return true;

        int d = number -1;
        while (d % 2 == 0)
            d /= 2;
        // Iterate given number of 'k' times
        for (int i = 0; i < k; i++)
            if (!millerTest(d, number))
                return false;
        return true;

    }
}

