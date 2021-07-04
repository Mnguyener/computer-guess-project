from random import randint

def main():

    def comp_guess():
        low = 1
        high = 10
        user_num = int(input("Provide a number.\n"))
        comp_num = randint(low, high)
        print(comp_num)

        while True:

            if comp_num > user_num:
                print("Too high.")
                high = comp_num - 1
                comp_num = randint(low, high)
                print(comp_num)
                continue
            if comp_num < user_num:
                print("Too low.")
                low = comp_num + 1
                comp_num = randint(low, high)
                print(comp_num)
                continue
            else:
                print("Correct")
                break

    comp_guess()
if __name__ == '__main__':
    main()