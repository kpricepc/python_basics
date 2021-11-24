def setup():
    while True:
        n = input("Please enter a number, or quit to exit:")
        if n.strip() == 'quit':
            break

if __name__ == "__main__":
    try:
        setup()
    except KeyboardInterrupt:
        print("Exiting Loop")