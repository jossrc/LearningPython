# Functions with Outputs

def format_name(f_name, l_name):
    formatted_f_name = f_name.strip().title()
    formatted_l_name = l_name.strip().title()

    return f"{formatted_f_name} {formatted_l_name}"


print(format_name("JoSE", "ROBles"))
