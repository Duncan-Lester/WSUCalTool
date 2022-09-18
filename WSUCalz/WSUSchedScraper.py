from bs4 import BeautifulSoup
import re
from urllib.request import urlopen

baseUrlexample = 'https://schedules.wsu.edu/List/Pullman/20223/Chem'



# find <tr> with class 'course_title'
# coursesOffered = soup.find_all('tr','course_title')

#find all 345 sections
campus = 'Pullman'
year = '2022'
term = '3'
prefix = 'CHEM'
classNum = '345'

def generalScraper(campus, year,term,prefix,classNum):
  constructed_Url = f'https://schedules.wsu.edu/List/{campus}/{year}{term}/{prefix}'
  page=urlopen(constructed_Url)
  xml = page.read().decode('utf-8')
  soup = BeautifulSoup(xml, 'lxml')
  secSchedList = []
  secDayList = []
  secTimeList = []
  chemCourses = soup.find_all( 'a', href=re.compile(f'.*{classNum}.*'))
  for chemCourse in chemCourses:
    chemSection = chemCourse.find_parent('tr')
    #TODO fix scrape logic error where sections with two times (recitation, break, lab) show up with 
    #only one time shown
    schedDay = chemSection.find('td', headers='sched_days')
    schedDay = schedDay.string.replace(',','')
    schedDay = schedDay.replace("'","")
    schedSec = chemSection.find('td', headers='sched_sec')
    secSchedList = secSchedList + [schedSec.a.string]
    secDayList = secDayList + [schedDay]
    secDayList.sort()
  
  return (secSchedList, secDayList, constructed_Url)

# for debugging, run the file after swapping print/return lines and the function call line
# (don't uncomment this block!) and run this module by itself to check output before hooking up to a web app.

#generalScraper(campus, year, term, prefix, classNum)