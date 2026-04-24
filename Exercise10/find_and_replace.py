def main():
#    text = "The fox"
#    oldText = "fox"
#    newText = "dog"
#
#    print(findAndReplace(text, oldText, newText))
    assert findAndReplace('The fox', 'fox', 'dog') == 'The dog'
    assert findAndReplace('fox', 'fox', 'dog') == 'dog'
    assert findAndReplace('Firefox', 'fox', 'dog') == 'Firedog'
    assert findAndReplace('foxfox', 'fox', 'dog') == 'dogdog'
    assert findAndReplace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.'


def findAndReplace(text, oldText, newText):
    replacedText = ""

    n = len(text)
    oldTextlen = len(oldText)

    i = 0
    while i < n:
        if text[i:i + oldTextlen] == oldText:
            replacedText += newText
            i+= oldTextlen
        else:
            replacedText += text[i]
            i+=1

    return replacedText


if __name__ == "__main__":
    main()
