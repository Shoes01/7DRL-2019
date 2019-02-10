class Entity():
    def __init__(self, ai=None, base=None, pos=None):
        self.ai = ai
        self.base = base
        self.pos = pos

        if self.ai:
            self.ai.owner = self
        if self.base:
            self.base.owner = self
        if self.pos:
            self.pos.owner = self