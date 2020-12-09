### Setup

import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bsp
from webdriver_manager.chrome import ChromeDriverManager
import time



# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


def scrape():


    ### NASA Mars News

    # Get to website
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(2)

    # Soup and find content
    html = browser.html
    soup = bsp(html, 'html.parser')
    content = soup.find("div", class_="image_and_description_container")
    news_title = content.find("div", class_ = "content_title").text
    news_p = content.find("div", class_ = "article_teaser_body").text
    news_p



    ### JPL Mars Space Images - Featured Image

    # Get to website
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    time.sleep(2)

    # Click through to arrive at correc destination 
    browser.find_by_id("full_image").click()
    time.sleep(2)
    browser.links.find_by_partial_text("more info").click()
    time.sleep(2)

    # Soup and find content 
    html = browser.html
    soup = bsp(html, 'html.parser')
    base_url = "https://www.jpl.nasa.gov"
    img = soup.find("img", class_ ="main_image")["src"]
    featured_image_url = base_url + img
    print(featured_image_url)



    ### Mars Facts

    # Get to website 
    url = 'https://space-facts.com/mars/'
    browser.visit(url)

    # bring into table
    tables = pd.read_html(url)
    tables[0]

    description_df = tables[0].rename(columns = {0:'Labels', 1:'Measurement'})
    mars_facts = description_df.to_html(classes = "table table-striped")



    ### Mars Hemispheres


    # Get to website
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    hemisphere_image_urls = []

    # Click through to arrive at correc destination 
    for i in range(4):
        browser.find_by_tag("h3")[i].click()

        html = browser.html
        soup = bsp(html, 'html.parser')
        content = soup.find("div", id ="wide-image")
        data = {
            "img_url":content.find("a")["href"],
            "title":soup.find("h2", class_ = "title").text
        }

        hemisphere_image_urls.append(data)

        browser.back()

    hemisphere_image_urls

    # Store data into a dictionary 
    
    mars_data = {
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_facts": mars_facts,
        "hemisphere_image_urls": hemisphere_image_urls
    }
    
    #Return results
    
    return mars_data
        






