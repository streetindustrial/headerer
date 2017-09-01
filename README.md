# Headerer

HTTP Header semi-random generator.

Generates a random HTTP header and directs it into stdout.

## Requirements

- **Python** (2.7.3, 3.6.2 approved)
- **Linux / OS X** probably, cause it uses *dig* to get the external IP

## Usage

Originally made to be used with Firefox extensions, that can load header
settings from a file, to update headers once a day etc.

By its own.

```console
python header.py > headers
```

With arguments or with a file template:

```console
python header.py $(cat template_file | xargs)
```

## Arguments and defaults:

Any standard header param passed as argument will override its random generation.
For example, if you pass `header.py Referer=http://google.com`, then it will
set the google page as the *Referer* param in the headers.

- hosts - list of hosts/host patterns, for each host random headers will be created
- ip_0, ip_1 - range of IPv4 addresses for proxy headers (defaults range from 0 to 255)

For random browser headers a hardcoded list of ~100 most common browser
headers was used.

For random *Referer* header it uses a list of (mostly) google domains.
