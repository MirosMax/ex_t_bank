word = list(input())

result = "Yes"
start_len_w = len(word)
counter = 0

while True:
    for i in range(len(word) // 2):
        if word[i] != word[len(word) + 1 - i - 2]:
            result = "No"
            break
        else:
            result = "Yes"

    if result == "Yes" or counter >= start_len_w:
        break

    word.insert(0, 'a')
    counter += 1

print(result)
