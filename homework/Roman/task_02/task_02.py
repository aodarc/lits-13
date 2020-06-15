def find_most_frequent(text: str):
    # Unify all text to lower case
    loc_text = text.lower()

    # Create list of words
    words_list = []
    one_word = ''
    for i in loc_text:
        if i.isalpha():
            one_word += i
            word_flag = True
        else:
            # Some punctuation mark happens
            if word_flag:
                word_flag = False
                words_list.append(one_word)
                one_word = ''

    # Made set from list to remove duplicates
    words_set = set(words_list)

    # Calculate frequency of word happening.
    # Will have list which contains pairs of elements: [word, freq]
    word_freq = []
    for j in words_set:
        word_cnt = [j]
        cnt = 0
        for i in words_list:
            if i == j:
                cnt += 1
        else:
            word_cnt.extend(str(cnt))
            word_freq.append(word_cnt)

    # Check how many max elements we have
    word_freq.sort(key=(lambda elem: elem[1]), reverse=True)
    maximum = word_freq[0][1]
    maxs_list = []
    for i in word_freq:
        if maximum == i[1]:
            maxs_list.append(i[0])

    # Sort list of most faced words
    maxs_list.sort(key=(lambda word: word[0]))

    return maxs_list

