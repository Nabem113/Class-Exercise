class Physics:

    def velocity(self, displacement, time):
        result = displacement/time
        return result

    def momentum(self, mass, velocity):
        result = mass * velocity
        return result

    def weight(self, mass, acceleration):
        result = mass * acceleration
        return result

    def workdone(self, force, distance):
        result = force * distance
        return result

    def density(self, mass, volume):
        result = mass / volume
        return result

