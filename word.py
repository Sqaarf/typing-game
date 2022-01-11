class Word:
    def __init__(self, string):
        self.string = string
        self.length = len(string)

        if 3 <= self.length < 8:
            self.color = (0, 255, 0)  # Green = Easy
        elif 8 <= self.length < 10:
            self.color = (255, 255, 0)  # Yellow = Intermediate
        elif self.length >= 10:
            self.color = (255, 0, 0)  # Red = Hard
        else:
            self.color = None

    def __str__(self):
        """
        :return: string value of the word
        """
        return self.string
