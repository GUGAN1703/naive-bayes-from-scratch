spam_messages = ["win free cash","free cash prize"]
ham_messages = ["let's meet today","are you free today"]

#task 1:
def count_word(word,messages):
    count = 0
    for msg in messages:
        count+=msg.split().count(word)
    return count


def p_word_given_spam(word):
    spam_count = count_word(word,spam_messages)
    total_words_spam = 6 
    unique_words = 8
    return (spam_count +1) / (total_words_spam + unique_words )

def p_word_given_ham(word):
    ham_count = count_word(word, ham_messages)
    total_words_ham = 7 # let's meet today(3) + are you free today(4) = 7
    unique_words = 8
    return (ham_count + 1) / (total_words_ham + unique_words)

word1 = "win"
word2 = "cash"

Spam_score = p_word_given_spam(word1)*p_word_given_spam(word2)
Ham_score = p_word_given_ham(word1)*p_word_given_ham(word2)

print(f"Spam score:{Spam_score}")
print(f"Ham score:{Ham_score}")

if Spam_score > Ham_score:
    print("prediction:Spam")
else:
    print("prediction:Ham")