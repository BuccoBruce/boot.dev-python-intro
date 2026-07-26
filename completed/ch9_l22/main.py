def filter_messages(messages):
    filtered_messages = []
    censored_words = ["dang"]
    censored_count_list = []

    for message in messages:
        censored_count = 0
        words = message.split()
        filtered_words = []

        for word in words:
            if word in censored_words:
                censored_count += 1
            else:
                filtered_words.append(word)

        sentence = " ".join(filtered_words)
        filtered_messages.append(sentence)

        censored_count_list.append(censored_count)

    return filtered_messages, censored_count_list
