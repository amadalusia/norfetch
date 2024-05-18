import datetime
import os
import sys
import socket

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
]


class SystemInformation:
    def __init__(self) -> None:
        self.hostname = socket.gethostname()
        self.username = os.getlogin()
        self.uptime = self.get_uptime()
        self.shell = os.environ.get("SHELL", "some shell idk")
        self.kernel = os.uname()

        pass

    def print_info(self):
        arg = ""

        try:
            arg = sys.argv[1]

        except:
            print_error()

        if arg not in arguments:
            print_error()

        if arguments[0] in arg:
            print("")
            print(
                f"{colours['red']}███{colours['white']}██{colours['blue']}██{colours['white']}██{colours['red']}█████████   user:    {self.username}"
            )
            print(
                f"{colours['white']}█████{colours['blue']}██{colours['white']}███████████   host:    {self.hostname}"
            )
            print(f"{colours['blue']}██████████████████   up:      {self.uptime}")
            print(
                f"{colours['white']}█████{colours['blue']}██{colours['white']}███████████   shell:   {self.shell}"
            )
            print(
                f"{colours['red']}███{colours['white']}██{colours['blue']}██{colours['white']}██{colours['red']}█████████   kernel:  {self.kernel.sysname} {self.kernel.release} {self.kernel.machine}"
            )

        if arguments[1] in arg:
            print(
                f"{colours['blue']}███{colours['white']}██{colours['red']}██{colours['white']}██{colours['blue']}█████████   user:    {self.username}"
            )
            print(
                f"{colours['white']}█████{colours['red']}██{colours['white']}███████████   host:    {self.hostname}"
            )
            print(f"{colours['red']}██████████████████   up:      {self.uptime}")
            print(
                f"{colours['white']}█████{colours['red']}██{colours['white']}███████████   shell:   {self.shell}"
            )
            print(
                f"{colours['blue']}███{colours['white']}██{colours['red']}██{colours['white']}██{colours['blue']}█████████   kernel:  {self.kernel.sysname} {self.kernel.release} {self.kernel.machine}"
            )
        if arguments[2] in arg:
            print(
                f"{colours['red']}█████{colours['white']}██{colours['red']}███████████   user:    {self.username}"
            )
            print(
                f"{colours['red']}█████{colours['white']}██{colours['red']}███████████   host:    {self.hostname}"
            )
            print(f"{colours['white']}██████████████████   up:      {self.uptime}")
            print(
                f"{colours['red']}█████{colours['white']}██{colours['red']}███████████   shell:   {self.shell}"
            )
            print(
                f"{colours['red']}█████{colours['white']}██{colours['red']}███████████   kernel:  {self.kernel.sysname} {self.kernel.release} {self.kernel.machine}"
            )
        if arguments[3] in arg:
            print(
                f"{colours['white']}█████{colours['blue']}██{colours['white']}███████████   user:    {self.username}"
            )
            print(
                f"{colours['white']}█████{colours['blue']}██{colours['white']}███████████   host:    {self.hostname}"
            )
            print(f"{colours['blue']}██████████████████   up:      {self.uptime}")
            print(
                f"{colours['white']}█████{colours['blue']}██{colours['white']}███████████   shell:   {self.shell}"
            )
            print(
                f"{colours['white']}█████{colours['blue']}██{colours['white']}███████████   kernel:  {self.kernel.sysname} {self.kernel.release} {self.kernel.machine}"
            )
        if arguments[4] in arg:
            print(
                f"{colours['blue']}█████{colours['yellow']}██{colours['blue']}███████████   user:    {self.username}"
            )
            print(
                f"{colours['blue']}█████{colours['yellow']}██{colours['blue']}███████████   host:    {self.hostname}"
            )
            print(f"{colours['yellow']}██████████████████   up:      {self.uptime}")
            print(
                f"{colours['blue']}█████{colours['yellow']}██{colours['blue']}███████████   shell:   {self.shell}"
            )
            print(
                f"{colours['blue']}█████{colours['yellow']}██{colours['blue']}███████████   kernel:  {self.kernel.sysname} {self.kernel.release} {self.kernel.machine}"
            )

    def get_uptime(self):
        with open("/proc/uptime", "r") as f:
            uptime_as_secs = float(f.readline().split()[0])

        return strfdelta(
            datetime.timedelta(seconds=int(uptime_as_secs)),
            "{days:02}:{hours:02}:{minutes:02}:{seconds:02}",
        )


def print_error():
    print(
        f"error: {colours['red']}no arguments given when one was needed.{colours['white']}"
    )
    print("")
    print("--norway  = norwegian flag")
    print("--iceland = icelandic flag")
    print("--denmark = danish flag")
    print("--finland = finnish flag")
    print("--sweden  = swedish flag")

    sys.exit(-1)


def strfdelta(tdelta, fmt):
    d = {"days": tdelta.days}

    d["hours"], rem = divmod(tdelta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 61)

    return fmt.format(**d)


norfetch = SystemInformation()

norfetch.print_info()
