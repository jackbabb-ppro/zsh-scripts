#!./venv/bin/python3

import sys, getopt
from ua_parser import user_agent_parser

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def main(argv):
    if len(argv) < 1:
        print("Usage: useragent \"<pasted user agent>\"")
        print("Results legend:")
        print(color.CYAN + u"\u2588" + " Browser" + color.END)
        print(color.GREEN + u"\u2588" + " Device" + color.END)
        print(color.RED + u"\u2588" + " Operating System" + color.END)
        return
 
    ua_string = argv[0]
        
    # Agent
    ua_agent = user_agent_parser.ParseUserAgent(ua_string)
    agent = ""
    for itm in ua_agent:
        if ua_agent[itm] != None:
            if itm == "minor":
                agent += "."
            agent += ua_agent[itm]
            if itm != "major":
                agent += " "
    
    # Device
    ua_dev = user_agent_parser.ParseDevice(ua_string)
    dev = ""
    for itm in ua_dev:
        if ua_dev[itm] != None:
            dev += ua_dev[itm] + " "
    if dev.strip() == "Other":
        dev = "Unknown Device"

    # OS
    ua_os = user_agent_parser.ParseOS(ua_string)
    os = ""
    for itm in ua_os:
        if ua_os[itm] != None:
            if itm == "minor" or itm == "patch_minor":
                os += "."
            if itm == "family":
                os += " "
            os += ua_os[itm].strip()
    print(color.CYAN + agent.strip() + color.END + " on " + color.RED + os.strip() + color.END + " on " + color.GREEN + dev.strip() + color.END)
if __name__ == "__main__":
    main(sys.argv[1:])
