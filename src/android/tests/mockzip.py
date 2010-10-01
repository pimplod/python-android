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

BUILDPROP = """# begin build properties
ro.build.date=Fri Oct  1 00:28:43 CDT 2010
ro.build.date.utc=0
ro.build.host=localhost
ro.build.user=username
ro.product.device=passion
ro.modversion=CyanogenMod-6.1.0-RC0-N1
"""

class MockZip(object):
    def read(self, path):
        return BUILDPROP

    def close(self):
        pass
