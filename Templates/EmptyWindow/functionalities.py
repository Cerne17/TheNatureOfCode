def map(number, currentMin, currentMax, desiredMin, desiredMax):
    """
    This function maps a number contained in a specific range to a new custom range
    (number-currentMin)/(currentMax-currentMin) = (newNumber-desiredMin)/(desiredMax-desiredMin)
    """
    newNumber = (number-currentMin)/(currentMax-currentMin)*(desiredMax-desiredMin)+desiredMin
    return newNumber


class Slider:
    def __init__(self, SCREEN, title, currentValue, minValue, maxValue, position, foregroundColor, backgroundColor):
        self.SCREEN = SCREEN
        self.title = title
        self.width = 250
        self.height = 30
        self.minValue = minValue
        self.maxValue = maxValue
        self.margin = 10
        self.position = position
        self.filledPart = (currentValue - minValue) * width / (maxValue - minValue)
        self.background = pygame.Rect(self.position[0], self.position[1], self.width, self.height)
        self.foreground = pygame.Rect(self.position[0], self.position[1], self.filledPart, self.height)
        self.Font = pygame.font.SysFont('Arial',  30)
        self.text = self.Font.render(name, True, (255, 255, 255))

    def draw(self, currentValue):
        self.filledPart = (currentValue - self.minValue) * self.width / (self.maxValue - self.minValue)
        self.foreground = pygame.Rect(self.position[0], self.position[1], self.filledPart, self.height)
        pygame.draw.rect(self.SCREEN, self.backgroundColor, self.background)
        pygame.draw.rect(self.SCREEN, self.foregroundColor, self.foreground)
        SCREEN.blit(text, (position[0]+width+margin, position[1]))


if __name__ == "__main__":
    print(map(10, 0, 100, 32, 212))
    print(map(30, 0, 100, 273, 373))
    print(map(30, 0, 100, 20, 120))

