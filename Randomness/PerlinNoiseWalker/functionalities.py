import pygame

def map(number, currentMin, currentMax, desiredMin, desiredMax):
    """
    This function maps a number contained in a specific range to a new custom range
    (number-currentMin)/(currentMax-currentMin) = (newNumber-desiredMin)/(desiredMax-desiredMin)
    """
    newNumber = (number-currentMin)/(currentMax-currentMin)*(desiredMax-desiredMin)+desiredMin
    return newNumber



if __name__ == "__main__":
    print(map(10, 0, 100, 32, 212))
    print(map(30, 0, 100, 273, 373))
    print(map(30, 0, 100, 20, 120))

