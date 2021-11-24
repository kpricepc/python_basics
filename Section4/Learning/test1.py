def functionA():
    print("Function A")

def functionB():
    print("Function B")

print("Not in Function")

if __name__ == '__main__':
    print("Print the main function")
    try:
        functionA()
    except:
        print("Exit")