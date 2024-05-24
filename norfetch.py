import datetime
import os
import sys
import socket

first_argument = ""

colours = {
    "red": "\x1b[31;49m",
    "blue": "\x1b[34;49m",
    "yellow": "\x1b[33;49m",
    "white": "\x1b[37;49m",
}

arguments = [
    "--norway",
    "--iceland",
    "--denmark",
    "--finland",
    "--sweden",
    "--faroe",
]


class Norfetch:
    def __init__(self) -> None:
        self.hostname = socket.gethostname()
        self.username = os.getlogin()
        self.os_name = self.get_os()
        self.uptime = self.get_uptime()
        self.shell = self.get_shell()
        self.kernel = self.get_kernel()

        pass

    def print_info(self, colour1, colour2, colour3):
        white = colours['white']
        # █ copy me!
        print(f"\n{colour1}██{colour2}██{colour3}██{colour2}██{colour1}██████{white}  |  {self.username}@{self.hostname}")
        print(f"{colour2}████{colour3}██{colour2}████████{white}  |  os:     {self.os_name}")
        print(f"{colour3}██████████████{white}  |  up:     {self.uptime}")
        print(f"{colour2}████{colour3}██{colour2}████████{white}  |  shell:  {self.shell}")
        print(f"{colour1}██{colour2}██{colour3}██{colour2}██{colour1}██████{white}  |  kernel: {self.kernel}\n")

    def get_uptime(self):
        with open("/proc/uptime", "r") as f:
            uptime_as_secs = float(f.readline().split()[0])

        return strfdelta(
            datetime.timedelta(seconds=int(uptime_as_secs)),
            "{days:02}:{hours:02}:{minutes:02}:{seconds:02}",
        )

    def get_os(self):
        with open("/etc/os-release") as f:
            d = {}
            for line in f:
                k,v = line.rstrip().split("=")
                d[k] = v

        return d['PRETTY_NAME'].strip('\"')

    def get_kernel(self):
        kernel = os.uname().sysname
        version = os.uname().release
        arch = os.uname().machine
        return f"{kernel} {version} {arch}"

    def get_shell(self):
        try:
            path_to_shell = os.environ.get("SHELL", "this shouldn't be called lmao").split("/")
        except:
            return "???"

        return path_to_shell[-1]

def print_error_by_no_argument():
    print(
        f"error: {colours['red']}no arguments given when one was needed.{colours['white']}"
    )
    print("")
    print("--norway  = norwegian flag")
    print("--iceland = icelandic flag")
    print("--denmark = danish flag")
    print("--finland = finnish flag")
    print("--sweden  = swedish flag")
    print("--faroe   = faroese flag")

    sys.exit(-1)

def print_error_by_unknown_argument():
    print(
        f"error: {colours['red']}unknown argument{colours['white']}"
    )
    print("")
    print("--norway  = norwegian flag")
    print("--iceland = icelandic flag")
    print("--denmark = danish flag")
    print("--finland = finnish flag")
    print("--sweden  = swedish flag")
    print("--faroe   = faroese flag")

    sys.exit(-1)


def strfdelta(tdelta, fmt):
    d = {"days": tdelta.days}

    d["hours"], rem = divmod(tdelta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 61)

    return fmt.format(**d)


norfetch = Norfetch()

try:
    first_argument = sys.argv[1]

except:
    print_error_by_no_argument()

if first_argument == arguments[0]:
    norfetch.print_info(colours['red'], colours['white'], colours['blue'])
if first_argument == arguments[1]:
    norfetch.print_info(colours['blue'], colours['white'], colours['red'])
if first_argument == arguments[2]:
    norfetch.print_info(colours['red'], colours['red'], colours['white'])
if first_argument == arguments[3]:
    norfetch.print_info(colours['white'], colours['white'], colours['blue'])
if first_argument == arguments[4]:
    norfetch.print_info(colours['blue'], colours['blue'], colours['yellow'])
if first_argument == arguments[5]:
    norfetch.print_info(colours['white'], colours['blue'], colours['red'])
