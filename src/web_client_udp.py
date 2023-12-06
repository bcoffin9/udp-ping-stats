# Ping server 10 times
# Report result in console and output file
import socket
from socket import AF_INET, SOCK_DGRAM
import time # helpful in multiple areas
import csv # helps in writing file
import os # helps in writing file


def calculate_ping_stats(response_times):
    """ Calculates the average response time and success rate of a ping program. """
    total = 0
    items = 0
    for response_time, did_succeed in response_times:
        if did_succeed:
            total += response_time
            items += 1
    if items == 0:
        return 0, 0
    return (round(total / items, 2), round((items / len(response_times)) * 100, 2))

# write results to file
def output_pings_to_file(response_times):
    """ Writes the results to a file located in the directory. """
    filepath = f'{os.getcwd()}/results/' \
        + time.strftime("%Y%m%dT%H%M", time.localtime()) \
        + f'_{socket.gethostbyname(socket.gethostname()).replace('.', '-')}.csv'
    with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
        log_writer = csv.writer(csvfile)
        log_writer.writerow(('response_time', 'did_succeed'))
        log_writer.writerows(response_times)

# Setup for socket        
HOST = socket.gethostbyname(socket.gethostname())
PORT = 12000
addr = (HOST, PORT)

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
# Assign IP address and port number to socket
clientSocket = socket.socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1.0)  # will raise error after one second

# holds results from pings
results = []

for x in range(1, 11):
    # Send some data
    data = f'ping {x}'.encode('utf-8')
    clientSocket.sendto(data, addr)
    start = time.time()
    try:
        # wait for one second max
        data, addr = clientSocket.recvfrom(1024)
        end = time.time()
        data = data.decode('utf-8')
        rtt = round((end - start) * 1000, 2)
        results.append((rtt, True))
        print(f'Packet {x}: {rtt} ms')
    except socket.timeout:
        results.append((-1.0, False))
        print(f'Packet {x}: failed')

avg_time, success_rate = calculate_ping_stats(results)
print(f'Avg response time: {avg_time} ms')
print(f'Success rate: {success_rate}%')
output_pings_to_file(results)
