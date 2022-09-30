# call the main function to convert the string
def main():
    txt = input("enter the string: ")
    convert(txt)

# use the .replace() method on the string once the convert function is called


def convert(face):
    face = face.replace(":)", "🙂")
    face = face.replace(":(", "🙁")
    return print(face)


main()
