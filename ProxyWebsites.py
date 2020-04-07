import requests
import re
from bs4 import BeautifulSoup

class ProxyWebsite:
    def __init__(self, url):
        self.url = url
        self.proxies = set()

    def get_proxies(self):
        '''
        Get proxies from the proxy website and return them
        '''
        r = requests.get( self.url )
        soup = BeautifulSoup ( r.text, 'html.parser' )
        rows = soup.find_all( 'tr' )
        for data in rows:
            td = data.find_all('td')
            if len( td ) > 1:
                if re.search( "\d+\.\d+\.\d+\.\d+" , str(td[0])) != None:  # check if I have a valid ip address
                    ip = td[ 0 ].text
                    port = td[ 1 ].text
                    self.proxies.add( ( ip, port ) )
                else:
                    break
        return self.proxies            
                

