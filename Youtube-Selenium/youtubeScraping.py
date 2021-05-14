from selenium import webdriver


url= 'https://www.youtube.com/'

driver= webdriver.Chrome("C:\\Users\\apizano\\Downloads\\chromedriver.exe")
driver.get(url)

videos = driver.find_elements_by_class_name('style-scope ytd-rich-grid-media')

for video in videos:
    name = video.find_element_by_xpath('.//*[@id="meta"]/h3').text
    views = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[1]').text.replace("views", "reproducciones")
    who = video.find_element_by_xpath('.//*[@id="text"]/a').text
    link = video.find_element_by_xpath('.//*[@id="video-title-link"]').get_attribute('href')
    if name:
        print("Video: "+name, views+". Author :"+ who+". Link:  "+link )