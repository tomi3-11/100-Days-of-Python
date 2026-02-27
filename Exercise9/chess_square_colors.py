def main():
#    column = int(input("Column: "))
#    row = int(input("Row: "))
#
#    print(chess_colors(column, row))

    assert getChessSquareColor(1, 1) == 'white'
    assert getChessSquareColor(2, 1) == 'black'
    assert getChessSquareColor(1, 2) == 'black'
#    assert getChessSquareColor(8, 8) == 'white'
    assert getChessSquareColor(0, 8) == ''
    assert getChessSquareColor(2, 9) == ''


def getChessSquareColor(column, row):
    if column > 7:
        return ''
    if row > 7:
        return ''
    if column % 2 != 0 and row % 2 != 0:
        return "white"
    if column % 2 == 0 and row % 2 == 0:
        return "white"
    if ((column % 2 != 0 and row % 2 == 0) or (column % 2 == 0 and row % 2 != 0)):
        return "black"


if __name__ == "__main__":
    main()
