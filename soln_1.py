"""Solution for puzzle 1"""

def turn(val: int, direction: str, steps: int) -> int:
    """
    Turns the dial.
    """
    new_val = 0
    if direction == "R":
        new_val = (val + steps) % 100
        # if new_val > 99:
        #     new_val -= 100
    elif direction == "L":
        new_val = (val - steps) % 100
        # if new_val < 0:
        #     new_val += 100
    return new_val

def main():
    """
    Reads the document and iterates through it - every time it hits 0 a counter is incremented.
    """
    password = 0
    file_path = "input.txt"
    val = 50

    print("The dial starts by pointing at", val)

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            direction = line[0]
            steps = int(line[1:])

            val = turn(val, direction, steps)
            print("Rotates by", line, "->", val)

            if val == 0:
                password += 1

    print("Number of zeroes:", password)

if __name__ == "__main__":
    main()
