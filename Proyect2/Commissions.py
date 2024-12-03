name = input("Please, tell me your name: ")
sales = int(input("Tell me your total sales for the month: "))

commission = round(sales * 13 / 100, 2)

print(f"Hello {name}, your commissions for this month are ${commission}")