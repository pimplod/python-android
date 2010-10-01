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
from android.ota import OTAPackage
from android.tests.mockzip import MockZip
from unittest import TestCase
import random

class TestOTAPackage(TestCase):
    def test_file_not_found(self):
        filename = str(random.randrange(0, 100)) + ".zip"
        self.assertRaises(FileNotFoundException, OTAPackage, filename)

    def test_device(self):
        ota = OTAPackage(MockZip())
        self.assertEquals(ota.device, "passion")

    def test_build_date(self):
        ota = OTAPackage(MockZip())
        self.assertEquals(ota.build_date, "Fri Oct  1 00:28:43 CDT 2010")

    def test_build_host(self):
        ota = OTAPackage(MockZip())
        self.assertEquals(ota.build_host, "localhost")

    def test_build_user(self):
        ota = OTAPackage(MockZip())
        self.assertEquals(ota.build_user, "username")

    def test_modversion(self):
        ota = OTAPackage(MockZip())
        self.assertEqual(ota.modversion, "CyanogenMod-6.1.0-RC0-N1")
