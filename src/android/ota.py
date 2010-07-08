from android.exc import NoFilenameException
import zipfile

class FileNotOpenedException():
    pass

class AndroidOTA(object):
    def __init__(self, filename = None):
        self.filename = filename
        self.buildprops = {}
    
    def open(self, filename = None):
        if filename:
            fn = self.filename = filename
        elif self.filename:
            fn = self.filename
        else:
            raise NoFilenameException()
        
        if fn:
            self.zip = zipfile.ZipFile(fn, "r")
    
    def getBuildProp(self, key):
        if self.buildprop == {} and self.zip:
            f = self.zip.open("system/build.prop").read()
            
            for line in [x.split("=") for x in f.split("\n")]:
                if len(line) == 2:
                    self.buildprop[line[0]] = line[1]
                    
            value = self.buildprop.get(key, None)
            if value:
                return value
            else:
                raise KeyError()
        else:
            raise FileNotOpenedException()
        
    def getModVersion(self):
        return self.getBuildProp("ro.modversion")
    
    def getDevice(self):
        return self.getBuildProp("ro.product.device")

if __name__ == "__main__":
    ota = AndroidOTA()
    ota.open()
    ota.getModVersion()