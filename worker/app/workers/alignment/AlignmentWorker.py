from app.configuration import loadConfig
from redis import ConnectionPool

def alignmentWorkerThread(redis_connection_pool: ConnectionPool):
    ...





def alignmentWorkerSubprocess(fileid_1, fileid_2, path1=None, path2=None):
    options = loadConfig()
    