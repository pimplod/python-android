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
