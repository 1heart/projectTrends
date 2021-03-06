from trends import *

tweets_by_state = make_database()
tweets_by_state = add_value(tweets_by_state, 'MT', [tweets[1], tweets[5]])
tweets_by_state = add_value(tweets_by_state, 'MI', [tweets[0], tweets[4]])
tweets_by_state = add_value(tweets_by_state, 'FL', [tweets[3], tweets[7]])
tweets_by_state = add_value(tweets_by_state, 'ND', [tweets[2], tweets[6]])
tweets_by_state = add_value(tweets_by_state, 'AA', [tweets[8], tweets[9]])
groups = average_sentiments(tweets_by_state)

tweets = [
make_tweet('I am the very model of a modern Major-General'.lower(), None, 43, -84),
make_tweet("I've information vegetable, animal, and mineral".lower(), None, 58, -112),
make_tweet('I know the kings of England, and I quote the fights historical'.lower(), None, 49, -104),
make_tweet('From Marathon to Waterloo, in order categorical'.lower(), None, 19, -87),
make_tweet("I'm very well acquainted, too, with matters mathematical".lower(), None, 44, -85),
make_tweet('I understand equations, both the simple and quadratical'.lower(), None, 59, -110),
make_tweet("About binomial theorem I'm teeming with a lot o' news".lower(), None, 50, -100),
make_tweet('With many cheerful facts about the square of the hypotenuse'.lower(), None, 15, -87),
]
tweets += [make_tweet('This tweet is without a sentiment', None, None, None),
  make_tweet('This tweet is also without a sentiment', None, None, None),
  ]