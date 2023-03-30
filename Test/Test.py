import functools
import signal
import random
import string
import urllib.parse
import urllib.request
import json
import subprocess
import time

def func_test():
    try:
        # Generate random input data
        fullname = ''.join(random.choices(string.ascii_letters, k=10))
        suggestion = ''.join(random.choices(string.ascii_letters, k=20))
        # print(fullname,suggestion)
        # Encode data for POST request
        data = urllib.parse.urlencode({'fullname': fullname, 'suggestion': suggestion}).encode('utf-8')

        # Call action.php to insert data
        request = urllib.request.Request('http://localhost/action.php', data=data, method='POST')
        # print(request)
        response = urllib.request.urlopen(request, timeout=10)
        print(response.getcode())
        # Check if insert was successful
        if response.getcode() == 200:
            # Call index.php to search for new record
            data = urllib.parse.urlencode({'search_fullname': fullname, 'search_suggestion': suggestion}).encode(
                'utf-8')
            request = urllib.request.Request('http://localhost/index.php', data=data, method='GET')
            result = urllib.request.urlopen(request).read().decode('utf-8')
            if fullname in result and suggestion in result:
                return "success"
            else:
                raise Exception("fail-1")
        else:
            raise Exception("fail-2")
    except:
        raise Exception("fail-3")

