# Open Systems Interconnection model 
là một mô hình căn bản về các tiến trình truyền thông gồm có 7 layer
```
--------------------------------------------------------------------------------------
|  Application         |        | Tầng ứng dụng: xác định giao diện người sử dụng và môi trường OSI. 
                       |        |  Là nơi người dùng tương tác với chương trình ứng dụng, và qua đó với mạng. 
                       |        | Một số ví dụ về tầng này bao gồm HTTP, Telnet, FTP, SMTP, IMAP
-----------------------|        -------------------------------------------------------
|  Presentation        |        | Tầng trình diễn: như tầng dữ liệu. Nhiệm vụ dịch dữ liệu được gửi từ tầng application
                       |        |
                       | Data       |sang định dạng chung. Ngược lại, ở máy tính nhận thì sẽ chuyển từ định dạng chung sang 
                       |        | định dạng của tầng application. Cụ thể:
                       |        | - Dịch từ ASCII -> EBCDIC
                       |        | - integer -> dấu phẩy động
                       |        | - nén dữ liệu
                       |        | - encoding và decoding để đảm bảo sự bảo mật
------------------------        -------------------------------------------------------
|  Session             |        | Tầng phiên: 
---------------------------------------------------------------------------------------
|  Transport           |segment,| Tầng vận chuyển: chuyển dữ liệu giữa các người dùng end-to-end, tầng này là nơi
                        Datagram  chuyển các ứng dụng thành TCP hay UDP
---------------------------------------------------------------------------------------
|  Network             | packet | Tầng mạng: truyền các chuỗi dữ liệu từ một nguồn tới một đích, thông qua một hoặc
                                  nhiều mạng. Thực hiện chứng năng định tuyến, các thiết bị định tuyến (router), 
                                  chuyển mạch (switch) hoạt động tại tầng này
-----------------------         -------------------------------------------------------
|  Data-link           | Frame  | Tầng liên kết dữ liệu: quy trình truyền dữ liệu giữa các thực thể mạng, phát hiện
                                  và sửa lỗi trong tầng Physical nếu có. Nó xác định giao thức để thiết lập hoặc kết thúc 
                                  kết nối giữa 2 thiết bị vật lý. IEEE 802 chia datalink layer thành 2 layer nhỏ hơn:
                                  - Medium access control (MAC) layer - kiểm soát thiết bị trong mạng có quyền truy cập
                                  vào các phương tiện và quyền truy cập dữ liệu
                                  - Logical link control (LLC) layer - xác định và đóng gói các giao thức lớp mạng,
                                  đồng thời kiểm tra lỗi và đồng bộ hóa.                                   
-----------------------         -------------------------------------------------------
|  Physical            | Bit,   | Tầng vật lý: về điện và vật lý cho các thiết bị: chân cắm, hiệu điện thế, cáp nối
                                  các thiết bị tầng vật lý: HUb, repeater, converter, network adapter, Host bus adapter
                                  Chức năng:
                                  - electrical connection: thiết lập hoặc ngắt mạch kết nối điện
                                  - modulation: analog to digital or digital to analog 
-----------------------  Symbol -------------------------------------------------------
```

# Ví dụ cụ thể
Khi một người dùng yêu cầu truy cập trang web https://wikipedia.org/, trình duyệt sẽ gọi tới máy chủ DNS để biên dịch URL trang web thành một địa chỉ IP, mỗi trang web có địa chỉ IP riêng biệt. Địa chỉ IP của trang web sẽ được trả về cho trình duyệt.
Đầu tiên, trang web sẽ truy vấn tới trình xử lý giao thức HTTP trong tầng thứ 7 - Application layer. Sau khi Application layer nhận ra đây là một truy vấn sử dụng kênh an toàn, nó sẽ chuyển tới thư viện TLS (transport Layer Security) tại tầng 5 và 6 và Session là Presentation layer. Thư viện TLS thiết lập một kết nối tới đích. Nó chuyển tới cho TCP - giao thức nằm ở tầng 4 (Transport). 
Trình xử lý TCP nhận truy vấn kết nối và tạo ra gói tin với cờ "SYN" và chuyển đến tầng 3 (Network). 
Tầng network nhận gói tin và thêm header có thông tin IP vào gói tin (giúp cho router biết cách định tuyến gói tin đến đúng địa chỉ đích)
Sau đó, chuyển tiếp dến tầng 2 (Data-link). Data-link layer sẽ thêm địa chỉ MAC của bộ định tuyến, cho phép bộ định tuyến gửi gói tin ra ngoài internet
Sau đó gói tin được chuyển tới tầng 1 (Physical layer): gói tin từ dạng nhị phân mã hóa vật lý để truyền tải trên cáp mạng - hay đặt nó lên Wifi - và bắt đầu chuyển đi qua mạng cục bộ và internet. 
*Khi đến được máy chủ đích, toàn bộ quá trình sẽ được thực hiện ngược lại với quá trình bên trên*

# Router, Switch
## Router
Bộ định tuyến là thiết bị mạng máy tính dùng để chuyển các gói dữ liệu qua cùng một liên mạng và đến các đầu cuối, thông qua một tiến trình gọi là định tuyến. Hoạt động ở tầng thứ 3 trong mô hình OSI (Network layer).
Router có vai trò kết nối 2 mạng trở lên với nhau (Thông thường là 2 mạng LANs hay WANs hoặc kết nối 1 mạng LANs với mạng ISP của nó). Router có chức năng gửi các gói dữ liệu mạng giữa 2 hoặc nhiều mạng, từ một tới nhiều điểm đích đến cuối cùng từ router. Chính vì vậy, vị trí của nó trong một mạng Internet là ở nơi có 2 mạng kết nối với nhau trở lên.
Về cấu tạo, router thường bao gồm 1 hoặc nhiều cổng LAN và có thể bao gồm ăng-ten phát tín hiệu wifi. Router sử dụng phần headers trong các gói tin để có thể xác định đường đi nhanh nhất cho các packet (đơn vị đo dữ liệu ở tầng mạng - Network Layer) từ host này đến với các host khác. 
## Switch
Switch (thiết bị chuyển mạch) là một thiết bị dùng để kết nối các đoạn mạng với nhau theo mô hình mạng hình sao (star). Theo mô hình này, switch đóng vai trò là thiết bị trung tâm, tất cả các máy tính đều được nối về đây. Trong mô hình OSI, switch hoạt động ở tầng liên kết dữ liệu (Data-link layer), ngoài ra có một số loại switch cao cấp hoạt động ở tầng mạng. 
Hiện nay đây là kiểu thiết kế mạng được sử dụng phổ biến. Phạm vi ứng dụng của mạng LAN thường được sử dụng để kết nối các máy tính trong gia đình, trong một phòng Game, phòng NET, trong một toà nhà của Cơ quan, Trường học.- Cự ly của mạng LAN giới hạn trong phạm vi có bán kính khoảng 100m, các máy tính có cự ly xa hơn thông thường người ta sử dụng mạng Internet để trao đổi thông tin. Mạng có các ưu điểm như tốc độ cao, do sử dựng mô hình mạng star nên khi một máy hỏng không gây ảnh hưởng đến kết nối mạng của các máy còn lại. 
Switch nhận biết máy nào kết nối với cổng của nó bằng cách học địa chỉ MAC nguồn trong frame mà nó nhận được. Khi hai máy thực hiện liên lạc với nhau. Switch chỉ thiết lập một mạch ảo giữa hai cổng tương ứng mà không làm ảnh hưởng đến lưu thông trên các cổng khác. Do đó, mạng LAN có hiệu suất hoạt động cao thường sử dụng chuyển mạch toàn bộ.

# Giao thức ARP
Address Resolution Protocol: là giao thức chịu trách nhiệm chuyển địa chỉ IP thành địa chỉ MAC hay dùng một địa chỉ IP (48 - bit) để tìm ra địa chỉ MAC (32 - bit). Mỗi thiết bị có một vùng nhỏ để lưu trữ địa chỉ IP và MAC được gọi là ARP cache. 
# Quá trình 2 máy tính kết nối với nhau trong cùng một mạng LAN
### host-to-host: 
2 máy tính được kết nối bằng cap Ethernet và thiết bị chuyển mạch mạng, không có Gateway hoặc bộ định tuyến đứng giữa. Máy tính 1 có thể gửi một gói tin tới máy tính 2 thông qua DNS, nghĩa là máy tính 1 xác định rằng máy tính 2 có địa chỉ IP 192.168.0.55. Nó cũng cần xác định địa chỉ MAC của máy tính 2 bằng cách: Đầu tiên, nó sử dụng một bảng ARP lưu trữ để tìm kiếm địa chỉ 192.168.0.55 cho bất kỳ ghi nhận vào hiện có của địa chỉ MAC của máy tính 2> Lúc này sẽ có 2 trường hợp xảy ra:
- MAC address được tìm thấy, ví dụ 00:eb:24:b2:05:ac chứa gói tin IP
- ARP không có kết quả nào cho 192.168.0.55, máy tính 1 sẽ gửi một ARP broadcast (FF:FF:FF:FF:FF:FF) được chấp nhận bởi tất cả các máy tính trong LAN để yêu cầu địa chỉ 192.168.0.55 trả lời. Máy tính 2 sẽ trả lời với địa chỉ MAC và địa chỉ IP của nó. Máy tính 2 có thể ghi một mục vào bảng ARP của máy tính 1 để có thể sử dụng sau này. Sau đó ARP response lại gồm cả địa chỉ MAC và IP được gửi đi. Máy 1 nhận phản hồi và thêm vào bảng ARP. Nếu MAC tương thích, frame Ethernet có thể gửi từ máy 1 đến máy 2. 
### host to route: 
Máy tính 1 và 2 thuộc 2 mạng cục bộ khác nhau. Máy tính 1 sẽ dùng bảng routing để tìm ra địa chỉ IP của router, rồi từ đó tìm địa chỉ MAC. 
### router to router
Router dùng bảng router để tìm ra địa chỉ IP của router trên cùng LAN, rồi từ đó tìm địa chỉ MAC
### router to host
Trong tường hợp này địa chỉ IP biết được qua địa chỉ IP của điểm đến trên gói tin gửi, router chỉ cần tìm địa chỉ MAC. 
# Quá trình 2 máy tính kết nối với nhau ngoài mạng LAN

