# 1.	Overview
SIP hoạt động với các giao thức bằng các điểm đầu cuối trong Internet (được gọi là user agent) để khám phá và đồng ý chia sẻ các đặc điểm của 1 phiên. IP tạo một cơ sở các máy chủ mạng (được gọi là proxy servers) nơi mà user agents có thể gửi bản tin đăng ký, mời tham gia phiên và các yêu cầu khác. SIP là một công cụ để tạo, sửa và chấm dứt các phiên hoạt động độc lập với giao thức vận chuyển và không phụ thuộc vào các phiên đang được thiết lập.
5 yếu tố khi thiết lập và chấm dứt các hoạt động truyền thông trên nhiều phương tiện: 
-	User location: xác định được các hệ thống đầu cuối được sử dụng
-	User availability: xác định xem bên được gọi tới có sẵn sàng hay không
-	User capabilities: xác định phương tiện và các parameters sẽ được sử dụng 
-	Session setup: “ringing”, thiết lập các parameters của phiên ở cả phía gọi và được gọi
-	Sesion management: gồm vận chuyển và chấm dứt phiên, sửa parameters của phiên, các dịch vụ gọi.
SIP hoạt động ở cả Ipv4 và Ipv6
# 2.	Cấu trúc chung
Ví dụ: trao đổi SIP message giữa 2 người dùng là Alice và Bob. Alice sử dụng SIP identity của Bob và Uniform Resource Identifier (URI - SIP URI)

## SIP URI
bao gồm thông tin ban đầu và duy trì phiên với các resource, ví dụ: 
- dịch vụ online
- trường hợp multi-line phone
- một mailbox 
- một số PSTN trong một cổng dịch vụ
- một nhóm (sales, helpdesk) trong một tổ chức
Example: Bob's SIPS URI: sip:bob@biloxi.com, Alice's SIPS URI: sip:alice@atlanta.com

## SIP dựa trên model HTTP - request/response
Nghĩa là trong mỗi một bản tin thì đều có các thông tin cụ thể về method, function ở server và ít nhất là có một response trả về. 

## Cấu trúc của một bản in INVITE
Example: Bản tin INVITE từ Alice request tới Bob
    1  INVITE sip:bob@biloxi.com SIP/2.0
    2  Via: SIP/2.0/UDP pc33.atlanta.com;branch=z9hG4bK776asdhds
    3  Max-Forwards: 70
    4  To: Bob <sip:bob@biloxi.com>
    5  From: Alice <sip:alice@atlanta.com>;tag=1928301774
    6  Call-ID: a84b4c76e66710@pc33.atlanta.com
    7  CSeq: 314159 INVITE
    8  Contact: <sip:alice@pc33.atlanta.com>
    9  Content-Type: application/sdp
   10  Content-Length: 142
Ở dòng đầu tiên: *INVITE sip:bob@biloxi.com SIP/2.0*. Tên method + SIPS URI + SIP/<version>
Các dòng sau sẽ gồm các trường: Via, To, From, Call-ID, CSeq, ... (sẽ được nói cụ thể ở phần sau)
# 4. Cấu trúc của một SIP Protocol 
    SIP là cấu trúc lớp, nghĩa là các giao thức sẽ được thiết lập theo các mục đích của từng lớp.
     Lớp thấp nhất là **syntax và encoding**: 
     Lớp thứ hai là **transport layer**: nó xác định cách là client gửi requests và nhận responses và server        nhận requests và gửi responses qua mạng. Khi một kết nối được mở bởi transport layer, thì index sẽ được        set thành destination IP, port và transport, còn khi được chấp nhận bởi transport layer thì index sẽ được      set thành source IP, port number và transport. 
     Lớp thứ ba là **transaction layer**: được gửi bởi một client (sử dụng transport layer) cho server. 
     Lớp cuối cùng là: **transaction user** :
    
    


