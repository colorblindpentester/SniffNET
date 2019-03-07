#!/usr/bin/python
import os
import shodan
import time
import sys
class color:
    HEADER = '\033[0m'

logo = color.HEADER + '''
==========================================================
 dP"8         ,e,  dP,e,  dP,e, Y88b Y88           d8
C8b Y 888 8e   "   8b "   8b "   Y88b Y8  ,e e,   d88
 Y8b  888 88b 888 888888 888888 b Y88b Y d88 88b d88888
b Y8D 888 888 888  888    888   8b Y88b  888   ,  888
8edP  888 888 888  888    888   88b Y88b  "YeeP"  888
   
Sniffnet is a toolkit what is going to help you hacking in
the global web. Tools: sqlmap, nikto, nmap, shodan, ping, 
adminpagefinder, ngrok, BeEF.
Telegram: https://t.me/reverseengineeringg
==========================================================
'''
print(logo)
print("Hi")
website = input ("Enter a website or a IP to test: ")
webport = input ("Enter a port to scan ((For Nikto) If you want to scan many ports enter: **,***,****): ")
os.system("clear")
print ('\x1b[1;32;40m' +' Enter 1 to scan it with NMAP, NIKTO''\x1b[0m')
print ('\x1b[1;32;40m' +' Enter 2 to try SQL injection with SQLMAP''\x1b[0m')
print ('\x1b[1;32;40m' +' Enter 3 to start BeEF Framework''\x1b[0m')
print ('\x1b[1;32;40m' +' Enter 4 to ping the target''\x1b[0m')
print ('\x1b[1;32;40m' +' Enter 5 to start ngrok''\x1b[0m')
print ('\x1b[1;32;40m' +' Enter 6 to use AdminPageFinder (By nu11-v0!''\x1b[0m')
print ('\x1b[1;32;40m' +' Enter 7 to use shodan search''\x1b[0m')
attack = input ("What do you want to use: ")
os.system("clear")
if attack =="1":
    os.system("clear")
    print(logo)
    os.system("nmap -A -Pn %s" % website)
    os.system("nikto -h %s -p %s" % (website, webport))
    print("Done scanning")

if attack =="2":
    print(logo)
    os.system("sqlmap -u %s --dbs --random-agent --tor --check-tor")
    print(" If it founds any data base, do the dumping your self")

if attack=="3":
    os.system("clear")
    print(logo)
    os.system("beef-xss")

if attack=="4":
    os.system("clear")
    print(logo)
    os.system("ping %s" % website)

if attack=="5":
    os.system("clear")
    print(logo)
    ngrokport = input(" Enter port for ngrok (if need): ")
    os.system("ngrok http %s" % ngrokport)
if attack=="6":
    os.system("clear")
    print(logo)
    os.system("perl AdminFinder.pl")

if attack =="7":
    os.system("clear")
    print(logo)
    shodansearch = input ("What do you want to search? ")
    shodanaAPI = input ("Enter a shodan API key: ")
    os.system("shodan input %s" % shodanaAPI)
    os.system("shodan search %s" % shodansearch)
print(logo)




