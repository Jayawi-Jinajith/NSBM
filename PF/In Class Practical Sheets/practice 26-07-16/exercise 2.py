

# Field - Gaming
# Parameters - Name | Release year | Price

names = []
release_years = []
prices = []

for i in range(5):
    nm = input(f"Game {i+1:>2} - Name : ")
    names.append(nm)

    ry = int(input(f"{" "*9} Release Year: "))
    release_years.append(ry)

    prc = float(input(f"{" "*9} Price (USD): "))
    prices.append(prc)

    print()

print(f"{" "*2} {"Game":^15} {"Release Year"}      {"Price (USD)"}")

for j in range(5):
    print(f"{j+1:2} {names[j]:^15} {release_years[j]:^12} ---- {prices[j]:6,.2f}")


    