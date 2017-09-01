# Headerer

v.0.1

HTTP Header semi-random generator.
Generates a random HTTP header and directs it into the stdout.

## Requirements

- **Python** (2.7.3, 3.6.2 approved)
- **Linux / OS X** probably, cause it uses *dig* to get the external IP

## Usage

Originally made to be used with Firefox extensions, that can load header
settings from a file, to update headers once a day etc. I'm going to make
a normal plugin out of this (or not, it depends on my laziness).

By its own.

```console
python header.py
```

You'll get something like this:

```console
.*
User-Agent=Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240
Client-Ip=171.143.103.130
Via=171.150.181.101
X-Forwarded-For=66.31.42.107
Referer=https://www.google.com.tr
Accept-Encoding=gzip, compress, br, deflate
```

With arguments or with a file template + saving into a file:

```console
python header.py $(cat template_file | xargs) > my_headers
```

## Arguments and defaults:

Any standard header param passed as argument will override its random generation.
For example, if you pass `header.py Referer=http://google.com`, then it will
set the google page as the *Referer* param in the headers.

Some specific keywords counts as the headerer settings and never as
browser headers, they are:

- hosts - list of hosts/host patterns, for each host random headers will be created
- ip_0, ip_1 - range of IPv4 addresses for proxy headers (defaults range from 0 to 255)
- languages - languages to use (will be shuffled)
- encodings - encodings to use (will be shuffled)

For random browser headers a hardcoded list of ~100 most common browser
headers was used.

For a random *Referer* header it uses a list of (mostly) google domains.
