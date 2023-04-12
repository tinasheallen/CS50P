def main():

    newsms = convert(input("Enter yr message here :"))
    print(newsms)




def convert(str):
    op = str.replace(":)", '🙂').replace(":(", '🙁')
    return op


main()