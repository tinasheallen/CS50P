def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    cap = d.replace('$', '')
    return float(cap)


def percent_to_float(p):
    tru = p.replace('%', '')
    tex = float(tru) / 100

    return (tex)


main()
