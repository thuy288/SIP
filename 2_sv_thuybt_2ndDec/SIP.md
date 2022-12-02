*Tiếp ngày hôm trước*
# 3. Cấu trúc của một SIP Protocol 
    SIP là cấu trúc lớp, nghĩa là các giao thức sẽ được thiết lập theo các mục đích của từng lớp.
     Lớp thấp nhất là **syntax và encoding**: 
     Lớp thứ hai là **transport layer**: nó xác định cách là client gửi requests và nhận responses và server nhận requests và gửi responses qua mạng. 
     Khi một kết nối được mở bởi transport layer, thì index sẽ được set thành destination IP, port và transport, còn khi được chấp nhận bởi transport layer thì index sẽ được set thành source IP, port number và transport. 
     Lớp thứ ba là **transaction layer**: được gửi bởi một client (sử dụng transport layer) cho server transaction, trong tất cả các responses gửi từ server tới client.  
     Lớp cuối cùng là: **transaction user** : khi TU muốn gửi một request, nó tạo một client transaction và chuyển request với địa chỉ IP đichs, port, và transport tới chỗ gửi request. 
   ## Các thành phần của SIP
   ### User agent clients and servers
   **User Agent clients (UAC)**
   một ứng dụng phục vụ như một peer-to-peer cổng giao tiếp và tạo ra request, nhận response từ những yêu cầu đó 
   **User Agent server (UAS)**
   UAS is a VoIP application that responds to UAC requests
   *Vai trò của UAC và UAS như là proxy và redirect servers, nó được định nghĩa trên một transaction-by-transaction basis. Ví dụ, UA tạo cuộc gọi là UAC trong khi gửi initial INVITE request và như là UAS trong khi nhận BYE request từ người được gọi*
   ### Stateless and stateful proxies 
   proxy server: chuyển tiếp cá SIP request tới các thành phần mạng khác trong mạng. Ngoài ra còn có tính năng xác thực khi có yêu cầu khai thác dịch vụ
   - Stateless proxy: khi thực hiện thì sẽ không lưu trữ bất kỳ thông tin nào cả, nó chuyển tiếp traffic tới thành phần khác. Vì vậy mà nó có scale lớn, và thực hiện nhanh -> tốt cho network cores
   - Stateful proxy: lưu các bản tin request được gửi tới, cùng với các bản tin response để thực hiện gửi tới các user agent. Có thể tạo nhánh và cung cấp các dịch vụ là stateless không thể (như là call forward busy) 
   ### Registrar
   nhận bản tin SIP register và cập nhật các thông tin mà user agents cung cấp từ bản tin register vào location database. 
# 4. Some Definitions
- SIP message is er a reqeust from a client to a server, or a response from a server to a client.
- 

