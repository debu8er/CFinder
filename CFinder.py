import os
import argparse
import re
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print (bcolors.FAIL + "  ____ _____ _           _")
print (bcolors.FAIL + " / ___|  ___(_)_ __   __| | ___ _ __")
print (bcolors.OKGREEN + "| |   | |_  | | '_ \ / _` |/ _ \ '__|")
print (bcolors.ENDC + "| |___|  _| | | | | | (_| |  __/ |")
print (bcolors.OKBLUE + " \____|_|   |_|_| |_|\__,_|\___|_|")
time.sleep(1)
print(bcolors.BOLD+"********** Made by debug **********\n")



parser = argparse.ArgumentParser(description="CFinder is a tool for get CIDR throught domain")

parser.add_argument("-d", "--domain",
                    help='domain input.')

parser.add_argument("-f", "--filename",
                    help='file input.')

options = parser.parse_args()

filename = options.filename
domain = options.domain



def domain_Whoiser():

    os.system(f"""\
    for domain in $(subfinder -d {domain} -silent); do 
        for IP in $(echo $domain | dnsx -a -resp -silent | sed 's/.*\[//;s/\]//'); do
            asn_name=$(curl -s https://api.bgpview.io/ip/$IP | jq -r '.data.prefixes[] | "{{ip}} \(.asn.name)"' | sed "s/{{ip}}/$IP/")
            echo $asn_name
        done
    done  >> {domain.split('.')[0]}
    """)

    f = open(f"{domain.split('.')[0]}","r")
    for i in f:
        if set(domain.split('.')[0]).issubset(set(i.lower())):
            ip_match = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", i).group()
            os.system(f"curl -s https://api.bgpview.io/ip/{ip_match} | jq -r '.data.prefixes[].prefix' >> CIDR")
    
    os.system("cat CIDR | sort -u")
    

def file_Whoiser():
    f = open(filename, "r")
    for t in f:
        t.replace("\n", "")
        match = re.match(r"https?://([a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,})(?:$|/)", t)
        
        if match:
            sub = match.group(1)

            os.system(f"""\
                for domain in $(subfinder -d {sub} -silent); do 
                    for IP in $(echo $domain | dnsx -a -resp -silent | sed 's/.*\[//;s/\]//'); do
                        asn_name=$(curl -s https://api.bgpview.io/ip/$IP | jq -r '.data.prefixes[] | "{{ip}} \(.asn.name)"' | sed "s/{{ip}}/$IP/")
                        echo $asn_name
                    done
                done  > {sub.split('.')[0]}
                """)

            f = open(f"{sub.split('.')[0]}","r")
            for i in f:
                if set(sub.split('.')[0]).issubset(set(i.lower())):
                    ip_match = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", i).group()
                    os.system(f"curl -s https://api.bgpview.io/ip/{ip_match} | jq -r '.data.prefixes[].prefix' >> CIDR")
            
    os.system("cat CIDR | sort -u")
            




if options.filename != None:
    if os.path.exists('IP-Whoiser'):
        file_Whoiser()
    elif not os.path.exists("IP-Whoiser"):
        os.mkdir("IP-Whoiser")
        file_Whoiser()

elif options.domain != None:
    if os.path.exists('IP-Whoiser'):
        domain_Whoiser()
    elif not os.path.exists("IP-Whoiser"):
        os.mkdir("IP-Whoiser")
        domain_Whoiser()