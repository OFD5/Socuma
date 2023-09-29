import argparse
import requests
from bs4 import BeautifulSoup
from termcolor import colored
import time

author_info = f"""
Author: {colored("OFD5", "yellow")}
GitHub: {colored("https://github.com/OFD5", "yellow")}
Contact me: {colored("OFD5@safepayload.co.za", "yellow")}

{colored("[WRN] [======WARNING: Conducting Reconnaissance=====]", "yellow")}
{colored("[WRN] Use with caution. You are responsible for your actions", "yellow")}
{colored("[WRN] Developers assume no liability and are not responsible for any misuse or damage", "yellow")}
{colored("[WRN] Always ensure that you have proper authorization to access and collect information about individuals or entities.", "blue")}
"""

def display_banner():
    banner = """
  ____                                   
 / ___|  ___   ___ _   _ _ __ ___   __ _ 
 \___ \ / _ \ / __| | | | '_ ` _ \ / _` |
  ___) | (_) | (__| |_| | | | | | | (_| |
 |____/ \___/ \___|\__,_|_| |_| |_|\__,_|

            Safepayload.co.za                           
        """
    print(colored(banner, "cyan"))
    print(author_info)

def find_profile(username, timeout=10):
    platforms = {
        "GitHub": f"https://github.com/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}",
        "LinkedIn": f"https://za.linkedin.com/in/{username}",
        "YouTube": f"https://www.youtube.com/user/{username}",
        "Facebook": f"https://m.facebook.com/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Snapchat": f"https://www.snapchat.com/add/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}",
        "Vimeo": f"https://vimeo.com/{username}",
        "Facebook Messenger": f"https://m.me/{username}",
        "HackerOne": f"https://hackerone.com/{username}",
        "Bugcrowd": f"https://bugcrowd.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Stack Exchange": f"https://stackexchange.com/users/{username}",
        "Medium": f"https://medium.com/{username}",
        "Twitch": f"https://www.twitch.tv/{username}",
        "Periscope": f"https://www.pscp.tv/{username}",
        "Tinder": f"https://tinder.com/@{username}",
        "SoundCloud": f"https://soundcloud.com/{username}",
        "TripAdvisor": f"https://www.tripadvisor.com/members/{username}",
        "Wanelo": f"https://wanelo.co/{username}",
        "Spotify": f"https://open.spotify.com/user/{username}",
        "Steam Community": f"https://steamcommunity.com/id/{username}",
        "ResearchGate": f"https://www.researchgate.net/profile/{username}",
        # Add other websites to check for usernames here.
    }

    for platform, url in platforms.items():
        try:
            response = requests.get(url, timeout=timeout)
            if response.status_code == 200:
                if "The profile you're looking for can't be found" in response.text:
                    print(colored(f"[X] {platform} Profile Not Found", "red"))
                elif "hasn't saved any items yet." in response.text:
                    print(colored(f"[!] {platform} User Found (No saved items):", "yellow"), url)
                else:
                    print(colored(f"[+] {platform} Profile Found:", "green"), url)
            else:
                print(colored(f"[-] {platform} No Usernames", "red"))
        except requests.exceptions.RequestException:
            print(f"[-] {platform} Profile Not Found")  # No color for errors

def check_wanelo_profile(username, timeout=10):
    url = f"https://wanelo.co/{username}"
    try:
        response = requests.get(url, timeout=timeout)
        if response.status_code == 200:
            if "The profile you're looking for can't be found" in response.text:
                print(colored(f"[X] Wanelo Profile Not Found", "red"))
            elif "hasn't saved any items yet." in response.text:
                print(colored(f"[!] Wanelo User Found (No saved items):", "yellow"), url)
            else:
                print(colored(f"[+] Wanelo Profile Found:", "green"), url)
        else:
            print(colored(f"[-] Wanelo No Usernames", "red"))
    except requests.exceptions.RequestException:
        print(f"[-] Wanelo Profile Not Found")  # No color for errors

def check_instagram_profile(username, timeout=10):
    url = f"https://www.instagram.com/{username}"
    try:
        response = requests.get(url, timeout=timeout)
        if response.status_code == 200:
            if "Sorry, this page isn't available." in response.text:
                print(colored(f"[X] Instagram No Username", "red"))
            else:
                print(colored(f"[+] Instagram Profile Found:", "green"), url)
        else:
            print(colored(f"[-] Instagram No Usernames", "red"))
    except requests.exceptions.RequestException:
        print(f"[-] Instagram Profile Not Found")  # No color for errors

def check_bugcrowd_profile(username, timeout=10):
    url = f"https://bugcrowd.com/{username}"
    try:
        response = requests.get(url, timeout=timeout)
        if response.status_code == 200:
            if "The requested page was not found" in response.text:
                print(colored(f"[X] Bugcrowd Profile Not Found", "red"))
            else:
                print(colored(f"[+] Bugcrowd Profile Found:", "green"), url)
        else:
            print(colored(f"[-] Bugcrowd No Usernames", "red"))
    except requests.exceptions.RequestException:
        print(f"[-] Bugcrowd Profile Not Found")  # No color for errors

def check_facebook_profile(username, timeout=10):
    url = f"https://m.facebook.com/{username}"
    try:
        response = requests.get(url, timeout=timeout)
        if response.status_code == 200:
            if "The link you followed may be broken, or the page may have been removed." in response.text:
                print(colored(f"[X] Facebook No Username", "red"))
            else:
                print(colored(f"[+] Facebook Profile Found:", "green"), url)
        else:
            print(colored(f"[-] Facebook No Usernames", "red"))
    except requests.exceptions.RequestException:
        print(f"[-] Facebook Profile Not Found")  # No color for errors

def check_spotify_profile(username, timeout=10):
    url = f"https://open.spotify.com/user/{username}"
    try:
        response = requests.get(url, timeout=timeout)
        if response.status_code == 200:
            if "Page not found" in response.text:
                print(colored(f"[X] Spotify Profile Not Found", "red"))
            else:
                print(colored(f"[+] Spotify Profile Found:", "green"), url)
        else:
            print(colored(f"[-] Spotify No Usernames", "red"))
    except requests.exceptions.RequestException:
        print(f"[-] Spotify Profile Not Found")  # No color for errors

def check_tiktok_profile(username, timeout=10):
    url = f"https://www.tiktok.com/@{username}"
    try:
        response = requests.get(url, timeout=timeout)
        if response.status_code == 200:
            if "Check out more trending videos on TikTok" in response.text:
                print(colored(f"[X] TikTok Profile Not Found", "red"))
            else:
                print(colored(f"[+] TikTok Profile Found:", "green"), url)
        else:
            print(colored(f"[-] TikTok No Usernames", "red"))
    except requests.exceptions.RequestException:
        print(f"[-] TikTok Profile Not Found")  # No color for errors

def check_steam_profile(username, timeout=10):
    url = f"https://steamcommunity.com/id/{username}"
    try:
        response = requests.get(url, timeout=timeout)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            profile_name = soup.find('span', class_='actual_persona_name')
            if profile_name and profile_name.text.strip() == username:
                print(colored(f"[+] Steam Community Profile Found:", "green"), url)
            else:
                no_profile_message = soup.find('div', class_='profile_no_content')
                if no_profile_message and "This user has not yet set up their Steam Community profile." in no_profile_message.text:
                    print(colored(f"[X] Steam Community Profile Not Found: This user has not yet set up their Steam Community profile.", "red"))
                else:
                    print(colored(f"[X] Steam Community Profile Not Found", "red"))
        else:
            print(colored(f"[-] Steam Community No Usernames", "red"))
    except requests.exceptions.RequestException:
        print(f"[-] Steam Community Profile Not Found")



if __name__ == "__main__":
    display_banner()
    parser = argparse.ArgumentParser(description="OSINT Tool for Finding Profiles by Username")
    parser.add_argument("-u", metavar="U", help="Specify username")
    parser.add_argument("-f", metavar="F", help="Specify a file containing username list")
    parser.add_argument("-l", metavar="L", help="Specify multiple comma-separated usernames")
    parser.add_argument("-t", metavar="T", type=int, default=10, help="Specify timeout [Default : 10]")
    parser.add_argument("-v", action="store_true", help="Prints version")
    parser.add_argument("-U", action="store_true", help="Check for Updates")
    parser.add_argument("-pm", metavar="PM", choices=["single", "file"], default="single", help="Proxy mode [Available: single, file] [Default: single]")
    parser.add_argument("-proto", metavar="PROTO", choices=["http", "https"], default="http", help="Proxy protocol [Available: http, https] [Default: http]")
    parser.add_argument("-ph", metavar="PH", help="Proxy Hostname")
    parser.add_argument("-pp", metavar="PP", help="Proxy port")

    args = parser.parse_args()

    if args.u:
        find_profile(args.u, args.t)
    elif args.f:
        with open(args.f, "r") as file:
            usernames = file.read().splitlines()
            for username in usernames:
                print(f"Scanning username: {username}")
                find_profile(username, args.t)
                print()  # Add an empty line to separate results for different usernames
    elif args.l:
        usernames = args.l.split(",")
        for username in usernames:
            print(colored(f"Scanning username: {username}","blue" ))
            find_profile(username.strip(), args.t)
            print()  # Add an empty line to separate results for different usernames
    else:
        parser.print_help()

    # Add a delay to keep the output visible before exiting
    time.sleep(5)
 