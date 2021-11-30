import requests
import matplotlib.pyplot as plt
import numpy
from config import authkey
date = []
twitter = []

topten = requests.get('https://financialmodelingprep.com/api/v4/social-sentiment/trending?apikey={}'.format(authkey))
fmp = topten.json()


print('---MOST TRENDING STOCKS----')
for x in range(len(fmp)):
    print('')
    print(str(x+1) + '.' + ' ------------')
    print('')
    print('Symbol: ' + fmp[x]['symbol'])
    print('')
    print('--- Twitter ---')
    print('Twitter Comments: ' + str(fmp[x]['twitterComments']))
    print('Twitter Impressions: ' + str(fmp[x]['twitterImpressions']))
    print('Twitter Likes: ' + str(fmp[x]['twitterLikes']))
    print('Twitter Posts: ' + str(fmp[x]['twitterPosts']))
    print('')
    print('--- Stockwits ---')
    print('Stockwits Comments: ' + str(fmp[x]['stocktwitsComments']))
    print('Stockwits Impressions: ' + str(fmp[x]['stocktwitsImpressions']))
    print('Stockwits Likes: ' + str(fmp[x]['stocktwitsLikes']))
    print('Stockwits Posts: ' + str(fmp[x]['stocktwitsPosts']))

print('')
symbol = input('Pick a trending ticker: ')

historicalsentiment = requests.get('https://financialmodelingprep.com/api/v4/historical/social-sentiment?symbol={}&limit=1000&apikey={}'.format(symbol.upper(),authkey))
fmp1 = historicalsentiment.json()

for i in range(len(fmp1)):
    date.append(fmp1[i]['date'])
    twitter.append(fmp1[i]['twitterImpressions'])
date.reverse()
twitter.reverse()

twitter_array = numpy.array(twitter)

plt.plot(date, twitter_array/1000)

# naming the x axis
plt.xlabel('Date/Time')
# naming the y axis
plt.ylabel('Impressions * 1000')

# giving a title to my graph
plt.title('Social Sentiment')

# function to show the plot
plt.show()

