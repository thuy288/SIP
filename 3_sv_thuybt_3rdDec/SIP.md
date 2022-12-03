# 1. Gửi Request
Đích phải được xác định bởi DNS.
  **DNS**: thủ tục cho phép một client giải quyết được việc tìm một SIP URI cho địa chỉ IP, port và giao thức transport của hop tiếp theo để liên lạc. SIp cũng sử dụng DNS cho phép server gửi response tới backup client nếu client chính bị lỗi. 
  Đầu tiên với proxy 1 để tìm được SIP server trong domain B, để chuyển tiếp cuộc gọi tới B. Thứ hai với proxy 2 sẽ xác định backup cho proxy 1 trong trường hợp nó lỗi sau khi chuyển tiếp request. 
  * Trường hợp 1: proxy 1 cần xác định địa chỉ IP, port, và giao thức vận chuyển cho server phía domain B. Client cần lựa chọn bất kỳ protocol nào đó (TCP, UDP, SCTP, TLS). Nếu trong URI không chọn transport protocol và target là một địa chỉ IP thì client sẽ chọn UDP cho SIP URI và TCP cho SIPS URI, nếu target không là một IP address thì client sẽ chọn truy vấn NAPTR cho doamin trong URI. 
  Xác định địa chỉ IP và port: nếu URI đã có port thì không cần tìm cái mới, còn nếu chưa có thì nó sẽ sử dụng port default của giao thức transport. 
  SIP URI có thể xác định dưới form: sip:<proxy>, proxy là FQDN (Full Qualified Domain Name - tên miền và tên máy chủ() hoặc địa chỉ IP của proxy hop tiếp theo. 
  ![image](https://user-images.githubusercontent.com/101868484/205438041-7bb16dce-7b37-46a1-8185-4f1de85d63dc.png)
# 2. Processeing Responses
-------------------|
Transport layer    |
Transaction layer  |
Transaction user

Responses được xử lý đầu tiên ở transport layer sau đó tới transaction layer. Transaction layer xử lý xong sẽ gửi đến transaction user. 
**Lỗi có thể xảy ra**: Trong một số trường hợp, transaction layer có thể nhận được phản hồi lỗi thay vì SIP message. Ví dụ, khi nhận được lỗi timeout là 408 (Request Timeout) 
# 3. Processing 3xx responses - Redirection
Được gửi bởi SIP server xảy ra như một redirect server trong response của một INVITE. Một UAS có thể gửi một phản hồi redirection class để thực hiện một số tính năng chuyển tiếp cuộc gọi. Một UAC có thể được cấu hình để tự động tạo INVITE khi chuyển hướng cuộc gọi. 
  
