import os

def read_file(filename):
    """Read the contents of a file."""
    with open(filename, "r") as f:
        return f.read().strip()

def write_file(filename, contents):
    """Write contents to a file."""
    with open(filename, "w") as f:
        f.write(contents)

def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")
    
def get_input(prompt, choices):
    """Get user input and validate it against a list of choices."""
    while True:
        choice = input(prompt).strip()
        if choice.lower() in choices:
            return choice.lower()
        print("Invalid choice, please try again.")

def format_time(seconds):
    """Convert seconds to a formatted time string."""
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
