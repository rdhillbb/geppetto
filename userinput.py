def getInput() -> str:
    print("Paste or key in code (type '[Return] ...' or '.done' when done):")
    user_input = ''
    try:
        while True:
            line = input()
            if line.strip() == '...':
                break
            if line == ".done":
                break
            user_input += line + '\n'
    except KeyboardInterrupt:
        print("\nUser interrupted the input process.")

    return user_input.strip()
