## weatherspideer
The folder contains python spider project based on scrapy.
The purpose is to crawl every period every day climate data in 2018.


## usage
cd to weather
run 'scrapy crawl weather2018 -o filename.csv'

## Changes before use
### In ./weahter/middlewares.py

`driver = webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe", chrome_options=chrome_options)`
// You should download chrome driver and change the path of it in this command.

## Author
- Jiansheng Zhang