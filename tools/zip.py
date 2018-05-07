#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from zipfile import ZipFile

from core.logger import log


class Zip(object):

    chunk_size = 1024 * 1024

    @staticmethod
    def unzip(file_name) -> bool:

        """
               Faz o un-zip do arquivo final
               Peguei de: https://stackoverflow.com/questions/17913952/monitoring-zip-file-extraction-display-percentage-in-python
               :return: bool
        """

        with ZipFile(file_name, 'r') as infile:

            for member_info in infile.infolist():

                filename = member_info.filename
                file_size = member_info.file_size

                with open("{}".format(filename), 'wb') as outfile:

                    member_fd = infile.open(filename)
                    total_bytes = 0

                    while 1:

                        x = member_fd.read(Zip.chunk_size)

                        if not x:
                            break

                        total_bytes += outfile.write(x)

                        log("{0}% extraido".format(100 * total_bytes / file_size))

        return True
