import sys

if sys.version_info[0] == 3:
    try:
        from markovbot import MarkovBot
    except:
        from markovbot.markovbot import MarkovBot
