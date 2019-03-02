import numpy as np

def get_stats(entity):
    # Return a dict holding the {'stat': value}
    if entity.soul:
        soul = entity.soul.soul.reshape(6).tolist()
        soul.sort(reverse=True)
    else:
        return {}
    
    return dict(zip(entity.job.value, soul))