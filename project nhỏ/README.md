## TCP client server and UDP client server (code python)
Chạy trên ubuntu và bắt gói wireshark để theo dõi quá trình trao đổi dữ liệu từ lúc khởi tạo kết nối đến lúc truyền nhận dữ liệu (để thể hiện các ý đã trình bày khi so sánh TCP và UDP)
Capture và lưu ra pcap luồng trao đổi 
## Code Server chạy trong máy ảo, client trong máy thật windows
Làm sao để có thể kết nối với nhau được và truyền tải dữ liệu, bắt luồng trao đổi của trường hợp này


Port từ 0 tới 1023: cho các ứng dụng TCP/IP và thường được gọi là well-known ports. Nó cho phép các ứng dụng client dễ dàng xác định vị trí các quy trình ứng dụng máy chỉ tương ứng trên các máy chủ khác.  
Port từ 2014 tới 49151: User or Registered port là một network port  
Port từ 49515 tới 655: Dynamic ports - private ports   

# Asumptions
- two Linux systems![205649681-5a3f6c43-08ec-418c-a589-ed7141ce6929](https://user-images.githubusercontent.com/101868484/205697557-b13f1a72-1c18-4774-be0c-33d72e105a47.png)

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

Server:
![image](https://user-images.githubusercontent.com/101868484/205697625-3553933f-9657-4c9d-b322-8f820d15f473.png)
Client: 
![image](https://user-images.githubusercontent.com/101868484/205697802-7c5ee419-0b5c-4fe9-96c0-050179a731f1.png)


