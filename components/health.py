from systems.stats import get_stats

class Health():
    def __init__ (self, max=0):
        self.points = max
        
    @property
    def max(self):
        if get_stats(self.owner)['HP'] * 4 > 10:
            return get_stats(self.owner)['HP'] * 4
        else:
            return 10

