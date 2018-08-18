from time import sleep
import time
from joblib import Parallel, delayed
from multiprocessing import Pool
import multiprocessing as multi
import tqdm

def process(n):
    sleep(n)
    # [l for l in range(n[1])]

# n_jobsが使用するcpuの数(-1は使える最大)
start = time.time()
result = Parallel(n_jobs=-1, verbose=10)([delayed(process)(0.1) for n in tqdm.tqdm(range(200))])
elapesed_time = time.time() - start
print('(-1)time:{0}[sec]'.format(elapesed_time))

start = time.time()
p = Pool(multi.cpu_count())
p.map(process, list(range(0,1)))
p.close()
elapesed_time = time.time() - start
print('(-1)time:{0}[sec]'.format(elapesed_time))

# start = time.time()
# result = Parallel(n_jobs=1)([delayed(process)(1) for n in range(20)])
# elapesed_time = time.time() - start
# print('(1)time:{0}[sec]'.format(elapesed_time))

# start = time.time()
# result = Parallel(n_jobs=2)([delayed(process)(1) for n in range(20)])
# elapesed_time = time.time() - start
# print('(2)time:{0}[sec]'.format(elapesed_time))


   