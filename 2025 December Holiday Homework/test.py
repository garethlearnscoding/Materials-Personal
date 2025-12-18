def inputPuzzle():
    puzzle = []
    for i in range(9):
        while True:
            cur_row = input(f"Row {i+1} | Enter answer: ")
            cur_row = [int(i) for i in cur_row.split(" ")]
            print(len(cur_row))
            print(set(cur_row))
            if len(cur_row) != 9:
                continue
            print(set(cur_row).issubset({1,2,3,4,5,6,7,8,9}))
            if set(cur_row).issubset({1,2,3,4,5,6,7,8,9}):
                break
        puzzle.append(cur_row)

example1 = inputPuzzle()