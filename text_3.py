import difflib

text_1 = open('file_1.txt', 'r+').read()
# """Hello !! My name is A. I am from Vietnam. I am 25. I love coding"""

text_2 = open("file_2.txt", "r+").read()
# """Hello !! My name's B. Vietnam is my country. I  love coding and I am 25 too"""

text = difflib.SequenceMatcher(None,text_1, text_2,)

match_text = text.find_longest_match(0, len(text_1), 0, len(text_2))

match_block = text.get_matching_blocks()

print text.ratio()


# print match_text
# print text_1[match_text.a : match_text.a + match_text.size]
# print text_2[match_text.b : match_text.b + match_text.size]
# print match_block

def display_diff():
    print "The same words are:"
    for i in range(0, len(match_block) - 1):
        print text_1[match_block[i][0] : match_block[i][0] + match_block[i][2]]
        # print text_2[match_block[i][1] : match_block[i][1] + match_block[i][2]]
    return True

display_diff()
