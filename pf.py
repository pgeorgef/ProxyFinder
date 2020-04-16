from ProxyWebsites import  Websites

class ProxyFinder:
    def grab_proxy(self):
        '''
        Function that returns a set of tuples with proxy hosts and ports from all the proxy websites
            Example: [(192.168.0.1, 80), .....]
        '''
        proxies = set()
        for website in Websites:
            proxies.update(website.get_proxies())
        return proxies
