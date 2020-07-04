# question number 3
def anagram_check(paragraph):
    lowerParagraph = paragraph.lower()
    words = lowerParagraph.split(" ")

    anagrams = []

    for word1 in words:
        for word2 in words:
            if word1 != word2 and (sorted(word1) == sorted(word2)):
                anagrams.append(word1)

    return anagrams


paragraph = " My Cat brags because he grabs a mouse and act as nothing happened  "
print(anagram_check(paragraph))

