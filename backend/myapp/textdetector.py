# !pip install googletrans
# !pip install dateparser

import dateparser
import datetime as dt
import re
from googletrans import Translator

def _gen_ngram(s, n):
    for i in range(len(s)):
        yield ' '.join(s[i:i+n])
    
def _data_corrector(s, current_date, date):
    for el in ['сегодня', 
               'завтра', 
               'понедельник', 
               'вторник', 
               'сред', 
               'четверг', 
               'пятниц', 
               'суббот', 
               'воскресень', ]:
        if el in s:
            shift = dt.datetime.now()-date
            return current_date-shift
    return current_date

def find_dates(s, current_date, ngrams=[1, 2, 3]):
    trans = Translator()
#    s = trans.translate(s).text
    s = re.sub(r'[^\w\s]','', s)
    s = s.replace(' to ', ' ')
    s = s.split(' ')
    dates = []
    for n in ngrams:
        for text_batch in _gen_ngram(s, n):
            pred = dateparser.parse(text_batch)
            if pred is not None:
                dates += [pred]
    dates = [x for x in dates if x > dt.datetime.now()-dt.timedelta(days=365)]
    if len(dates)>0:
        date = dates[-1]
        date = dt.datetime(date.year, date.month, date.day)
        return _data_corrector(s, date, current_date)
    else:
        return 
    
def find_urls(s):
    urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', s)
    try:
        return urls[-1]
    except:
        return 