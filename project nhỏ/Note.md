Port từ 0 tới 1023: cho các ứng dụng TCP/IP và thường được gọi là well-known ports. Nó cho phép các ứng dụng client dễ dàng xác định vị trí các quy trình ứng dụng máy chỉ tương ứng trên các máy chủ khác.  
Port từ 2014 tới 49151: User or Registered port là một network port  
Port từ 49515 tới 655: Dynamic ports - private ports   

# Asumptions
- two Linux systems
- Python3 should be installed
- able to ping each other 
- One system should act as Server and other system should act as clientat one particular time.
# Requirements
- use two different Linux systems which are connected through network
- Two systems should be connected through Ehternet or Wi-fi or any other connections.
# How to run programs and expected output
**Step 1:** Open terminal in servel system
**Step 2:** Go to the path where server.py is present
**Step 3:** Run server.py  
```
python3 server.py
```
We should see below prints:
Server is listening on port : 9898
Copied file name will be recv.txt at server side
**Step 4:** Open terminal at client system
**Step 5:** Go to the path where client.py and sample.txt present
**Step 6:** Run client.py 
```
python3 client.py <server system IP>
```
**Step 7:** Go to server and look for output
```
File has been copied successfully
Server closed the connection
```
**Step 8:** There should be one file name recv.txt at server folder. The content recv.txt ~ sample.txt
-> successfully copied 







