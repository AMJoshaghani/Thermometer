class Worker:
    def __init__(self, dt, dx):
        self.T = None
        self.dt = dt
        self.dx = dx

    def evaluate_temperature(self):
        v = self.evaluate_velocity()
        self.T = 273 * ((v/331)**2 - 1)

    def evaluate_velocity(self):
        return self.dx / self.dt

    def temperature(self, unit):
        if unit == 'K':
            return self.T
        elif unit == 'C':
            return self.temperature('K') - 273
        elif unit == 'F':
            return self.temperature('C') * 9/5 + 32
        else:
            return "Unknown unit."
