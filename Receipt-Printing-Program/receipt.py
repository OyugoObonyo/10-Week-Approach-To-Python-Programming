"""
A receipt printing program
"""
company_name = "LAKEFRONT STORES"
company_address = "1234 FREEDOM STREET"
message = f"Thanks for shopping at {company_name}!"
prod1, price1 = "Pen", 10
prod2, price2 = "Pencil", 10
prod3, price3 = "Graph Book", 40
total_price = price1 + price2 + price3

print("*" * 60)
print("\t\t{}".format(company_name.title()))
print("\t\t{}".format(company_address.title()))
print("=" * 60)
print("\tProduct Name\t\tProduct Price")
print(f"\t{prod1}\t\t\t{price1}")
print(f"\t{prod2}\t\t\t{price2}")
print(f"\t{prod3}\t\t{price3}")
print("*" * 60)
print(f"\t\t\t\tTOTAL:{total_price}")
print("=" * 60)
print("\n")
print(f"\t{message}")
print("\n")
print("_" * 60)
