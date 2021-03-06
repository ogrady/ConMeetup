import datetime
import time

class Logger(object):
    def __init__(self, filename, mode = "a"):
        self._fh = open(filename, mode)

    def error(self, message):
        self._write("ERROR", message)

    def info(self, message):
        self._write("INFO", message)

    def close(self):
        self._fh.flush()
        self._fh.close()

    def _write(self, header, message):
        ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        self._fh.write("[%s] %s: %s \n" % (header, ts, message))
        self._fh.flush()