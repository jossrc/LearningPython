guess_list: list[str] = []

with open("Input/Names/invited_names.txt") as invited_names:
    names: list[str] = invited_names.readlines()

guess_list.extend([name.strip() for name in names])

with open("Input/Letters/starting_letter.txt") as model_letter:
    content = model_letter.read()
    for invited in guess_list:
        with open(f"Output/ReadyToSend/letter_for_{invited}.txt", mode="w") as letter:
            updated_content = content.replace("[name]", invited)
            letter.write(updated_content)
