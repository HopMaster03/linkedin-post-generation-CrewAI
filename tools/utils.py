from bs4 import BeautifulSoup

#Debug this function 
def parse_html_content(page_source: str):
    """
    Parses the HTML from the LinkedIn's profile and returns a collection of LinkedIn posts. We don't need
    all of them, just a few, since we can get the "writing-style" very easily.

    Args:
        page_source: The HTML content

    Returns:
        A list of div containers representing a collection of LinkedIn posts
    """
    print(f"parse html content started")
    linkedin_soup = BeautifulSoup(page_source.encode("utf-8"), "lxml")#not working
    print(f"encoding page done, result: ")
    containers = linkedin_soup.find_all("div", {"class": "feed-shared-update-v2"})
    print(f"containers found: ")
    containers = [container for container in containers if 'activity' in container.get('data-urn', '')]
    print(f"final container to return")
    return containers


def get_post_content(container, selector, attributes):
    """
    Gets the content of a LinkedIn post container
    Args:
        container: The div container
        selector: The selector
        attributes: Attributes to be fetched

    Returns:
        The post content
    """
    try:
        print(f"Started try operation")
        element = container.find(selector, attributes)
        if element:
            print(f"Try operation successful")
            return element.text.strip()
        print(f"Try operation fail")    
    except Exception as e:
        print(e)
    return ""

#For example post scraping
def get_linkedin_posts(page_source: str):
    containers = parse_html_content(page_source)
    posts = []
    for container in containers:
        post_content = get_post_content(container, "div", {"class": "update-components-text"})
        posts.append(post_content)       
    return posts

