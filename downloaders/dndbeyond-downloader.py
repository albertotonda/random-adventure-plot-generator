# Simple Python script to download all names of TV tropes (along with a link, maybe)
# and save them to a .csv file
# by Alberto Tonda, 2020 <alberto.tonda@gmail.com>

import os
import re as regex
import selenium
import sys
import time
import urllib.request

# selenium is a module used to drive a browser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException

def get_html_from_page(url) :

    request = urllib.request.Request(url, headers={'User-Agent': 'Chrome/76.0.3809.132'})
    response = urllib.request.urlopen(request)
    htmlBytes = response.read()
    html = htmlBytes.decode("utf8")
        
    return html

def main() :

    output_file = "../monsters/dndbeyond.csv"
    current_webpage_url = "https://www.dndbeyond.com/monsters?page="
    current_webpage_number = 1
    next_link_exists = True

    # initialize output file
    with open(output_file, "w") as fp : fp.write("name\n") # TODO: NAME, TYPE, ALIGNMENT?

    # read html of the first page 
    html = get_html_from_page(current_webpage_url + str(current_webpage_number))

    while next_link_exists :

        # read html
        print("Working on page #%d, \"%s\"..." % (current_webpage_number, current_webpage_url))

        # get all names and urls for the monsters listed
        matches = regex.findall("<div class=\"row monster-name\">[\s]+<span class=\"name\">[\s]+<a class=\"link\" href=\"/monsters/.*?\">(.*?)</a>", html)

        print("Found a total of %d matches, writing to file \"%s\"" % (len(matches), output_file))
        for m in matches : print("\t\"%s\"" % m)

        # open the output file and add at the end
        with open(output_file, "a") as fp :
            for m in matches :
                fp.write("\"%s\"\n" % (m))

        # wait a few seconds
        time.sleep(1)

        # read html of the next page
        current_webpage_number += 1
        html = get_html_from_page(current_webpage_url + str(current_webpage_number))
        if current_webpage_number == 90 : next_link_exists = False

    return

if __name__ == "__main__" :
    sys.exit( main() )
