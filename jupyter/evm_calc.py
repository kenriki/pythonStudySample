class ProjectSnapshot:
    bac = 0  # Budget At Completion
    pv = 0  # Planned Value
    ev = 0  # Earned Value
    ac = 0  # Actual Cost

    sv = 0  # Schedule Variance
    cv = 0  # Cost Variance
    cpi = 0  # Cost Performance Index
    spi = 0  # Schedule Performance Index
    eac = 0  # Estimate At Completion
    etc = 0  # Estimate To Complete
    tcpi_bac = 0  # To-complete performance index (BAC)
    tcpi_eac = 0  # To-complete performance index (EAC)
    vac = 0  # Variance At Completion

    def __init__(self, bac, pv, ev, ac):
        self.bac = float(bac)
        self.pv = float(pv)
        self.ev = float(ev)
        self.ac = float(ac)

    def compute_evm(self):
        self.sv = self.ev - self.pv
        self.cv = self.ev - self.ac
        self.cpi = self.ev / self.ac
        self.spi = self.ev / self.pv
        self.eac = self.bac / self.cpi
        self.etc = self.eac - self.ac
        self.tcpi_bac = (self.bac - self.ev) / (self.bac - self.ac)
        self.tcpi_eac = (self.bac - self.ev) / (self.eac - self.ac)
        self.vac = self.bac - self.eac

    def print_status(self):
        print("----")
        print("BAC:" + str(self.bac))
        print("PV:" + str(self.pv))
        print("EV:" + str(self.ev))
        print("AC:" + str(self.ac))
        print("----")
        print("SV:" + str(self.sv))
        print("CV:" + str(self.cv))
        print("CPI:" + str(self.cpi))
        print("SPI:" + str(self.spi))
        print("EAC:" + str(self.eac))
        print("ETC:" + str(self.etc))
        print("TCPI_BAC:" + str(self.tcpi_bac))
        print("TCPI_EAC:" + str(self.tcpi_eac))
        print("VAC:" + str(self.vac))


if __name__ == "__main__":

    bac = input("Please Input [Budget At Completion]:")  # Budget At Completion
    pv = input("Please Input [Planned Value]:")  # Planned Value
    ev = input("Please Input [Earned Value]:")  # Earned Value
    ac = input("Please Input [Actual Cost]:")  # Actual Cost

    p = ProjectSnapshot(bac, pv, ev, ac)
    p.compute_evm()
    p.print_status()
