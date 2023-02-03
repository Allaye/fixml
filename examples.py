from punctuation import FixPunctuation




punctuation = FixPunctuation()
# read test file
with open('tests/sample_text.txt', 'r') as fp:
    test_sample = fp.read()
    # predict text and print
    punctuated = punctuation.punctuate(test_sample)
    print(punctuated)
