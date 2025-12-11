sentences = ["My name is Ram", "He is a good person", "You should be careful while coding", "He can do better", "The person is mysterious", "Jay Shree Ram", "It is my pen."]

word_trees = []
for sentence in sentences:
    words = sentence.split()
    word_trees.append(words)
print("\nWord Trees = ",word_trees)

print("\nNumbers of time each word appears:")
word_count = {}
for words in word_trees:
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
print(word_count)