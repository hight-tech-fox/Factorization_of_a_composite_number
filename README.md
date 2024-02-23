# Factorization_of_a_composite_number
The program checks a number for primality using the Rabin-Miller test. If the number is composite, a complete factorization of the number is performed using the rho-Pollarad method, and the operating time is also measured.

  <h2>Description of the algorithm</h2>
We read the number n, check it for primality, if the number is prime, output the message “n is a prime number” to the file, otherwise we perform a complete factorization of the number n, output the factorization and the running time of the program.
  <h2>Description of the software solution</h2>
  The software solution contains the following functions:
  <h3>def generate_random_number(n):</h3>
  Accepts for entry: Integer n
  What is he doing? Generates a random number in the range [1; n-1)
  Returns: Generated number
  <h3>def gcd(a, b):</h3>
    Accepts for entry: Integers a and b
    What is he doing? Finds GCD(a, b)
    Returns: GCD(a, b)
  <h3>def f(x):</h3>
   Accepts for entry: x
   What is he doing? Counts x**2 + 1
   Returns: Returns the found value f(x)
    
