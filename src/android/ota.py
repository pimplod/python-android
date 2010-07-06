class AndroidOTA(object):
    def __init__(self, filename):
        self.filename = filename
        self.buildprops = {}
        sef.zip = zipfile.ZipFile(filename, "r")
