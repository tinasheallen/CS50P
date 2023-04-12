user_answer = input("What is the answer to the great Question of Life, the Universe, and Everything? ").lower().strip()

match user_answer:
    case "42" | "forty-two" | "forty two":
        print("Yes")

    case _:
        print("No")