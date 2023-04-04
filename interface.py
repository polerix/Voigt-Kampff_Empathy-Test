import os

#Seems OK for what we need.

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_header():
    clear_screen()
    print("""+========================================================+
|            VOIGHT-KAMPFF MACHINE (2022)                |
|                 NEXUS-6 EDITION                         |
|         Detecting Replicants since 2019                 |
+========================================================+\n""")


def show_question(question, time):
    clear_screen()
    print("  " + question + "\n")
    print("  Time to answer: {0:02d}:{1:02d}".format(time // 60, time % 60))
    print("  Press -> to advance to the next question.\n")


def show_results(co2, o2, iris):
    clear_screen()
    print("  +============================+")
    print("  |  SENSOR READINGS           |")
    print("  +============================+")
    print("  |  CO2:  {:<18}|".format(co2))
    print("  |  O2:   {:<18}|".format(o2))
    print("  |  IRIS: {:<18}|".format(iris))
    print("  +============================+\n")


def show_error(msg):
    clear_screen()
    print("  Error: {}\n".format(msg))
