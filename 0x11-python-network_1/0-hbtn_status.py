#!/usr/bin/python3
"""
<<<<<<< HEAD
a Python script that fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
=======
 a Python script that fetches https://alx-intranet.hbtn.io/status
 
"""

if __name__ == '__main__':
    import urllib.request
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
>>>>>>> 29ec27263e50e87792dd743a9c941e70ee9c5af7
        content = resp.read()
        print("Body response:$")
        print("\t- type: {}$".format(type(content)))
        print("\t- content: {}$".format(content))
<<<<<<< HEAD
        print("\t- utf8 content: {}$".format(content.decode("utf-8")))
=======
        print("\t- utf8 content: {}$" .format(content.decode('utf-8')))

>>>>>>> 29ec27263e50e87792dd743a9c941e70ee9c5af7

