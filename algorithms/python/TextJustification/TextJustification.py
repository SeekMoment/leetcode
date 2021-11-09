class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def generateLine(words, space_len):
            if len(words) == 1:
                return words[0] + ' ' * space_len
            n = len(words)
            space_gap, extra_space = space_len // (n - 1), space_len % (n - 1)
            line = ''
            for i in range(n - 1):
                line += words[i] + ' ' * space_gap
                if i < extra_space:
                    line += ' '

            return line + words[-1]

        line_list = []
        inline_words = []
        word_space_len = 0
        for word in words:
            if word_space_len + len(word) > maxWidth:
                word_len = word_space_len - len(inline_words)
                space_len = maxWidth - word_len
                line_list.append(generateLine(inline_words, space_len))
                inline_words = []
                word_space_len = 0
            inline_words.append(word)
            word_space_len += len(word) + 1
        line_list.append(' '.join(inline_words) + ' ' * (maxWidth - word_space_len + 1))
        return line_list
