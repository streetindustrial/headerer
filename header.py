#!/usr/bin/env python

import sys
from random import randint, choice, shuffle
from subprocess import PIPE

try:
    from subprocess import run
except ImportError:
    from subprocess import Popen as run

__version__ = '0.1'

browsers = (
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.104 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
    'Mozilla/5.0 (Unknown; Linux) AppleWebKit/538.1 (KHTML, like Gecko) Chrome/v1.0.0 Safari/538.1',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
    'Mozilla/5.0 (Windows NT 6.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586',
    'Mozilla/5.0 (Windows NT 6.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240',
    'Mozilla/5.0 (Windows NT 6.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) electron/1.0.0 Chrome/53.0.2785.113 Electron/1.4.3 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Mozilla/5.0 (Windows NT 5.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
    'Mozilla/5.0 (Windows NT 5.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Mozilla/5.0 (Windows NT 6.1; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20150101 Firefox/47.0 (Chrome)',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0',
    'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Mozilla/5.0 (Windows NT 5.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0',
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E)',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.991',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.991',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 OPR/42.0.2393.94',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 OPR/42.0.2393.94',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/601.4.4 (KHTML, like Gecko) Version/9.0.3 Safari/601.4.4',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/601.5.17 (KHTML, like Gecko) Version/9.1 Safari/601.5.17',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/601.6.17 (KHTML, like Gecko) Version/9.1.1 Safari/601.6.17',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/601.2.7 (KHTML, like Gecko) Version/9.0.1 Safari/601.2.7',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0.2 Safari/602.3.12',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/601.4.4 (KHTML, like Gecko) Version/9.0.3 Safari/601.4.4',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/601.5.17 (KHTML, like Gecko) Version/9.1 Safari/601.5.17',
    'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Thunderbird/45.3.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/601.5.17 (KHTML, like Gecko)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/601.4.4 (KHTML, like Gecko)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko)')

sites = (
    'https://www.google.com.ph', 'https://www.google.cv', 'https://www.google.tg',
    'https://www.google.iq', 'https://www.google.co.in', 'https://www.google.me',
    'https://www.google.com.tr', 'https://www.google.gr', 'https://www.google.sh',
    'https://www.google.as', 'https://www.google.com', 'https://www.google.com.om',
    'https://www.google.co.id', 'https://www.google.com.mx', 'https://www.google.pn',
    'https://www.google.ki', 'https://www.google.com.jm', 'https://www.google.com.ni',
    'https://www.google.ml', 'https://www.google.ba', 'https://www.google.com.ng',
    'https://www.google.md', 'https://www.google.com.pa', 'https://www.google.co.th',
    'https://www.google.mg', 'https://www.google.hn', 'https://www.google.dz',
    'https://www.google.ch', 'https://www.google.gp', 'https://www.google.co.ck',
    'https://www.google.co.ve', 'https://www.google.ad', 'https://www.google.fi',
    'https://www.google.ms', 'https://www.google.com.cu', 'https://www.google.com.sa',
    'https://www.google.li', 'https://www.google.pt', 'https://www.google.co.za',
    'https://www.google.nr', 'https://www.google.co.ls', 'https://www.google.ee',
    'https://www.google.com.kh', 'https://www.google.cg', 'https://www.google.cn',
    'https://www.google.ca', 'https://www.google.com.ec', 'https://www.google.co.il',
    'https://www.google.com.sb', 'https://www.google.se', 'https://www.google.sk',
    'https://www.google.tm', 'https://www.google.com.vn', 'https://www.google.com.lb',
    'https://www.google.nu', 'https://www.google.tl', 'https://www.google.ge',
    'https://www.google.by', 'https://www.google.cf', 'https://www.google.mu',
    'https://www.google.com.af', 'https://www.google.pl', 'https://www.google.sn',
    'https://www.google.co.jp', 'https://www.google.sc', 'https://www.google.com.co',
    'https://www.google.com.et', 'https://www.google.co.ma', 'https://www.google.com.uy',
    'https://www.google.fr', 'https://www.google.es', 'https://www.google.com.mt',
    'https://www.google.cat', 'https://www.google.mn', 'https://www.google.lu',
    'https://www.google.vg', 'https://www.google.com.pe', 'https://www.google.is',
    'https://www.google.co.ke', 'https://www.google.no', 'https://www.google.com.py',
    'https://www.google.com.sl', 'https://www.google.vu', 'https://www.google.co.cr',
    'https://www.google.gl', 'https://www.google.ht', 'https://www.google.jo',
    'https://www.google.td', 'https://www.google.mk', 'https://www.google.com.tw',
    'https://www.google.com.cy', 'https://www.google.so', 'https://www.google.be',
    'https://www.google.kz', 'https://www.google.com.ua', 'https://www.google.com.nf',
    'https://www.google.mw', 'https://www.google.com.pk', 'https://www.google.co.tz',
    'https://www.google.co.ug', 'https://www.google.fm', 'https://www.google.com.ai',
    'https://www.google.it', 'https://www.google.dk', 'https://www.google.rw',
    'https://www.google.ps', 'https://www.google.com.qa', 'https://www.google.bg',
    'https://www.google.lk', 'https://www.google.rs', 'https://www.google.gm',
    'https://www.google.xxx', 'https://www.google.de', 'https://www.google.im',
    'https://www.google.lt', 'https://www.google.com.do', 'https://www.google.tt',
    'https://www.google.si', 'https://www.google.com.ag', 'https://www.google.com.np',
    'https://www.google.ru', 'https://www.google.bf', 'https://www.google.com.gt',
    'https://www.google.com.ar', 'https://www.google.ro', 'https://www.google.co.zm',
    'https://www.google.com.hk', 'https://www.google.com.kw', 'https://www.google.ci',
    'https://www.google.com.sg', 'https://www.google.com.gi', 'https://www.google.co.kr',
    'https://www.google.cl', 'https://www.google.com.ly', 'https://www.google.tn',
    'https://www.google.co.zw', 'https://www.google.com.pr', 'https://www.google.com.na',
    'https://www.google.mv', 'https://www.google.co.bw', 'https://www.google.kg',
    'https://www.google.co.vi', 'https://www.google.st', 'https://www.google.bi',
    'https://www.google.com.fj', 'https://www.google.dm', 'https://www.google.ie',
    'https://www.google.com.bn', 'https://www.google.tk', 'https://www.google.com.tj',
    'https://www.google.sm', 'https://www.google.gy', 'https://www.google.cm',
    'https://www.google.to', 'https://www.google.com.br', 'https://www.google.nl',
    'https://www.google.com.eg', 'https://www.google.am', 'https://www.google.com.vc',
    'https://www.google.ga', 'https://www.google.az', 'https://www.google.hr',
    'https://www.google.hu', 'https://www.google.co.nz', 'https://www.google.at',
    'https://www.google.ae', 'https://www.google.com.bz', 'https://www.google.lv',
    'https://www.google.co.uk', 'https://www.google.gg', 'https://www.google.com.sv',
    'https://www.google.com.bh', 'https://www.google.dj', 'https://www.google.com.gh',
    'https://www.google.je', 'https://www.google.com.bd', 'https://www.google.cz',
    'https://www.google.co.ao', 'https://www.google.bj', 'https://www.google.com.my',
    'https://www.google.la', 'https://www.google.co.mz', 'https://www.google.ws',
    'https://www.google.bs', 'https://www.google.cd', 'https://www.google.com.bo',
    'https://www.google.ne', 'https://www.google.com.au', 'https://www.google.co.uz')


class Generator:
    """
    HTTP headers randomizer by Violet.

    Usage (Unix):

      python3 header.py <option>=<value> ... > header_file

    You can override random values with your defaults as well:

      python3 header.py User-Agent="f*ck gv"

    Or use a default template from a file:

      python3 header.py $(cat template_file | xargs)

    Options:

    - hosts=<host1>,<host2>, ... - list of hosts for each of that unique
      headers will be created (default is .*)
    - ip_0=<ip> - start ip for Client-Ip and proxy headers (default is 1.0.0.0)
    - ip_1=<ip> - end ip (default is 255.255.255.255)
    - encodings=<encoding1>,<encoding2>... - list of encodings (gzip, ...)
      will be shuffled
    - languages=<lang1>,<lang2>... - languages to use (en-US, ...)
    """

    ip_command = ('dig', 'TXT', '+short', 'o-o.myaddr.l.google.com',
                  '@ns1.google.com')
    encodings = ['gzip', 'deflate', 'br', 'compress']

    def __call__(self, args=sys.argv[1:]):
        if '--help' in args or '-h' in args:
            print(self.__doc__)
        else:
            args, kws = self._parse_args(args)
            for arg in args: print(arg)
            hosts = kws.get('hosts', ['.*'])
            for host in hosts:
                print(host)
                self._print(self._gen(**kws))

    def _gen(self, **kws):

        def _gen_random_list(data):
            shuffle(data)
            s = choice((',', ', '))
            return s.join(data)

        def get_real_ip(**_):
            p = run(self.ip_command, stdout=PIPE, stderr=PIPE)
            try:  # python 2.7/3 compatibility
                txt = p.stdout.read()
            except AttributeError:
                txt = p.stdout
            return txt.decode('utf-8').strip('\n').strip('"')

        def set_user_agent(**_):
            return choice(browsers)

        def set_up_ref(**_):
            return choice(sites)

        def set_up_encodings(encodings=None, **_):
            if not encodings: encodings = self.encodings
            return _gen_random_list(encodings)

        def set_ip(ip_0='1.0.0.0', ip_1='255.255.255.255', **_):
            ip0, ip1 = map(int, ip_0.split('.')), map(int, ip_1.split('.'))
            ip = (str(randint(*sorted([i0, i1]))) for i0, i1 in zip(ip0, ip1))
            return '.'.join(ip)

        headers = {
            'User-Agent': set_user_agent(),
            'Client-Ip': set_ip(**kws),
            'Via': set_ip(**kws),
            'X-Forwarded-For': get_real_ip(**kws),
            'Referer': set_up_ref(**kws),
            'Accept-Encoding': set_up_encodings(**kws)
        }

        args = {'ip_0', 'ip_1', 'encodings'}

        for k, v in kws.items():
            if isinstance(v, (list, tuple)):
                v = ','.join(v)
            if k not in args:
                headers[k] = v

        return headers

    @staticmethod
    def _parse_args(args):
        _args = [arg for arg in args if '=' not in arg]
        kws = dict((arg.split('=') for arg in args if '=' in arg))
        for key, value in kws.items():
            if ',' in value:
                kws[key] = [v.strip(' ') for v in value.split(',')]
        return _args, kws

    @staticmethod
    def _print(headers):
        for k, v in headers.items():
            print('%s=%s' % (k, v))


if __name__ == '__main__':
    Generator()()
