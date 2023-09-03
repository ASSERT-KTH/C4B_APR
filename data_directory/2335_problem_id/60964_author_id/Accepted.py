def main():
    pattern = "hello"
    line = input()
    current_letter_index = 0
    for letter in line:
        if letter == pattern[current_letter_index]:
            current_letter_index += 1
            if current_letter_index == 5:
                print("YES")
                break
    else:
        print("NO")

if __name__ == "__main__":
    main()