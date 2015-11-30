def get_page(url):
    try:
        if url == "http://neki.sajt.com":
            return '<some html code...>'
        elif url == "http://moze.i.ovaj.com":
            return '<some html code...> '
    except:
        return ""
    return ""

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def get_all_pages(page):
    while True:
        links = []
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links
# sada ubacujemo i index
def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])

def add_page_to_index(index,url,content):
    for entry in content.split():
        add_to_index(index, entry, url)


def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = [] #inicijalizacija indexa
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page) #get_page je "skupa" p-dura
            add_page_to_index(index, page, content) # pravi se index
            union(tocrawl, get_all_links(content))
            crawled.append(page)
    return crawled
        