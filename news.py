from GoogleNews import GoogleNews
news = input("search your news:")
googlenews = GoogleNews(lang='en', period='id')
googlenews.search(news)
results = googlenews.result(sort = True)
for result in results:
    print('\n\n TITLE:', result['title'] , '\nDESC:', result['desc'])