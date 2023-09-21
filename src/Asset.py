class Asset:

    def __init__(self, fund) -> None:
        self.fund = fund
        self.num_unit = 0

    def set_num_unit(self, num_unit):
        self.num_unit = num_unit