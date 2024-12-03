def perfume_numbers():
    for n in range(1, 10000):
        yield f"P - {n}"


def pharmacy_numbers():
    for n in range(1, 10000):
        yield f"F - {n}"


def cosmetics_numbers():
    for n in range(1, 10000):
        yield f"C - {n}"


p = perfume_numbers()
f = pharmacy_numbers()
c = cosmetics_numbers()


def decorator(section):
    print("\n" + "*" * 23)
    print("Your number is:")
    if section == "P":
        print(next(p))
    elif section == "F":
        print(next(f))
    else:
        print(next(c))
    print("Please wait, you will be served shortly")
    print("*" * 23 + "\n")
