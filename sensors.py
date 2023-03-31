import time
import random


def read_co2():
    return round(random.uniform(0.0, 1.0) * 1000, 2)


def read_o2():
    return round(random.uniform(0.0, 1.0) * 100, 2)


def read_iris():
    return random.choice(["green", "blue", "brown", "hazel"])


def read_sensors():
    co2 = read_co2()
    o2 = read_o2()
    iris = read_iris()
    return co2, o2, iris


def update_sensor_data():
    while True:
        with open("co2.txt", "w") as f:
            f.write(str(read_co2()))
        with open("o2.txt", "w") as f:
            f.write(str(read_o2()))
        with open("iris.txt", "w") as f:
            f.write(str(read_iris()))
        time.sleep(1)
