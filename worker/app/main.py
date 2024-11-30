from threading import Thread
import redis

from app.configuration import loadConfig
from app.workers.alignment.AlignmentWorker import alignmentWorkerThread
from app.workers.alignment.ExtractionWorker import extractionWorkerThread
from app.workers.download.Downloader import downloadWorkerThread
from app.workers.download.LiveCapture import liveCaptureWorkerThread
from app.workers.rendering import Renderer

options = loadConfig()


# 'REDIS_HOST': REDIS_HOST,
# 'REDIS_PORT': REDIS_PORT,
# 'WORKER_IDENTITY': WORKER_IDENTITY,
# 'RENDER_PROCESS_COUNT': RENDER_PROCESS_COUNT,
# 'AUDIO_ALIGN_PROCESS_COUNT': AUDIO_ALIGN_PROCESS_COUNT,
# 'LIVE_CAPTURE_PROCESS_COUNT': LIVE_CAPTURE_PROCESS_COUNT,
# 'LOCAL_CACHE_DIR': LOCAL_CACHE_DIR,

REDIS_HOST = options['REDIS_HOST']
REDIS_PORT = options['REDIS_PORT']
WORKER_IDENTITY = options['WORKER_IDENTITY']

conn_pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT)

render_threads = []

for i in range(options['RENDER_PROCESS_COUNT']):
    thr = Thread(target=Renderer.renderWorkerThread, name=f"render-thread-{i}", args=(conn_pool, ), )
    render_threads.append(thr)
    thr.start()


audio_align_threads = []

for i in range(options['AUDIO_ALIGN_PROCESS_COUNT']):
    thr = Thread(target=alignmentWorkerThread, name=f"audio-align-thread-{i}", args=(conn_pool, ), )
    audio_align_threads.append(thr)
    thr.start()



audio_extraction_threads = []

for i in range(options['AUDIO_ALIGN_PROCESS_COUNT']):
    thr = Thread(target=extractionWorkerThread, name=f"audio-extraction-thread-{i}", args=(conn_pool, ), )
    audio_extraction_threads.append(thr)
    thr.start()




live_capture_threads = []

for i in range(options['AUDIO_ALIGN_PROCESS_COUNT']):
    thr = Thread(target=liveCaptureWorkerThread, name=f"audio-extraction-thread-{i}", args=(conn_pool, ), )
    live_capture_threads.append(thr)
    thr.start()



download_threads = []

for i in range(options['AUDIO_ALIGN_PROCESS_COUNT']):
    thr = Thread(target=downloadWorkerThread, name=f"audio-extraction-thread-{i}", args=(conn_pool, ), )
    download_threads.append(thr)
    thr.start()

