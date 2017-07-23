class Solution(object):
    def findWords(self, words):

        filtered_words = []

        row_map = self.construct_row_map()

        for word in words:
            lowercase_word = word.lower()

            if self.word_in_row(lowercase_word, row_map):
                filtered_words.append(word)

        return filtered_words

    def word_in_row(self, lowercase_word, row_map):

        for row in row_map:
            contained_in_row = True

            for char in lowercase_word:
                if char not in row_map[row]:
                    contained_in_row = False
                    break

            if contained_in_row:
                return True

        return False

    def construct_row_map(self):

        row_map = dict()

        row_map[0] = set(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'])
        row_map[1] = set(['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'])
        row_map[2] = set(['z', 'x', 'c', 'v', 'b', 'n', 'm'])

        return row_map