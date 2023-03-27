 # Return the GCD of a and b using Euclid's Algorithm
def gcd(a, b):
   
    while a != 0:
        a, b = b % a, a
    return b

# Returns the modular inverse a and b using the Extended Euclidean Algorithm
def xgdc(a, m):

    # Check if a and m are relative prime
    if gcd(a, m) != 1:
        return None 

    # Calculate the modular inverse using the Extended Euclidean Algorithm:
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 
        v1, v2, v3, u1, u2, u3  = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m