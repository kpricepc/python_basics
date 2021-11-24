# Take user inputs
A  = int(input("Enter your first integer: "))
B  = int(input("Enter your second integer: "))

def function(A,B):
    # Verify Larger number is first, if not swap the values
    if A < B:
        A , B = B , A 
    # If no remainder, return value. Otherwise, iterate over function again with remainder
    if( A % B) == 0:
        return B
    else:
        T = A % B
        return (function(B,T))

# Print the answer
print("GCD: ", function(A, B))