# Functions with Outputs

def format_name(f_name, l_name):
    """
      :type f_name: str
      :type l_name: str

      Take a first and last name and format it
      to return the title case version of the name.
    """
    if f_name.strip() == "" or l_name.strip() == "":
        return "You didn't provide valid inputs."  # Be careful, return -> None

    formatted_f_name = f_name.strip().title()
    formatted_l_name = l_name.strip().title()

    return f"{formatted_f_name} {formatted_l_name}"


name = input("What is your first name? ")
last_name = input("What is your last name? ")

print(f"Result : {format_name(name, last_name)}")
