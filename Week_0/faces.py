def main():
    txt = input("enter the string: ")
    convert(txt)


def convert(face):
    face = face.replace(":)", "🙂")
    face = face.replace(":(", "🙁")
    return print(face)


main()
