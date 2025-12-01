"""Solution for puzzle 2"""

def turn(val: int, direction: str, steps: int):
    """
    Turns the dial.
    """
    new_val = 0
    zero_count = 0

    if direction == "R":
        new_val = (val + steps) % 100
        zero_count += int((val + steps) / 100)
    elif direction == "L":
        new_val = (val - steps) % 100
        zero_count += int((val - steps) / 100)

    if new_val == 0:
        zero_count += 1
    return new_val, zero_count

def main():
    """
    Reads the document and iterates through it - every time it hits 0 a counter is incremented.
    """
    file_path = "input_eg.txt"
    val = 50
    password = 0

    print("The dial starts by pointing at", val)

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            direction = line[0]
            steps = int(line[1:])

            val, zero_count = turn(val, direction, steps)
            print("Rotates by", line, "->", val)
            password += zero_count
            print(password)

    print("Number of zeroes:", password)

if __name__ == "__main__":
    main()
