# python-android
# Copyright (C) 2010 Chris Soyars
#
# This progream is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the license, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from android.exc import FileNotFoundException
from android.tests.mockzip import MockZip
import os.path
import re
import zipfile

RE_BUILDPROP = re.compile(r'^(.*)=(.*)$')

class OTAPackage(object):
    def __init__(self, file):
        self.file = file
        self.test = False

        if isinstance(file, MockZip):
            self.test = True

        if not self.test and not os.path.exists(self.file):
            raise FileNotFoundException("File '%s' not found!" % self.file)

        self._loadfile()
        self._load_buildprop()

    def _loadfile(self):
        if self.test:
            self.fd = self.file
        else:
            self.fd = zipfile.ZipFile(self.file)

    def _load_buildprop(self):
        bp = self.fd.read("system/build.prop")
        self.fd.close()

        self.build_prop = {}

        bp = bp.split("\n")
        for line in bp:
            m = RE_BUILDPROP.match(line)
            if m:
                self.build_prop.update({
                    m.group(1): m.group(2)
                })

    @property
    def size(self):
        return self.getSize()

    @property
    def device(self):
        return self.getDevice()

    @property
    def build_date(self):
        return self.getBuildDate()

    @property
    def build_host(self):
        return self.getBuildHost()

    @property
    def build_user(self):
        return self.getBuildUser()

    @property
    def modversion(self):
        return self.getModVersion()

    def getSize(self):
        return os.path.getsize(self.file)

    def getModVersion(self):
        return self.build_prop.get('ro.modversion', None)

    def getBuildUser(self):
        return self.build_prop.get('ro.build.user', None)

    def getBuildHost(self):
        return self.build_prop.get('ro.build.host', None)

    def getDevice(self):
        return self.build_prop.get('ro.product.device', None)

    def getBuildDate(self):
        return self.build_prop.get('ro.build.date', None)

if __name__ == '__main__':
    ab = OTAPackage("/home/ctso/cm.zip")
