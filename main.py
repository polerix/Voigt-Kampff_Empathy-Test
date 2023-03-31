import threading
from sensors import Sensor
from interface import Interface
from utils import load_questions, load_config
from input import Input
from results import Results
from questions import Questions


def main():
    # Load questions, config and create objects
    questions = load_questions()
    config = load_config()
    sensor = Sensor(config)
    results = Results(config)
    interface = Interface(config)
    input_manager = Input(interface)

    # Create and start threads
    sensor_thread = threading.Thread(target=sensor.run, args=(results,))
    interface_thread = threading.Thread(target=interface.run, args=(questions,))
    input_thread = threading.Thread(target=input_manager.run)

    sensor_thread.start()
    interface_thread.start()
    input_thread.start()

    # Wait for threads to finish
    sensor_thread.join()
    interface_thread.join()
    input_thread.join()

if __name__ == "__main__":
    main()
