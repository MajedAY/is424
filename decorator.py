x = int(input("Enter a number of repetitions: "))


def announce(f):
    def wrapper():

        iteration = 0
        while True:
            if x == iteration:
                break
            iteration += 1
            print("About to run the function", iteration)
            f()
            print("Done with the function", iteration)

    return wrapper


@announce
def hello():
    print("Hello")


hello()
