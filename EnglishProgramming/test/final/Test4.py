#1
def menu(**menus):
    print("=== dictionary ===")
    for i in menus:
        print(f"{i}: {menus[i]}")
    return menus

#2
def cal(menu):
    print("\n=== New price ===")
    for i in menu:
        price = f"{str(int(menu[i]*0.8))[:-3]},{str(int(menu[i]*0.8))[-3:]}"
        print(f"{i}: {price} won")

a = menu(Americano = 5000, Latte = 6500, Einspanner = 8500)
cal(a)