
import socket
from threading import *

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "52.49.91.111"
port = 2019
print (host)
print (port)
serversocket.bind((host, port))

class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while 1:
            print('Client sent:', self.sock.recv(1024).decode())
            self.sock.send(b'''
SELECT STATES.user_id,
MIN(STATES.date_time) session_from ,
MAX(STATES.date_time) session_to ,
  -TIMESTAMPDIFF(second,MAX(STATES.date_time),MIN(STATES.date_time)) seconds ,
sum(DUPS.duplication) num_actions
FROM (
select SUM(
CASE WHEN 
(b.date_time<a.date_time and (b.action='open' or b.action='close')) 
or (b.date_time=a.date_time and b.action='open')
THEN 1
ELSE 0
END
) State,
a.user_id,a.action,a.date_time 
from  activity a join activity b on a.user_id=b.user_id 
group by a.user_id,a.action,a.date_time
 ) STATES join (select user_id,date_time,action,count(*) duplication
from activity group by user_id,date_time,action) DUPS on STATES.user_id = DUPS.user_id 
where  STATES.date_time = DUPS.date_time and STATES.action = DUPS.action 
GROUP BY user_id,state
order by user_id,session_from
                    ''')

serversocket.listen(5)
print ('server started and listening')
while 1:
    clientsocket, address = serversocket.accept()
    client(clientsocket, address)
