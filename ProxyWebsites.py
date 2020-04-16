import requests
import re
from bs4 import BeautifulSoup

class ProxyWebsite:
    def __init__(self, url):
        self.url = url
        self.proxies = set()

    def get_proxies(self):
        '''
        Get proxies from the proxy website 
        Returns a set of tuples with proxy hosts and ports
            Example: [(192.168.0.1, 80), .....]
        '''
        r = requests.get( self.url )
        soup = BeautifulSoup ( r.text, 'html.parser' )
        rows = soup.find_all( 'tr' )
        for data in rows:
            td = data.find_all('td')
            if len( td ) > 1:
                if re.search( "\d+\.\d+\.\d+\.\d+" , str(td[0])) != None:  # check if a valid ip address was found
                    ip = td[ 0 ].text
                    port = td[ 1 ].text
                    self.proxies.add( ( ip, port ) )
                else:
                    break
        return self.proxies            
                

Websites = [
    ProxyWebsite( url = 'https://socks-proxy.net/' ),
    ProxyWebsite( url = 'https://www.sslproxies.org/'),
    ProxyWebsite( url = 'https://us-proxy.org/'),
    ProxyWebsite( url = 'https://free-proxy-list.net/')
]

