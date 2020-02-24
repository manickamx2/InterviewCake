# 2.20.2020
# You work with a team whose job is to understand to the most sought after toys for the holiday season.
# A teammate of yours has built a webcrawler that extracts a list of quotes about toys from different
# articles. You need to take these quotes and identify which toys are mentioned most frequently. Write an
# algorithm that identifies the top N toys out of a list of quotes and a list of toys.
#
# Your algorithm should output the top N toys mentioned most frequently in the quotes.

# Input:
# The input to the function/method consists of five arguments:
#
# numToys, an integer representing the number of toys
# topToys, an integer representing the number of top toys your algorithm needs to return
# toys, a list of strings representing the toys,
# numQuotes, an integer representing the number of quotes about toys;
# quotes, a list of strings that consists of space-sperated words representing articles about toys
#
# Output:
# Return a list of strings of the most popular N toys in order of most to least frequently mentioned
#
# Note:
# The comparison of strings is case-insensitive.
# If the value of topToys is more than the number of toys, return the names of only the toys mentioned in the quotes.
# If toys are mentioned an equal number of times in quotes, sort alphabetically.

import re
import unittest

def topNToys(numToys, topToys, toys, numQuotes, quotes):

    # create a dictionary {'toyName': [mention_count, number_of_quotes_mentioned_in]}
    toy_freq = { toy:[0,0] for toy in toys }
    for quote in quotes: # loop through quotes
        # initiate each toy occurrence to false (i.e. it is not contained in any quotes)
        toy_in_quote = { toy:False for toy in toys }
        for word in quote.lower().split():
            word = re.sub('[^A-Za-z]', '', word)
            if word in toy_freq:
                toy_freq[word][0] += 1
                # the toy is found in a quote, so update toy_in_quote[word] to True and update toy_freq[word][1] = 1
                if not toy_in_quote[word]:
                    toy_in_quote[word] = True
                    toy_freq[word][1] += 1

    # now to have to sort first by total count, then by number of quotes count, then alphabetically
    sorted_toy_freq = sorted(toy_freq.items(), key=lambda x: (-x[1][0], -x[1][1], x[0]))
    result = []
    for toy in sorted_toy_freq[:topToys]:
        result.append(toy[0])

    return result


# Tests
class Test(unittest.TestCase):

    def test_one(self):
        numToys = 6
        topToys = 3
        toys = ["elmo", "elsa", "legos", "drone", "tablet", "warcraft"]
        numQuotes = 5
        quotes = [
            "Elmo is the hottest of the season! Elmo will be on every kid's wishlist!",
            "The new Elmo dolls are super high quality",
            "Expect the Elsa dolls to be very popular this year, Elsa!",
            "Elsa and Elmo are the toys I'll be buying for my kids, Elsa is good",
            "For parents of older kids, look into buying them a drone",
            "Warcraft is slowly rising in popularity ahead of the holiday season"
        ]
        result = topNToys(numToys, topToys, toys, numQuotes, quotes)
        expected = ['elmo', 'elsa', 'drone']
        self.assertEqual(result, expected)

    def test_two(self):
        numToys = 2 # number of toys is less than the top toys expected
        topToys = 3
        toys = ["elmo", "elsa"]
        numQuotes = 5
        quotes = [
            "Elmo is the hottest of the season! Elmo will be on every kid's wishlist!",
            "The new Elmo dolls are super high quality",
            "Expect the Elsa dolls to be very popular this year, Elsa!",
            "Elsa and Elmo are the toys I'll be buying for my kids, Elsa is good",
            "For parents of older kids, look into buying them a drone",
            "Warcraft is slowly rising in popularity ahead of the holiday season"
        ]
        result = topNToys(numToys, topToys, toys, numQuotes, quotes)
        expected = ['elmo', 'elsa']
        self.assertEqual(result, expected)

    def test_three(self):
        numToys = 5
        topToys = 3
        toys = ["altracell", "betacell", "cartacell", "duracell", "ectocell"]
        numQuotes = 5
        quotes = [
            "Altracell is better than betacell! Kids love altracell",
            "Betacell is good",
            "Duracell is a battery, not a toy",
            "Cartacell is a funny name. Ectocell sounds better",
            "Duracell is a battery",
            "Betacell is better than duracell"
        ]
        result = topNToys(numToys, topToys, toys, numQuotes, quotes)
        expected = ['betacell', 'duracell', 'altracell']
        self.assertEqual(result, expected)

    def test_empty_quotes(self):
        numToys = 5
        topToys = 3
        toys = ["altracell", "betacell", "cartacell", "duracell", "ectocell"]
        numQuotes = 5
        quotes = [

        ]
        result = topNToys(numToys, topToys, toys, numQuotes, quotes)
        expected = ['altracell', 'betacell', 'cartacell']
        self.assertEqual(result, expected)

    def test_empty_toys(self):
        numToys = 0
        topToys = 3
        toys = []
        numQuotes = 5
        quotes = [
            "Altracell is better than betacell! Kids love altracell",
            "Betacell is good",
            "Duracell is a battery, not a toy",
            "Cartacell is a funny name. Ectocell sounds better",
            "Duracell is a battery",
            "Betacell is better than duracell"
        ]
        result = topNToys(numToys, topToys, toys, numQuotes, quotes)
        expected = []
        self.assertEqual(result, expected)

unittest.main(verbosity=2)
