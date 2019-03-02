class Entity:
    def __init__(self, ai=None, base=None, body=None, equip=None, inv=None, pos=None, skill=None, soul=None, stats=None, status=None):
        self.ai = ai
        self.base = base
        self.body = body
        self.equip = equip
        self.inv = inv
        self.pos = pos
        self.skill = skill
        self.soul = soul
        self.stats = stats
        self.status = status

        if self.ai:
            self.ai.owner = self
        if self.base:
            self.base.owner = self
        if self.body:
            self.body.owner = self
        if self.equip:
            self.equip.owner = self
        if self.inv:
            self.inv.owner = self
        if self.pos:
            self.pos.owner = self
        if self.skill:
            self.skill.owner = self
        if self.soul:
            self.soul.owner = self
        if self.stats:
            self.stats.owner = self
        if self.status:
            self.status.owner = self