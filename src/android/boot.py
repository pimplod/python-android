import struct
from binascii import hexlify

class BootImage(object):
    def __init__(self, filename="boot.img"):
        self._fd = open(filename, "r")
        self._header = self._fd.read(584)
        
        self._loadInfo()
        
    def _loadInfo(self):
        header = struct.unpack("<8s8I8s16s512s8s", self._header)
        
        self.magic = header[0]
        self.kernel_size = header[1]
        self.kernel_addr = header[2] - 0x00008000
        self.ramdisk_size = header[3]
        self.ramdisk_addr = header[4] - 0x01000000
        self.stage2_size = header[5]
        self.sage2_addr = header[6] - 0x00F00000
        self.tags_addr = header[7] - 0x00000100
        self.page_size = header[8]
        self.unused = header[9]
        self.name = header[10]
        self.cmdline = header[11]
        self.checksum = hexlify(header[12]).upper()
        
    def getKernelBase(self):
        return str("%#x" % self.kernel_addr)
    
    def getRamdiskBase(self):
        return str("%#x" % self.ramdisk_addr)
    
if __name__ == '__main__':
    bi = BootImage()
    print bi.getKernelBase()