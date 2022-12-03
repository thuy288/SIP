UDP cung cấp trải nghiệm tốt hơn cho người dùng VoIP, nó cho phép trải nghiệm real-time và không bị gián đoạn bởi bất kỳ delay nào. 
SIP clients thường sử dụng TCP hoặc UDP trên port 5060 hoặc 5061 để kết nối SIP server và các SIP endpoints khác. 
- 5060 thường sử dụng cho luồng tín hiệu non-encrypted
- 5061 thường sử dụng cho luồng tín hiệu encrypted với Transport LAyer security (TLS)  
Trong VoIP thì audio được truyền qua mạng network. Một gói chứa âm thanh sẽ từ 10 đến 30 ms.
**TCP: Accuracy matters**
- A gửi packet tới B 
- B nhận packet 1 không lỗi và gửi gói acknowledgement tới A
- A nhận gói acknowledgement và chuẩn bị gửi packet 2 tới B
**UDP: Speed matters**
UDP thích hợp cho các dịch vụ real-time như là VoIP. 
