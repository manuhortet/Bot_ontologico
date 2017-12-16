from keys import *
import time

while True:
    # reading and removing sentences from our generated_sentences.txt file
    sentences_list = open("generated_sentences.txt", "r+")
    tweet = sentences_list.readline()
    sentences_list.close()

    sentences_list = open("generated_sentences.txt", "r")
    new_txt_file = [line for line in sentences_list]
    sentences_list.close()

    sentences_list = open("generated_sentences.txt", "w")
    sentences_list.truncate()
    for x in range(1, len(new_txt_file)):
        sentences_list.write(new_txt_file[x])
    sentences_list.close()

    # tweeting!
    api.update_status(status=tweet)

    # waiting an hour to tweet again :)
    time.sleep(3600)

