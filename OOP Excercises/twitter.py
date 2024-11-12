"""Very awesome twitter script."""


class Tweet:
    """Tweet class."""

    def __init__(self, user: str, content: str, time: float, retweets: int):
        """
        Tweet constructor.

        :param user: Author of the tweet.
        :param content: Content of the tweet.
        :param time: Age of the tweet.
        :param retweets: Amount of retweets.
        """
        self.user = user
        self.content = content
        self.time = time
        self.retweets = retweets


def find_fastest_growing(tweets: list) -> Tweet:
    """
    Find the fastest growing tweet.

    A tweet is the faster growing tweet if its "retweets/time" is bigger than the other's.
    :param tweets: Input list of tweets.
    :return: Fastest growing tweet.
    """
    return max(tweets, key=lambda tweet: tweet.retweets / tweet.time)


def sort_by_popularity(tweets: list) -> list:
    """
    Sort tweets by popularity.

    Tweets must be sorted in descending order.
    A tweet is more popular than the other if it has more retweets.
    If the retweets are even, the newer tweet is the more popular one.
    :param tweets: Input list of tweets.
    :return: List of tweets by popularity
    """
    return sorted(tweets, key=lambda tweet: (tweet.retweets, -tweet.time), reverse=True)


def filter_by_hashtag(tweets: list, hashtag: str) -> list:
    """
    Filter tweets by hashtag.

    Return a list of all tweets that contain the given hashtag.
    :param tweets: Input list of tweets.
    :param hashtag: Hashtag to filter by.
    :return: Filtered list of tweets.
    """
    hashtag = hashtag.lower()
    filtered_tweets = []
    for tweet in tweets:
        content = tweet.content.lower()
        if hashtag in content:
            filtered_tweets.append(tweet)
    return filtered_tweets


def sort_hashtags_by_popularity(tweets: list) -> list:
    """
    Sort hashtags by popularity.

    Hashtags must be sorted in descending order.
    A hashtag's popularity is the sum of its tweets' retweets.
    If two hashtags are equally popular, sort by alphabet from A-Z to a-z (upper case before lower case).
    :param tweets: Input list of tweets.
    :return: List of hashtags by popularity.
    """
    hashtag_popularity = {}

    for tweet in tweets:
        content = tweet.content
        words = content.split()
        for word in words:
            if word.startswith("#"):
                if word in hashtag_popularity:
                    hashtag_popularity[word] += tweet.retweets
                else:
                    hashtag_popularity[word] = tweet.retweets

    sorted_hashtags = sorted(hashtag_popularity.keys(), key=lambda x: (-hashtag_popularity[x], x))
    return sorted_hashtags


if __name__ == '__main__':
    tweet1 = Tweet("@realDonaldTrump", "Despite the negative press covfefe #bigsmart", 1249, 54303)
    tweet2 = Tweet("@elonmusk", "Technically, alcohol is a solution #bigsmart", 366.4, 166500)
    tweet3 = Tweet("@CIA", "We can neither confirm nor deny that this is our first tweet. #heart", 2192, 284200)
    tweets = [tweet1, tweet2, tweet3]

    print(find_fastest_growing(tweets).user)  # -> "@elonmusk"

    filtered_by_popularity = sort_by_popularity(tweets)
    print(filtered_by_popularity[0].user)  # -> "@CIA"
    print(filtered_by_popularity[1].user)  # -> "@elonmusk"
    print(filtered_by_popularity[2].user)  # -> "@realDonaldTrump"

    filtered_by_hashtag = filter_by_hashtag(tweets, "#bigsmart")
    print(filtered_by_hashtag[0].user)  # -> "@realDonaldTrump"
    print(filtered_by_hashtag[1].user)  # -> "@elonMusk"

    sorted_hashtags = sort_hashtags_by_popularity(tweets)
    print(sorted_hashtags[0])  # -> "#heart"