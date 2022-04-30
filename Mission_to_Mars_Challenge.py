#!/usr/bin/env python
# coding: utf-8

# In[57]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[58]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[59]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[60]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[61]:


slide_elem.find('div', class_='content_title')


# In[62]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[63]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[64]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[65]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[66]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[67]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[68]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[69]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[70]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[71]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[72]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[73]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
html = browser.html
html_soup = soup( 'html.parser')

links = browser.find_by_css('a.product-item img')
for i in range(len(links)):
    hemispheres = {}
    browser.find_by_css('a.product-item img')[i].click()
    
    # scrape image title and url string
    
    sample_elem = browser.links.find_by_text('Sample').first
    
    sample_title = browser.find_by_tag('h2').first
    
    
    hemispheres['title'] = sample_title.text
    hemispheres['img_url'] = sample_elem['href']
    
    #add to list
    hemisphere_image_urls.append(hemispheres)
    
    browser.back()
    


# In[74]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[75]:


# 5. Quit the browser
browser.quit()


# In[ ]:




