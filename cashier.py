"""
author: https://github.com/alif-arrizqy
topics: simple cashier app
"""


class cashier:
    price_black_coffee = 20000
    price_white_latte = 26000
    price_hzlt_latte = 24000
    price_roti_bakar = 6000
    price_singkong_goreng = 7000
    price_tempe_mendoan = 5000

    def coffee():
        print("=============================")
        print("|     coffee       | price  |")
        print("=============================")
        print("|1. black coffee   | 20.000 |")
        print("|2. white latte    | 26.000 |")
        print("|3. hazelnut latte | 24.000 |")
        print("============================")

    def side():
        print("=================================")
        print("|       side        | price (IDR)|")
        print("=================================")
        print("|1. roti bakar      |   6.000    |")
        print("|2. singkong goreng |   7.000    |")
        print("|3. tempe mendoan   |   5.000    |")
        print("=================================")
    
    def next_side():
        print("1. cash")
        print("2. choose side")
    
    def next_coffee():
        print("1. cash")
        print("2. choose side")


    print("=======================================")
    print("Welcome to Warkop Pengkolan")
    print("=======================================\n")
    print("Choose your menu:")
    print("1. Coffee")
    print("2. Side")
    print("*type the number of menu")
    menu = input("your menu: ")
    menu = int(menu)
    if menu == 1:
        coffee()
        coffees = input("menu coffee: ")
        coffees = int(coffees)
        if coffees == 1:
            next_side()
            next = input("choose the number: ")
            next = int(next)
            if next == 1:
                ammount = input("Enter purchase amount: ")
                ammount = int(ammount)
                total = ammount * price_black_coffee
                print(f"total: {total}")
            elif next == 2:
                side()
        elif coffees == 2:
            next_side()
            next = input("choose the number: ")
            next = int(next)
            if next == 1:
                ammount = input("Enter purchase amount: ")
                ammount = int(ammount)
                total = ammount * price_white_latte
                print(f"total: {total}")
            elif next == 2:
                side()
        elif coffees == 3:
            next_side()
            next = input("choose the number: ")
            next = int(next)
            if next == 1:
                ammount = input("Enter purchase amount: ")
                ammount = int(ammount)
                total = ammount * price_hzlt_latte
                print(f"total: {total}")
            elif next == 2:
                side()

    elif menu == 2:
        side()
        side = input("menu side: ")
        side = int(side)
        if side == 1:
            next_coffee()
            next = input("choose the number: ")
            next = int(next)
            if next == 1:
                ammount = input("Enter purchase amount: ")
                ammount = int(ammount)
                total = ammount * price_roti_bakar
                print(total)
        elif side == 2:
            next_coffee()
            next = input("choose the number: ")
            next = int(next)
            if next == 1:
                ammount = input("Enter purchase amount: ")
                ammount = int(ammount)
                total = ammount * price_singkong_goreng
                print(total)
        elif side == 3:
            next_coffee()
            next = input("choose the number: ")
            next = int(next)
            if next == 1:
                ammount = input("Enter purchase amount: ")
                ammount = int(ammount)
                total = ammount * price_tempe_mendoan
                print(total)
    else:
        print("not found")


if __name__ == "__main__":
    cashier()
