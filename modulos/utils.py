class Package:
    MAX_DATA_SIZE = 900
    NUMBER_OF_RETRIES = 5
    def __init__(self, seq, ack, is_ack, is_syn, is_end, data=b'', is_fin_1=False, is_fin_2=False):
        self.seq = seq
        self.ack = ack
        self.is_ack = is_ack
        self.is_syn = is_syn
        self.is_end = is_end
        self.is_fin_1 = is_fin_1
        self.is_fin_2 = is_fin_2
        self.data = data

    def content(self):
        return self.data

    def encode(self):
        package = '{0:032b}'.format(self.seq)
        package += '{0:032b}'.format(self.ack)
        package += '{0:01b}'.format(self.is_ack)
        package += '{0:01b}'.format(self.is_syn)
        package += '{0:01b}'.format(self.is_end)
        package += '{0:01b}'.format(self.is_fin_1)
        package += '{0:01b}'.format(self.is_fin_2)
        package += self.data.decode()
        return package.encode()

    @staticmethod # this function behaves like a plain function
    def decode(package):
        package = package.decode()
        seq = int(package[0:32], 2)
        ack = int(package[32:64], 2)
        is_ack = bool(int(package[64:65]))
        is_syn = bool(int(package[65:66]))
        is_end = bool(int(package[66:67]))
        is_fin_1 = bool(int(package[67:68]))
        is_fin_2 = bool(int(package[68:69]))
        data = package[69:].encode()
        return Package(seq, ack, is_ack, is_syn, is_end, data, is_fin_1, is_fin_2)
