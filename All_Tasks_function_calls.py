from UST_Tests.Frequency_of_words import word_frequency
from UST_Tests.shape_square_class import Shape, Square


def main():
    line = "which is better python 2 or python 3"
    result = word_frequency(line)
    print("Word Frequency:", result)

    shape = Shape()
    print("Area of Shape:", shape.area())

    square = Square(5)
    print("Area of Square:", square.area())


if __name__ == "__main__":
    main()
