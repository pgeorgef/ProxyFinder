import requests
import re
import json
from bs4 import BeautifulSoup

class ProxyWebsite:
    def __init__(self, url):
        self.url = url
        self.proxies = set()

    def get_proxies(self):
        '''
        Get proxies from the proxy website 
        Returns a list without duplicates of dictionaries with proxy hosts, ports and protocols
            Example: [{'ip' : '109.167.113.9', 'port' : '59606', 'protocol' : 'Https'}, .....] 
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
                    if td[ 6 ].text == 'yes':  # check if the protocol is Https or Http
                        protocol = 'Https'
                    else:
                        protocol = 'Http'
                    proxies_dict = {
                        'ip' : ip,
                        'port' : port,
                        'protocol' : protocol
                    }

                    self.proxies.add( json.dumps(proxies_dict) ) # add the dict in the json format so it can be added in a set

                else:
                    break
        self.proxies = list(self.proxies)
        for i in range( len(self.proxies) ):
            self.proxies[ i ] = json.loads( self.proxies[ i ] )  # convert the json back to a dict
        return self.proxies            
                

Websites = [
    ProxyWebsite( url = 'https://socks-proxy.net/' ),
    ProxyWebsite( url = 'https://www.sslproxies.org/'),
    ProxyWebsite( url = 'https://us-proxy.org/'),
    ProxyWebsite( url = 'https://free-proxy-list.net/')
]