import requests
import re
import json
from bs4 import BeautifulSoup

class ProxyWebsite:
    def __init__(self, url):
        self.url = url
        self.proxies = set()

    def get_proxies(self, type_option):
        '''
        Get proxies from the proxy website 
        Returns a list without duplicates of dictionaries with proxy hosts, ports and type
            Example: [{'ip' : '109.167.113.9', 'port' : '59606', 'proxy_type' : 'Https'}, .....] 
        type_option argument default value is all, it can be all, Http, or https
        '''
        self.proxies = set()
        r = requests.get( self.url )
        soup = BeautifulSoup ( r.text, 'html.parser' )
        rows = soup.find_all( 'tr' )
        for data in rows:
            td = data.find_all('td')
            if len( td ) > 1:
                if re.search( "\d+\.\d+\.\d+\.\d+" , str(td[0])) != None:  # check if a valid ip address was found
                    ip = td[ 0 ].text
                    port = td[ 1 ].text
                    if td[ 6 ].text == 'yes':  # check if the proxy type is Https or Http
                        proxy_type = 'https'
                    else:
                        proxy_type = 'http'
                    proxies_dict = {
                        'ip' : ip,
                        'port' : port,
                    }
                    if type_option == 'all':
                        proxies_dict['proxy_type'] = proxy_type
                    elif type_option =='http':
                        if proxy_type =='http':
                            proxies_dict['proxy_type'] = proxy_type
                        else:
                            continue
                    elif type_option =='https':
                        if proxy_type =='https':
                            proxies_dict['proxy_type'] = proxy_type
                        else:
                            continue                    
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