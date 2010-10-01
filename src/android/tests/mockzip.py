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
