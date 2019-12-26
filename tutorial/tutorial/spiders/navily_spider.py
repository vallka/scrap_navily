import scrapy
import csv

class MarinaLink(scrapy.Item):
    country = scrapy.Field()
    region = scrapy.Field()
    page = scrapy.Field()
    link = scrapy.Field()

class Marina(scrapy.Item):
    country = scrapy.Field()
    link = scrapy.Field()
    name = scrapy.Field()
    coord = scrapy.Field()
    berths  = scrapy.Field()
    draft  = scrapy.Field()
    length  = scrapy.Field()
    vhf  = scrapy.Field()
    phone  = scrapy.Field()
    electricity = scrapy.Field()
    water = scrapy.Field()
    wifi = scrapy.Field()
    fuel = scrapy.Field()

#FEED_EXPORT_FIELDS = ['country','name','coord','berths','draft','length','vhf','phone','electricity','water','wifi','fuel']

class Region(scrapy.Item):
    country = scrapy.Field()
    region = scrapy.Field()

class NavilyListMarinasSpider(scrapy.Spider):
    name = "navily-list-marinas"

    custom_settings = {
        'FEED_EXPORT_FIELDS': ['country','region','page','link']
    }

    def start_requests(self):
        with open('regions.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                print(row)
                country = row[0]
                link = row[1].split('/')
                id = link[-1]
                print (id)

                if id!=None:
                    reg = id
                    ix = range(1,51)

                    curl = """
curl "https://www.navily.com/region/next-page" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0" -H "Accept: */*" -H "Accept-Language: en-GB,en;q=0.5" --compressed -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" -H "X-CSRF-TOKEN: ajBIY2WZFVlSYxnvh11nVxQHbLBP8VQvTPNb87uz" -H "X-Requested-With: XMLHttpRequest" -H "Origin: https://www.navily.com" -H "Connection: keep-alive" -H "Referer: https://www.navily.com/region/sicily-anchorings-ports/317" -H "Cookie: XSRF-TOKEN=eyJpdiI6Ijc1bzRiekVnTU1Ma2Q2K2F3UkdQeEE9PSIsInZhbHVlIjoiT3E3djR6N0pqOFFubzJGRUI5OXNxdnl1akZQZ09YZU84aEJEbDBWZklvR1ZmZldsV2FnSkRhNHJYQmZsUmFJdSIsIm1hYyI6IjVjOTRjOTg0YWQ2ZGQ4OWUwMzRjMjY5N2MwMGM0YjA5OGE0ZjdiMTc2ZjIzYmFiZGIwYzgzNDUwOWEyMDE3NGYifQ"%"3D"%"3D; navily_webapp_session=eyJpdiI6Im4yZkFxNUdwQWdEMUxyODhpRk1aVXc9PSIsInZhbHVlIjoidks0Mldtd1wvZU5FaFoxTW1PdE1ISXFjcGx0N3dyanY1REJmSkVpcjZPXC9BaFB1QUlXbHZTSzBFXC9EOU1JRG1iRSIsIm1hYyI6IjRkMzNiMWZjNmU2MDNhNTBiZjNhZmRkMjk1YWM0NDBmYWE1OGFlYjI1ZTRiZDJiODVkNjc3OTg4MGY4NjMzZTEifQ"%"3D"%"3D; _ga=GA1.2.580859728.1577137865; _gid=GA1.2.46961634.1577137865; _fbp=fb.1.1577137865407.1944913650; CookieInfoScript=1; user_token=eyJpdiI6Ikg0dFQxQ0ZDUXhkMXFzOEExOEhBSVE9PSIsInZhbHVlIjoiZExZN0VZSEVrZUtYbVBvMVFFU095Zkd6OEg2Nk1TTkM2eE9RRTJlVE5lVnVnYVU4VXVqR2RnXC9OR05wQUx1cFwvZUduc3M3R09CQ2ZjdjJoYUJJSHBOVkFNdkx1MkFOTGVZNm1qb00yN2VqTT0iLCJtYWMiOiJkNTczYTY2MDc0NTE0NDI1YjFiZTNkODE3OTg2ZmJhY2Y3MzgxYmYxYWVmY2NkNWJmZTZmNzIyMmU4NDU1MTBiIn0"%"3D; crisp-client"%"2Fsession"%"2F0b8ed04d-fef2-4d38-94d9-1f27d5525ef1=session_d131ce75-5bb9-4900-acaa-2c2575b9ac29; crisp-client"%"2Fsession"%"2F0b8ed04d-fef2-4d38-94d9-1f27d5525ef1=session_55cc2549-9814-40cb-b5f5-cf4c2673b551" --data "id={}&pageNumber={}&filter=port"        
"""            

                    for i in ix:
                        yield scrapy.Request.from_curl(curl.format(reg,i), method="POST",
                                                callback=self.parse,
                                                cb_kwargs={'i': i,'country': country, 'region': reg}
                                                )

    def parse(self, response,i,country,region):
        if len(response.body)>0:
            print ('----------------parse',i,country)
            #print (response.body)
            aa = response.css('a::attr(href)').getall()
            #print (aa)
            for a in aa:
                #print ( a)
                r = MarinaLink(country=country,link=a,region=region,page=i)
                yield r



class NavilyRegionsSpider(scrapy.Spider):
    name = "navily-regions"

    start_urls = [
        'https://www.navily.com/regions',
    ]        

    def parse(self, response):
        for country in response.css('.country-list-container .container'):
            #print (country.css('.title::text').get())
            country_text = country.css('.title::text').get().split(" ")[-1]

            aa = country.css('.section-slides-image a::attr(href)').getall()
            for a in aa:
                #print(a)
                r = Region(country=country_text,region=a)
                #yield scrapy.Request(a, callback=self.parseRegion,cb_kwargs={'country': country_text})
                yield r


class NavilySpider(scrapy.Spider):
    name = "navily-marinas"

    #country_now = 'Brazil'
    #country_now = 'States'
    #country_now = 'Greece'
    #country_now = 'Croatia'
    #country_now = 'Spain'
    #country_now = 'France'
    country_now = 'Italy'
    
    

    custom_settings = {
        'FEED_EXPORT_FIELDS': ['country','name','coord','berths','draft','length','vhf','phone','electricity','water','wifi','fuel']
    }

    links = []
    new_links = []
    old_links = []

    def start_requests(self):
        with open('marina_links3.csv', newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if row[0]=='country':
                    continue

                self.old_links.append(row[3])

        with open(self.country_now+'-new.csv', newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line=0
            for row in csv_reader:
                line += 1
                print(row)
                if row[0]=='country' or row[0]!=self.country_now:
                    continue

                if line<int(self.settings['LINE']):
                    self.old_links.append(row[3])
                    continue

                country = row[0]
                link = row[3]
                print (link)
                self.links.append(link)

        print (self.links)        

        for link in self.links:
            yield scrapy.Request(link, callback=self.parsePort,cb_kwargs={'country': self.country_now})

            
    def closed(self,reason):
        print ('***EXTRA LINKS***',self.new_links)
        with open(self.country_now +'-new2.csv',mode='w', newline='') as csv_file:
            for link in self.new_links:
                csv.writer(csv_file).writerow([self.country_now,None,None,link])

    def parse(self, response):
        for country in response.css('.country-list-container .container'):
            #print (country.css('.title::text').get())
            country_text = country.css('.title::text').get().split(" ")[-1]

            aa = country.css('.section-slides-image a::attr(href)').getall()
            for a in aa:
                #print(a)
                yield scrapy.Request(a, callback=self.parseRegion,cb_kwargs={'country': country_text})


    def parseRegion(self, response, country):
        #print ('-parseRegion-',country)
        ports = response.css('.region-container .item_port a::attr(href)').getall()
        for port in ports:
            #print("==port",port)
            yield scrapy.Request(port, callback=self.parsePort,cb_kwargs={'country': country})

    def parsePort(self, response, country):
        #print ('--parsePort--',country)

        marina = Marina()
        marina['country'] = country


        #nm = response.css('.container h1::text').get()
        #print (nm)

        #    response.css('.n-booking-navbar .d-none-mob::text').get()
        #        )
        marina['name'] = response.css('.container h1::text').get().strip()
        marina['coord'] = response.css('.n-booking-navbar .d-none-mob::text').get().strip(' /')

        params = {}
        for item in response.css('.landing-page-main .n-square-v2 .n-square-v2-item'):
            #print (item.css('.n-square-v2-item-label::text').get(),item.css('.n-square-v2-item-value::text').get())
            params[item.css('.n-square-v2-item-label::text').get()] = item.css('.n-square-v2-item-value::text').get()

        #print (params)    
        marina['berths'] = params['Berths'].strip(' —')
        marina['draft'] =  params['Draft'].strip(' —')
        marina['length'] =  params['Length'].strip(' —')
        marina['vhf'] =  params['VHF channel'].strip(' —')
        marina['phone'] =  params['Phone'].strip(' —')

        facilities = {}
        for eq in response.css('.landing-page-main .n-equipments li'):
            #f= list(map(lambda x: x.replace('\t','').replace('\n',''),eq.css('::text').getall()))[1::]
            #print(eq.css('.n-equipments-text strong::text').get(),eq.css('::attr(class)').get())
            facilities[eq.css('.n-equipments-text strong::text').get()] = \
                'yes' if eq.css('::attr(class)').get().find('unavailable')==-1 else 'no'

        #print (facilities)    
        marina['electricity'] = facilities.get('Electricity','no')
        marina['water'] = facilities.get('Water','no')
        marina['wifi'] = facilities.get('WIFI','no')
        marina['fuel'] = facilities.get('Fuel','no')

        links = response.css('.container .n-around a::attr(href)').getall()
        for link in links:
            if not link in self.links and not link in self.new_links and not link in self.old_links:
                self.new_links.append(link)


        #print (marina)
        yield marina
