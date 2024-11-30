import os
import random

WORKER_AUTOID_LENGTH = 16

def loadConfig() -> dict:
    
    REDIS_HOST = os.environ["VODM_WORKER_REDIS_HOST"]
    REDIS_PORT = os.environ["VODM_WORKER_REDIS_PORT"]
    
    if 'WORKER_IDENTITY' in os.environ:
        WORKER_IDENTITY = os.environ["WORKER_IDENTITY"]
    else:
        WORKER_IDENTITY = f"WORKER-{''.join((str(random.randint(0, 9)) for _ in range(WORKER_AUTOID_LENGTH)))}"
    
    if 'VODM_WORKER_RENDER_PROCS' in os.environ:
        RENDER_PROCESS_COUNT = int(os.environ["VODM_WORKER_RENDER_PROCS"])
        if RENDER_PROCESS_COUNT < 0:
            raise ValueError(f"Invalid render process count: '{RENDER_PROCESS_COUNT}'")
        elif RENDER_PROCESS_COUNT > 1:
            print(f"More than one render process enabled, I hope you know what you're doing!\n")
    else:
        print("No render process count specified, defaulting to 1")
        RENDER_PROCESS_COUNT = 1

    if 'VODM_WORKER_AUDIO_ALIGN_PROCS' in os.environ:
        AUDIO_ALIGN_PROCESS_COUNT = int(os.environ["VODM_WORKER_AUDIO_ALIGN_PROCS"])
        CPU_COUNT = os.cpu_count()
        if AUDIO_ALIGN_PROCESS_COUNT < 0:
            raise ValueError(f"Invalid render process count: '{AUDIO_ALIGN_PROCESS_COUNT}'")
        elif CPU_COUNT is not None and AUDIO_ALIGN_PROCESS_COUNT > CPU_COUNT:
            print(f"More audio alignment processes than CPUs, I hope you know what you're doing!!!!\n")
    else:
        AUDIO_ALIGN_PROCESS_COUNT = 1

    # LIVE_CAPTURE_PROCESS_COUNT = int(os.environ["VODM_WORKER_LIVE_CAPTURE_PROCS"])
    # if LIVE_CAPTURE_PROCESS_COUNT < 0:
    #     raise ValueError(f"Invalid render process count: '{LIVE_CAPTURE_PROCESS_COUNT}'")

    LOCAL_CACHE_DIR = None
    if "VODM_WORKER_LOCAL_CACHE_DIR" in os.environ:
        LOCAL_CACHE_DIR = os.environ["VODM_WORKER_LOCAL_CACHE_DIR"]

    if LOCAL_CACHE_DIR == "":
        LOCAL_CACHE_DIR = None
    
    
        
    return {
        'REDIS_HOST': REDIS_HOST,
        'REDIS_PORT': REDIS_PORT,
        'WORKER_IDENTITY': WORKER_IDENTITY,
        'RENDER_PROCESS_COUNT': RENDER_PROCESS_COUNT,
        'AUDIO_ALIGN_PROCESS_COUNT': AUDIO_ALIGN_PROCESS_COUNT,
        # 'LIVE_CAPTURE_PROCESS_COUNT': LIVE_CAPTURE_PROCESS_COUNT,
        'LOCAL_CACHE_DIR': LOCAL_CACHE_DIR,
    }