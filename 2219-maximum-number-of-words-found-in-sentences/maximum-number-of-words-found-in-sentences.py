class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        maxlen = 0

        for i in sentences:
            count = i.count(" ") + 1

            if count > maxlen:
                maxlen = count

        return maxlen