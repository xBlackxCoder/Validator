#!/usr/bin/python
# -*- coding: utf-8 -*-
#============== Moudles ==============#
import requests
import os, time, random, platform, colorama
from colorama import Fore, Back, Style
from datetime import datetime
from requests import get, Session, post
from concurrent.futures import ThreadPoolExecutor
#============== Moudles ===============#
colorama.init()
#==========================================#
def get_proxy():
    # Choose a random proxy
    lines = open("proxy.txt").read().splitlines()
    proxy = random.choice(lines)
    # Split up the proxy
    proxy_parts = proxy.split(':')

    # Set up the proxy to be used
    proxies = {
        "http": "http://"+str(proxy),
        "https": "https://"+str(proxy),
    }
 
    # Return the proxy
    return proxies
#==========================================#
def find_between(s, first, last):
        try:
            start = s.index(first) + len(first)
            end = s.index(last, start)
            return s[start:end]
        except ValueError:
            return ''
#============ Create Folder ===============#
try:
    os.mkdir('Results')
except:
    pass
#===========================================#
class Bot():
    def Checker(self, i):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "https://telnyx.com/",
            "origin": "https://telnyx.com",
        }
        ProxShit = get_proxy()

        try:
            self.response = get(url="https://api.telnyx.com/anonymous/v2/number_lookup/{_number}".format(_number=i), headers=self.headers, proxies=ProxShit, allow_redirects=False)

            if 'national_format' in self.response.text:
                content = self.response.text
                Carrier = find_between(content,'name":"','"')
                print(Fore.GREEN+'[+] Number: '+ i +' |Carrier: '+Carrier)
                self.save_file = open("Results/"+str(Carrier)+".txt", "a")
                self.save_file.write(f"\n{i}")
                self.save_file.close()
                del self.save_file
                return None
        except Exception as e:
            print('[!] Proxy ERROR')
            self.Checker(i=i)
        else:
            self.save_invalid = open("Results/Invalids.txt", "a")
            self.save_invalid.write(f"\n{i}")
            self.save_invalid.close()
            del self.save_invalid
            return None

if __name__ == '__main__':
    bot = Bot()

    while(True):
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        print(Fore.RED+requests.get("http://artii.herokuapp.com/make?text=Hlr Validator").text)
        print(Fore.GREEN+'By xBlacKx | @xBlackx_Coder | Channel:- @xBlackxCoder')
        print('')

        try:
            inpFile = input("Enter Your Leads File : ")
            threads = []
            with open(inpFile) as NumList:
                argFile = NumList.read().splitlines()
            with ThreadPoolExecutor(max_workers=50) as executor: #Defaulted To 50 threads
                for data in argFile:
                    threads.append(executor.submit(bot.Checker, data))
        except Exception as e:
            print(e)
