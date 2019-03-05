import numpy as np

def get_stats(entity, job=None, race=None, soul=None):
    if entity is not None:
        soul = entity.soul.soul.copy()
        soul += entity.race.value.get('bonus')
        soul = soul.reshape(6).tolist()
        soul.sort(reverse=True)
        
        stats = dict(zip(entity.job.value.get('stats'), soul))
        stats['HP'] = stats['HP'] * 4

        return stats
    else:
        soul = soul.copy()
        soul += race.value.get('bonus')
        soul = soul.reshape(6).tolist()
        soul.sort(reverse=True)

        stats = dict(zip(job.value.get('stats'), soul))
        stats['HP'] = stats['HP'] * 4

        return stats

def get_ordered_soul(entity, job=None, soul=None):
    if entity is not None:
        soul = entity.soul.soul.copy()
        soul = soul.reshape(6).tolist()
        soul.sort(reverse=True)
        
        stats = dict(zip(entity.job.value.get('stats'), soul))
        stats['HP'] = stats['HP'] * 4

        return stats
    else:
        soul = soul.copy()
        soul = soul.reshape(6).tolist()
        soul.sort(reverse=True)

        stats = dict(zip(job.value.get('stats'), soul))
        stats['HP'] = stats['HP'] * 4

        return stats