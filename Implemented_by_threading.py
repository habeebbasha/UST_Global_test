import threading
from UST_Tests.Frequency_of_words import word_frequency
from UST_Tests.shape_square_class import Shape, Square


def calculate_word_frequency(line):
    result = word_frequency(line)
    print("Word Frequency:", result)


def calculate_shape_area():
    shape = Shape()
    print("Area of Shape:", shape.area())


def calculate_square_area(length):
    square = Square(length)
    print("Area of Square:", square.area())


def main():
    line = "which is better python 2 or python 3"
    thread1 = threading.Thread(target=calculate_word_frequency, args=(line,))

    thread2 = threading.Thread(target=calculate_shape_area)
    thread3 = threading.Thread(target=calculate_square_area, args=(5,))

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()


if __name__ == "__main__":
    main()
