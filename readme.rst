Header-mod

OS: Linux, Mac OS
Python: 2.7+, 3.0+
Requirements: None
Version: 0.1.1
Author: Violet Red `https://violent.red`_
GPG:

Description:

    Originally it was intended to be used with
    HTTP Header Mangler `https://github.com/disptr/httpheadermangler`_
    Firefox Plugin by Peter Nilsson.

    This simple tool can generate random IP (fake proxy) headers and set up
    random "Referer" and "User-Agent" as well.

Usage (terminal):

    You may want to set the file to be executable (for convenience):

        mv header.py header
        chmod u+x header

    Then use it just like any UNIX program:

        header

    To save this into a file:

        header > headers.txt

    Generate IP within a range:

        header ip_0=1.1.1.1 ip_1=5.5.5.5

    Override or set headers (quotes will be escaped):

        header Referer="http://your.site"

    Generate headers for multiple hosts (no spaces between commas, please):

        header hosts=".*,abc.d"

    Result example:

        .*
        User-Agent=Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101
        Client-Ip=109.119.22.182
        Via=251.28.117.165
        X-Forwarded-For=65.43.11.120
        Referer=https://www.google.com.bh

Setting up a cron job (Mac OS):

    `com.http.header.maker.plist` contains a simple cron job for Mac OS system.

    Copy this file into the ... (I forgot where it's stored)

Setting up a cron job (Linux):

    in progress ...
