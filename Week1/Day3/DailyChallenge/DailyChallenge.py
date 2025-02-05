#Challenge 1

word = input("Enter a word: ")
print("You entered:", word)

letter_dict = {}

for index, letter in enumerate(word):
    if letter not in letter_dict:
        letter_dict[letter] = []
    letter_dict[letter].append(index)

print(letter_dict)


#Challenge 2
def affordable_items(items_purchase, wallet):
    wallet = int(wallet.replace("$", "").replace(",", ""))
    affordable = []

    for item, price in items_purchase.items():
        price = int(price.replace("$", "").replace(",", ""))
        if price <= wallet:
            affordable.append(item)

    affordable.sort()
    
    if affordable:
        return affordable
    else:
        return "Nothing"

# Example 1
items_purchase = {
    "Water": "$1",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20"
}
wallet = "$300"
print(affordable_items(items_purchase, wallet))

# Example 2
items_purchase = {
    "Apple": "$4",
    "Honey": "$3",
    "Fan": "$14",
    "Bananas": "$4",
    "Pan": "$100",
    "Spoon": "$2"
}
wallet = "$100"
print(affordable_items(items_purchase, wallet))

# Example 3
items_purchase = {
    "Phone": "$999",
    "Speakers": "$300",
    "Laptop": "$5,000",
    "PC": "$1200"
}
wallet = "$1"
print(affordable_items(items_purchase, wallet))

