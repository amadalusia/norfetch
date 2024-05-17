import datetime
import os
import socket

colours = {
    "red": "\x1b[31;49m",
    "blue": "\x1b[34;49m",
    "white": "\x1b[37;49m",
}


class SystemInformation:
    def __init__(self) -> None:
        self.hostname = socket.gethostname()
        self.username = os.getlogin()
        self.uptime = self.get_uptime()
        self.shell = os.environ.get("SHELL", "some shell idk")
        self.kernel = os.uname()

        pass

    def print_info(self):
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

    def get_uptime(self):
        with open("/proc/uptime", "r") as f:
            uptime_as_secs = float(f.readline().split()[0])

        return strfdelta(
            datetime.timedelta(seconds=int(uptime_as_secs)),
            "{days:02}:{hours:02}:{minutes:02}:{seconds:02}",
        )


def strfdelta(tdelta, fmt):
    d = {"days": tdelta.days}

    d["hours"], rem = divmod(tdelta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 61)

    return fmt.format(**d)


norfetch = SystemInformation()

norfetch.print_info()
