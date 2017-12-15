from keys import *
import time

while True:

    # reading and removing sentences from our generated_sentences.txt file
    sentences_list = open("generated_sentences.txt", "r+")
    tweet = sentences_list.readline()
    new_txt_file = sentences_list.readlines()
    sentences_list.truncate(0)
    for x in range(0, len(new_txt_file)):
        sentences_list.write(new_txt_file[x])

    # tweeting!
    api.update_status(status=tweet)

    # waiting an hour to tweet again :)
    time.sleep(1200)

