import pexpect


class PtxExpect(pexpect.spawn):
    def __init__(self, driver, logfile=None, timeout=None, cwd=None):
        self.driver = driver
        self.logfile=logfile
        self.linesep = b"\n"
        pexpect.spawn.__init__(
            self, None,
            timeout=timeout,
            cwd=cwd,
            logfile=self.logfile,
        )
    def send(self, s):
        "Write to fd, return number of bytes written"
        s = self._coerce_send_string(s)
        self._log(s, 'send')

        b = s
        return self.driver.write(b)

    def read_nonblocking(self, size=1, timeout=0):
        return self.driver.read(size=size,timeout=timeout)