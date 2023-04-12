def main():
    greet = input("Please enter your greeting: ").strip().lower()

    if "hello" in greet:
        print("$0")

    elif has_h(greet):
        print("$20")

    else:
        print("$100")


def has_h(greet):
    return greet.startswith('h') and greet != "hello"



main()