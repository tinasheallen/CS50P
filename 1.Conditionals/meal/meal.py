def main():
    time = input("What time is it? ").strip()
    converted_time = convert(time)

    if 7 <= converted_time < 9:
        print("breakfast time")
    elif 12 <= converted_time < 14:
        print("lunch time")
    elif 18 <= converted_time < 20:
        print("dinner time")

def convert(time):
    hr, mins = map(float, time.split(":"))
    return hr + mins / 60

if __name__ == "__main__":
    main()
