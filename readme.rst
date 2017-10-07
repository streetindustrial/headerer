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

    Result example:

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

    xA0DAAoBBlwjHugln6QBy+F0AOIAAAAA43JlYWRtZS5y4XN0AMLBXAQAAQoAEAUC
    WdkLXQkQBlwjHugln6QAAC5oEAB5aRvfYW+A5K34FFsxToAwlCy4L7WSCr+gXKhi
    7HNYX9It8/CwDF9GMkmPL2Kk3ODQa09syh0t8dDdtcT2xXh5xaI40P11pQTCMDT1
    EjwSra0s8CGrB0c6DxynlcOQKwytjJtlZr7luNxdIwmscW6ZYxCze+IFXJwxiZEq
    v3sbuzN3e4dmv5da+ydS876TKGucpHRGQE+5TPLKsDxd4O1+o36KPk6LO55Ac18l
    5qTDXN6PpRrKQQm0WYUvqpPJ2SujZdc1RjNJmFNAHoJrYPFOMNpUpXDg0hm/F3JZ
    waYaWTU409I+1HiN6R1xVhf+tsb3pl3yYpM8xhajq4+WjUjPfGidFlqZGDS42JJm
    Y0/wpq9+WWOOhFEtidsjibTeKzg8QgGEWYGxOpbiH85c0RAYy/OTA8+F1px5Gjif
    L0hAZsmUyNCz1yOc/UB+5SfrzSZUslrUbOvYrCcV9vkZXiE5fb93vQPZDQfd9ntO
    vjcQqL22gZNW2NwjkIsxssu+u5eWuBF0ZE2rapjBQXYerHn+RnuHtk8XHfzcmqMT
    RJ5na0JJPkdaU1SImxDWc92W0SO1yr6RAk91d9MdwK4v0eFB5DZk/yI84zqdg0iv
    5lckihFtY14uoC6OQ45WlX7RAbyKR8yDLOopQLo+tGob4wiC1iLpTDb3PA73+3J9
    40r2vg==
    =L7F7
    -----END PGP MESSAGE-----
