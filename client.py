import http.client
import time

conn = http.client.HTTPConnection("www.localhost:5000")

transaction_id = 1
while True:
    conn.request("GET", "/calculate_pi/" + str(transaction_id))
    transaction_id += 1
    print('send request to server farms')
    conn.close()
    time.sleep(.3)