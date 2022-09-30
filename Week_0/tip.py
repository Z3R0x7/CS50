def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(
        input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# use the replace() method and convert the values to float


def dollars_to_float(d):
    # TODO
    d = d.replace('$', '')
    d = float(d)
    return d

# use the replace() mmethod and convert them to float while calculating the percentage


def percent_to_float(p):
    # TODO
    p = p.replace('%', '')
    p = float(p)
    p = p/100
    return p


main()
