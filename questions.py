import time


def ask_questions():
    with open("questions.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("{"):
                time_str = line.split("}")[0].strip("{").strip()
                question = line.split("}")[1].strip()
                print_question(question)
                wait_time = int(time_str.split(":")[0]) * 60 + int(time_str.split(":")[1])
                time.sleep(wait_time)
            else:
                print_question(line.strip())


def print_question(question):
    print("+{}+".format("-" * (len(question) + 2)))
    print("| {} |".format(question))
    print("+{}+".format("-" * (len(question) + 2)))
