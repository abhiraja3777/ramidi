import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
from influxdb import InfluxDBClient



driver = webdriver.PhantomJS()
i = 0
client = InfluxDBClient('localhost', 8086, 'admin', 'admin', 'ramidi')
while 1:
	start = time.clock() 
	driver.get('https://srs.telenor.se/index.html#/retailer')
	stop = time.clock()-start

        #htmlsource = driver.page_source
        #print htmlsource

        #try:
	   #driver.find_element_by_id('retailId')
	   #driver.find_element_by_id('sellerId')
	   #driver.find_element_by_id('password')
	   #driver.find_element_by_id('loginButton')
	#except NoSuchElementException:
	   #print "There was an unusual response"
           #continue


	print "Response time to get the webpage is : %f" %(stop)
	time.sleep(5)
	s = driver.find_element_by_id('retailId')
	t = driver.find_element_by_id('sellerId')
	u = driver.find_element_by_id('password')
	f = driver.find_element_by_id('loginButton')
	time.sleep(5)
	if i == 0:
		s.send_keys('A7MB')
	t.send_keys('BTBT')
	u.send_keys('e2eBTH2017')
	start1 = time.clock()
	f.click()
	stop1 = time.clock()-start1

        #try:
	   #driver.find_element_by_id('personalId')
	   #driver.find_element_by_class_name('input-group-button')
        #except NoSuchElementException:
           #print "There was an unusual response"
           #continue

	print "Response time for login is : %f" %(stop1)

    #htmlSource = driver.page_source
    #print htmlSource

	time.sleep(5)
	new1=driver.find_element_by_id('personalId')
	new2=driver.find_element_by_class_name('input-group-button')
	time.sleep(5)
	new1.send_keys('19941029-8393')
	start2 = time.clock()
	new2.click()
	stop2 = time.clock()-start2
	print "Response time to fetch data is : %f" %(stop2)
	time.sleep(5)

	new3=driver.find_element_by_class_name('caret')
	time.sleep(5)	
	new3.click()
	time.sleep(5)
	new4=driver.find_element_by_link_text('Logga ut')
	time.sleep(5)
	start3=time.clock()
	new4.click()
	stop3=time.clock()-start3
	print "Response time for logout is: %f" %(stop3)
	i = i+1        
        #json_body=[ 
                   #{
                    #"measurement": "cpu_load_short",
                    #"fields": {
                         #"load_page": stop,
                         #"login": stop1,
                         #"fetch_data": stop2,
                         #"logout": stop3
                     #}
                   #}
                  #]
	#client.write_points(json_body)
