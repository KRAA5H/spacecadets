###
# Reading and Writing Strings from Files and URLs
#
# Have a look at the Web page at https://www.ecs.soton.ac.uk/people/dem.
# This is a departmental information page which gives all sorts of information
# about a member of staff. The Web address is constructed from a departmental
# email id (in this case 'dem'). If you have someone else's email id, you can
# look up their name from one of these Web pages. Try it with your own email id.
#
# In fact, in the past the name started at the 12th character of the 6th line
# of the HTML data returned by the Web server. It finishes when a '<' character
# appears. (Choose 'View Source' from your Web browser to check where it is now.)
###

from bs4 import BeautifulSoup
import requests, re


def username():
    dem = input("What is your departmental email address?")
    if re.search(r'@soton\.ac\.uk$', dem):
        dem = dem.split('@')[0]
    return dem

def req(dem):
    r = requests.get(f'https://www.southampton.ac.uk/people/{dem}')
    r.encoding = r.content
    return r.text

def main():
    soup = BeautifulSoup(req(username()), 'html.parser')
    
    title_str = soup.title.string
    if not title_str.startswith("Find"):
        print(f"Hi, {title_str.split('|')[0].strip()}!")

main()
