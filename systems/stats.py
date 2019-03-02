import numpy as np

def get_stats(entity):
    # Return a dict holding the {'stat': value}
    soul = entity.soul.soul.copy()
    soul += entity.race.value.get('bonus')          # Add race bonus
    soul = soul.reshape(6).tolist()    # Convert to list
    soul.sort(reverse=True)            # Sort
    
    return dict(zip(entity.job.value, soul))