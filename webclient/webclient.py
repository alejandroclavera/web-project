from urllib.request import urlopen
import bs4

class WebClient(object):

    def __init__(self):
        pass

    def get_web_page(self):
        # Get web page
        webpage = urlopen('http://bid.udl.cat/ca/')
        html = webpage.read()
        return html
    
    def parse_web_page(self, html):
        soup = bs4.BeautifulSoup(html, features='lxml')
        news = soup.find_all('li', 'box')
        information = []
        for new in news:
            title_tag = new.find('a')
            title = title_tag['title']
            information.append(title)
        return information

    def get_information(self):
        html = self.get_web_page()
        info = self.parse_web_page(html)
        # read information
        return info

if __name__ == '__main__':
    client = WebClient()
    information = client.get_information()
    print(information)

    
