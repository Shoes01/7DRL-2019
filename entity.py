class Entity:
    def __init__(self, ai=None, base=None, body=None, equip=None, health=None, inv=None, job=None, pos=None, race=None, rank=None, skill=None, soul=None, stats=None, status=None):
        self.ai = ai
        self.base = base
        self.body = body
        self.equip = equip
        self.health = health
        self.inv = inv
        self.job = job
        self.pos = pos
        self.race = race
        self.rank = rank
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
        if self.health:
            self.health.owner = self
        if self.inv:
            self.inv.owner = self
        if self.job:
            self.job.owner = self
        if self.pos:
            self.pos.owner = self
        if self.race:
            self.race.owner = self
        if self.rank:
            self.rank.owner = self
        if self.skill:
            self.skill.owner = self
        if self.soul:
            self.soul.owner = self
        if self.stats:
            self.stats.owner = self
        if self.status:
            self.status.owner = self