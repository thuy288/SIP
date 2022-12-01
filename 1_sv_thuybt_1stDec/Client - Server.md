# Client - Server architecture  
*thêm hình ảnh*
Mô hình mạng máy tính bao gồm 2 thành phần chính là client và server giúp cho các máy tính giao tiếp và truyền tải dữ liệu cho nhau. 
- Máy tính đóng vai trò máy khách - **client**
- Máy tính đóng vai trò máy chủ - **server** 
Nguyên tắc hoạt động: server chấp nhận các requests hợp lệ từ mọi nơi qua Internet và trả kết quả về máy tính đã gửi request đó. Để có thể giao tiếp được thì giữa chúng phải có một chuẩn nhất định được gọi là giao thức. Một số giao thức được sử dụng phổ biến hiện nay như: HTTPS, TCP/IP, FTP,...
Ưu điểm: 
- có thể làm việc trên bất kì một máy tính nào có hỗ trợ giao thức truyền thông
- nhiều server làm cùng một dịch vụ, có thể nằm trên cùng nhiều hay một máy tính
- khả năng truy cập từ xa -> hỗ trợ nhiều dịch vụ đa dạng
- khả năng mở rộng (tăng kích thước của server) 
Nhược điểm: bảo mật thông tin chưa an toàn lắm, tuy nhiên khi sử dụng giao thức HTTPS thì đã được hỗ trợ bảo mật khi truyền tải. 
### So sánh client-server và Peer to Peer 
| Client - Server | Peer - to - Peer |
|---|---|
| Client và Server được phân biệt với nhau | Client và Server không được phân biệt với nhau |
| tập trung và chia sẻ dữ liệu | tập trung vào kết nối |
| Server dùng để lưu trữ dữ liệu | mỗi Peer có dữ liệu riêng của nó |
| Server phản hồi lại dịch vụ được request bởi client | Mỗi node đều có thể request và response các dịch vụ |
| Chi phí đắt hơn | Chi phí rẻ hơn | 
| Ổn định hơn | không ổn định bằng |
| Dùng cho cả các mạng nhỏ lẫn lớn | thường dùng cho các mạng nhỏ, số lượng máy tính nhỏ hơn 10 | 
