#
cd to weather
run 'scrapy crawl weather2018 -o filename.csv'

## Changes before use
### In ./weahter/middlewares.py

`driver = webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe", chrome_options=chrome_options)`
// You should download chrome driver and change the path of it in this command.
