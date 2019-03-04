from systems.stats import get_stats

class Health():
    def __init__ (self, max=0):
        self.points = max
        
    @property
    def max(self):
        return get_stats(self.owner)['HP'] * 4
