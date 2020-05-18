import logging
import uuid
from abc import ABCMeta, abstractmethod
from io import BytesIO
from pathlib import Path

import requests


class FileAbstract(metaclass=ABCMeta):

    @property
    @abstractmethod
    def path(self) -> str:
        """System path to file"""

    @abstractmethod
    def load(self):
        """Load file from source"""


class WebFile(FileAbstract):
    def __init__(self, path, destination):
        self.__path = path
        self.__file = None
        self.__binary = BytesIO()
        self._destination = destination
        self._filename = ''

    def load(self):
        resp = requests.get(self.__path)
        if resp.status_code == 200:
            self.__binary.write(resp.content)
            logging.info('File has been loaded')
            return
        logging.warning('Invalid response')

    def path(self) -> str:
        if not self.__file:
            if self.__binary.getbuffer().nbytes == 0:
                self.load()

            filepath = f'{self.destination}/{self.filename}'
            self.__file = open(filepath, 'wb')
            self.__file.write(self.__binary.getbuffer())
            self.__file.close()

        return self.__file.name

    @property
    def destination(self) -> str:
        """Return destination path and create if not exist"""
        Path(self._destination).mkdir(parents=True, exist_ok=True)
        return self._destination

    @property
    def filename(self):
        if not self._filename:
            self._filename = uuid.uuid4().hex + 'txt'
        return self._filename


some_file = WebFile(
    path='https://raw.githubusercontent.com/aodarc/lits-13/master/homework/Roman/task_06/task_06.py',
    destination='data/downloads'
)

if __name__ == '__main__':
    print(some_file.path())
