### default tên file: <số thứ tự>.sv_thuybt_day.month
# RFC3261
# Building Telephony systems with OpenSIPS

về chuyển thành file:
1.	Overview
SIP hoạt động với các giao thức bằng các điểm đầu cuối trong Internet (được gọi là user agent) để khám phá và đồng ý chia sẻ các đặc điểm của 1 phiên. IP tạo một cơ sở các máy chủ mạng (được gọi là proxy servers) nơi mà user agents có thể gửi bản tin đăng ký, mời tham gia phiên và các yêu cầu khác. SIP là một công cụ để tạo, sửa và chấm dứt các phiên hoạt động độc lập với giao thức vận chuyển và không phụ thuộc vào các phiên đang được thiết lập.
5 yếu tố khi thiết lập và chấm dứt các hoạt động truyền thông trên nhiều phương tiện: 
-	User location: xác định được các hệ thống đầu cuối được sử dụng
-	User availability: xác định xem bên được gọi tới có sẵn sàng hay không
-	User capabilities: xác định phương tiện và các parameters sẽ được sử dụng 
-	Session setup: “ringing”, thiết lập các parameters của phiên ở cả phía gọi và được gọi
-	Sesion management: gồm vận chuyển và chấm dứt phiên, sửa parameters của phiên, các dịch vụ gọi.
SIP hoạt động ở cả Ipv4 và Ipv6


