from ProxyWebsites import  Websites

class ProxyFinder:
    def grab_proxy(self, proxy_type='all'):
        '''
        Function that returns a set of tuples with proxy hosts and ports from all the proxy websites
            Example: [(192.168.0.1, 80), .....]
        Protocol option argument default value is all, it can be all, http, or https
        '''
        proxies = list()
        for website in Websites:
            proxies.extend(website.get_proxies(proxy_type))
        return proxies
