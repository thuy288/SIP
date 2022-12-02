# Socket Programming 
- Server là một phần mềm mà nó sẽ đợi request từ client, client là requester của các dịch vụ
- Chương trình client request tới một tài nguyên của server và server phản hồi tới request đó
- Socket là một điểm cuối của 1 kết nối 2 chiều giữa server và client. Socket có thể communicate
  trong cùng một máy, hoặc giữa các máy khác nhau. Với bất kỳ communication với một chương trình 
  remote, chúng ta cần kết nối qua sockt port. 
# Các bước khi kết nối
1. Chương trình python socket server thực thi đầu tiên và chờ đợi bất kỳ một request nào 
2. Chương trình python socker client sẽ bắt đầu conversation đầu tiên
3. Chương trình server sẽ response tới client requests
4. Chương trình client sẽ kết thúc nếu người dùng enter "bye" message. Chương trình server
   sẽ kết thúc khi chương trình client kết thúc
# Python socket server
Để có thể sử dụng python socket connection, chúng ta cần import **socket** module. Sau đó,
một cách tuần tự chúng ta cần thiết lập một vài task để kết nối giữa server và client. 

