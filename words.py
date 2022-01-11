from word import Word


class Words:
    def __init__(self):
        self.words = []

    def parse(self):
        """
        read every line of words_alpha.txt and store them in the words array
        """
        with open('./words_alpha.txt') as f:
            for line in f:
                if len(line) > 3:  # To get meaningful values
                    self.words.append(Word(line.strip('\n')))  # Remove \n character at the end of the words

    def colorTotal(self):
        """
        Listing total of words by difficulty for curiosity’s sake
        """
        cnt = [0, 0, 0]
        for word in self.words:
            if word.color == (0, 255, 0):
                cnt[0] += 1
            elif word.color == (255, 255, 0):
                cnt[1] += 1
            elif word.color == (255, 0, 0):
                cnt[2] += 1
        print(f"Easy : {cnt[0]}; Intermediate : {cnt[1]}; Hard : {cnt[2]}")

    def __str__(self):
        """
        :return: string value of the list of words
        """
        for word in self.words:
            print(word, endl=' ')
