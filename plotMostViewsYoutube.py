
import re
import pylab
import requests

source = requests.get('http://en.wikipedia.org/wiki/List_of_most_viewed_YouTube_videos')
data = source.text

views = re.findall(r'>\d\d\d,\d+,\d+', data)
largeViews = re.findall(r'\d+,\d+,\d+,\d+', data)

views = [int(x.replace(',','')[1:]) for x in views]
largeViews = [int(x.replace(',','')) for x in largeViews]
views += largeViews
views.sort(reverse = True)

pylab.scatter(range(1, len(views) + 1), views)
pylab.annotate(views[0], xy = (1, views[0]), xytext = (10, views[0]), \
bbox = dict(boxstyle = 'round,pad=0.3', fc = 'yellow', alpha = 0.5), \
arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0', shrinkB=10))

pylab.xlabel("Nth Most Watched YouTube video")
pylab.ylabel("View Count (Billions)")
pylab.title("Top YouTube Videos by View Count")
pylab.xticks([1] + range(5, int(len(views)*1.1), 5))

pylab.show()

