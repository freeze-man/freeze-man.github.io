#!usr/bin/evn python
#Integrating nmap

import nmap
import argparse


# defining nmap scan function with arguments
# tgtHost will hold the host value and tgtPort will hold the port value
def nmapScan(tgtHost, tgtPort):
    nmscan = nmap.PortScanner()
    nmscan.scan(tgtHost, tgtPort)
    state = nmscan[tgt_host]['tcp'][int(tgtPort)]['state']
    print(" [*] " + tgtHost + " tcp/"+tgtPort + " "+state)


def main():
    # setup argument parsing
    parser = argparse.ArgumentParser(description='Command line Argument passing example')
    
    # reading and storing the value for host
    parser.add_argument('--host', action="store", dest="host", required=True)

    # reading and storing the value for port
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)

    given_args = parser.parse_args()
    tgtHost = given_args.host
    tgtPort = given_args.port

    # check if host and port values are not null
    if tgtHost is None or tgtPort is None:
        print(parser.usage)
        exit(0)
    else:
        print("Scanning: " + tgtHost + "-" + str(tgtPort))
        # calling the nmapScan function with the provided values
        nmapScan(tgtHost, str(tgtPort))


if __name__ == '__main__':
    main()


"""
python scan_nmap_argparse.py  --host=127.0.0.1  --port=21
"""