import os
import socket    
import multiprocessing
import subprocess

def pinger(job_q, results_q): # Ping a ip
    DEVNULL = open(os.devnull, 'w')
    while True:
        ip = job_q.get()
        if ip is None:
            break
        try:
            subprocess.check_call(['ping', '-c1', ip],
                                  stdout=DEVNULL)
            results_q.put(ip)
        except:
            pass

def get_my_ip(): # Return your ip
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

def map_network(pool_size=255): # Returns a python list of all valid ips on the network
    ip_list = list()

    ip_parts = get_my_ip().split('.') # get the first part of the network ip (ex 192.168.1.xxx)
    base_ip = ip_parts[0] + '.' + ip_parts[1] + '.' + ip_parts[2] + '.'

    jobs = multiprocessing.Queue() # prepare the jobs queue
    results = multiprocessing.Queue()

    pool = [multiprocessing.Process(target=pinger, args=(jobs, results)) for i in range(pool_size)]

    for p in pool:
        p.start()

    for i in range(1, 255): # cue the ping processes
        jobs.put(base_ip + '{0}'.format(i))

    for p in pool:
        jobs.put(None)

    for p in pool:
        p.join()

    while not results.empty(): # collect the results
        ip = results.get()
        ip_list.append(ip)

    return ip_list

print('Mapping...')
lst = map_network()
print(lst)