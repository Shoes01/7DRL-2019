class Entity():
    def __init__(self, base=None, pos=None):
        self.base = base
        self.pos = pos

        if self.base:
            self.base.owner = self
        if self.pos:
            self.pos.owner = self