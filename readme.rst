Header-mod
==========

:OS: Linux, Mac OS
:Version: 0.1.1
:Author: `V.R. (keybase)`_
:Website: `violent.red`_

Description
===========

    Originally it was intended to be used with `HTTP Header Mangler`_
    Firefox Plugin by *Peter Nilsson*.

    This simple tool can generate random IP (fake proxy) headers and set up
    random "Referer" and "User-Agent" as well.

Usage (terminal)
================

    You may want to set the file to be executable (for convenience)::

        mv header.py header
        chmod u+x header

    Then use it just like any UNIX program::

        header

    To save this into a file::

        header > headers.txt

    Generate IP within a range::

        header ip_0=1.1.1.1 ip_1=5.5.5.5

    Override or set headers (quotes will be escaped)::

        header Referer="http://your.site"

    Generate headers for multiple hosts (no spaces between commas, please)::

        header hosts=".*,abc.d"

    Result example::

        .*
        User-Agent=Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101
        Client-Ip=109.119.22.182
        Via=251.28.117.165
        X-Forwarded-For=65.43.11.120
        Referer=https://www.google.com.bh

Setting up a launchd job in Mac OS
==================================

    **com.http.header.maker.plist** contains a simple cron job for
    Mac OS system, which will regenerate a random headers file periodically.

    It must be stored in `~/Library/LaunchAgents`.
    See `Creating Launch Daemons and Agents (Apple)`_.

Setting up a cron job in Linux
==============================

    in progress ...


.. _HTTP Header Mangler: https://github.com/disptr/httpheadermangler
.. _V.R. (keybase): https://keybase.io/electrostatix
.. _violent.red: https://violent.red
.. _Creating Launch Daemons and Agents (Apple): https://developer.apple.com/library/content/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html

Signature
=========

-----BEGIN PGP MESSAGE-----
Comment: https://keybase.io/download
Version: Keybase Go 1.0.33 (darwin)

xA0DAAoBBlwjHugln6QBy+F0AOIAAAAA5EhUVFAgaGVhZGVyIGdlbmXjcmF0b3Ig
YnniIFYuUuAuAMLBXAQAAQoAEAUCWdkO1wkQBlwjHugln6QAAJqpEAAN7Ob4NBzD
VDZiXRe6rEl5F/Gqj8MexgMLmaPzoZH1mYKOjkP6yqk9St2ex4mWihu5vUrCSRD7
3THq9x5hlZsxLtlyCyCKBnfjQSnrds8B8kSLHifJ0ZZ1yv2lSjjlEZ+v/vOFYjMj
2YMoDqeLOAA3HoLsVzyhXMXjZ0W0DWBAvjY/ydT1VnTSX1dTI2f2bCcyW/NekSH1
3FzGIlR13PopYoFPCU7gD500WSTxDovrvV0vanNI7f8LdstzLMZLYX81WBaB/zHh
T/gfcTRaVs1g0hAliOL9+Pn4rxLrN92zXMxzpJMtCEjXvnntSr57r1btALN1WqFk
hg1FI62h1E+88mW7EuSxO924nJWsQYSk4ZDIbFiA1F3OmxJgxR1O/8MKutupMiWC
xBz4XhyjyxWLZF+iKSQllxNEZ73pSc/4vd5NINxrWzVG/pAUQSagnLtETNve3b6O
BdAGrA3+yj/KiXYAZZnD+IAQXrxtWrbACVDD4qmZy3wDNqQh3klklg+d+91heziZ
sJw8NVkriIUO3c0X6lIAAdk40matYb7s7HE7gI6NWJ804YfiAJqO1F4J8ijsYhyX
xrK8ndW+1qdEDtUQulDaGlNGZvrICCHne9wTk7DA2EVIyVCv8k3dxdq2RQ7GM6hh
3lWiueXXRh6vnJT+2x3Y/JRKuH9dX7xPNg==
=/k9R
-----END PGP MESSAGE-----
