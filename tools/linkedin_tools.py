import os
import time
from crewai_tools import tool
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tools.utils import get_linkedin_posts
from crewai import tools
import undetected_chromedriver as uc

#To catch exception on login
class LinkedinToolException(Exception):
    def __init__(self):
        super().__init__("You need to set the LINKEDIN_EMAIL and LINKEDIN_PASSWORD env variables")
        
#Function which scrapes linkedin
def scrape_linkedin_posts_fn(profile_username: str,orglink: int) -> str:
    print(f"Received profile_username in tool: {profile_username!r}")
    """
    A tool that can be used to scrape LinkedIn posts
    
    """
    linkedin_username = os.environ.get("LINKEDIN_EMAIL")
    linkedin_password = os.environ.get("LINKEDIN_PASSWORD")
    if not (linkedin_username and linkedin_password):
        raise LinkedinToolException()
    browser = uc.Chrome()
    browser.get("https://www.linkedin.com/login")
    #Login Process
    username_input = browser.find_element("id", "username")
    password_input = browser.find_element("id", "password")
    username_input.send_keys(linkedin_username)
    password_input.send_keys(linkedin_password)
    password_input.send_keys(Keys.RETURN)
    time.sleep(10)
    if orglink==0:
        browser.get(f"https://www.linkedin.com/in/{profile_username}/recent-activity/all/")
    else:
        browser.get(f"https://www.linkedin.com/company/{profile_username}/posts/")
    time.sleep(2)
    for _ in range(2):   
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")     
        time.sleep(2)
    posts = get_linkedin_posts(browser.page_source)
    print(f"Extraction process complete")
    browser.quit()
    return str(posts[:2])#Getting two posts

#Creating our custom tool here
@tool("ScrapeLinkedinPosts")
def scrape_linkedin_posts_tool(linkedin_username:str,orglink:int) -> str:  
    """
    A tool that scrapes LinkedIn posts from a given linkedin_username and orglink
    """
    linkedin_username = linkedin_username
    orglink = orglink
    if not linkedin_username:
        raise ValueError("Profile username not provided")
    return scrape_linkedin_posts_fn(linkedin_username,orglink)





