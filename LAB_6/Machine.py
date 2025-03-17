class Machine:
    def __init__(self, productivity, price, detail_price):
        self.productivity = productivity
        self.price = price
        self.det_pr = detail_price

    def benefit_det_count(self):
        return round(self.price/self.det_pr)
    
    def benefit_time(self):
        if self.productivity > 0:
            return self.benefit_det_count()/self.productivity
        
    def __str__(self):
        return (f"Machine(productivity={self.productivity}, "
                f"price={self.price}, "
                f"detail_price={self.det_pr})")


class MillingMachine(Machine):
    def __init__(self, productivity, price, detail_price, cutter_diameter, detail_size):
        super().__init__(productivity, price, detail_price)
        self.cut_d = cutter_diameter
        self.det_s = detail_size
    
    def step_count(self):
        return round((self.det_s[0]* self.det_s[1]) / self.cut_d)
    
    def __str__(self):
        return (f"Milling Machine(productivity={self.productivity}, "
                f"price={self.price}, "
                f"detail_price={self.det_pr}"
                f"cutter_diameter={self.cut_d}"
                f"detail_size={self.det_s})")


class CNCMachine(Machine):
    def __init__(self, productivity, price, detail_price, accuracy_class, reliability): # надежность вычисляется в процентах
        super().__init__(productivity, price, detail_price)
        self.acc_cls = accuracy_class
        self.rlb = reliability

    def defect_det_percent(self):
        return 100-self.rlb

    def __str__(self):
        return (f"CNC Machine {self.acc_cls}(productivity={self.productivity}, "
                f"price={self.price}, "
                f"detail_price={self.det_pr}" 
                f"reliability={self.rlb}%" 
                f"defect={self.defect_det_percent()}%)")
    

if __name__ == '__main__':
    mmachine = MillingMachine(250, 2000000, 120, 2, (15, 30))
    cncmachine = CNCMachine(450, 3400000, 230, 'А', 79)

    print(mmachine)
    print(cncmachine)

