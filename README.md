# Web Scrapping with Python

## Initial Steps

- Install *scrapy* with pip : <pre> $ pip install scrapy </pre>
- Start scraping project with scrapy : <pre> $ scrapy startproject ietf_scrapper </pre>
- Generate spider *ietf* for scraping domain *pythonscraping.com* : <pre>$ scrapy genspider ietf pythonscraping.com </pre>
- Run the modified *ietf.py* spider : <pre>$ scrapy runspider ietf.py</pre>
- use xpath to scrap the site