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
- SIP message is either a request from a client to a server, or a response from a server to a client.
- Requests: phân biệt dựa trên Request-line
            Cấu trúc của Request-line: <method name> <request-URI>  <protocol version>
            Example: sip:bob@biloxi.com SIP/2.0
            - Method: REGISTER, INVITE, ACK, CANCEL, BYE
            - Request-URI: is a SIP or SIPS URI 
- Responses: phân biệt dựa trên requests bởi Status-line = SIP_version SP Status_code Reasion_Phrase CRLF
    Status-Code: là một số nguyên gồm 3 chữ số, với chữ số đầu tiên là class của response
    1xx: provisional - request received : 100 trying, 180 Ringing, ...
    2xx: Success: 200 OK, 202 Accepted
    3xx: Redirection: 300 Multiple choices, 301 Moved Permanently
    4xx: Client error: 407 Proxy Authentication Required, 408 Request Timeout
    5xx: Server error: 500 server internal Error, 501 Not Implemented ,..
    6xx: Global error: 506 Busy Everywhere, 603 Decline

# 5. UAC Behavior
    **Tạo request**: các trường sau cần phải có: To, From, CSeq, Call-ID, Max-Forwards, Via
   * **To**: may contain SIP or SIPS URI là nơi là nó muốn request tới. 
   * **From**: contains a URI and optionally a display name. "tag" được sử dụng trong trường To và From của SIP messages. Nó dùng để xác định dialog. Khi UA gửi request ra ngoài dialog, nó sẽ có tag duy nhất trong trường From. Khi tag được insert vào request hoặc response thì nó là duy nhất là được tạo ra từ việc random ít nhất 32 ký tự. UA sẽ thay thế different tag vào From của một bản tin INVITE hơn và thay thế vào trường To cả response trong same INVITE. 
   * **Call-ID**: unique identitier để tạo thành 1 nhóm series của message. Nó sẽ giống cho cả requests và responses gửi bởi UA trong 1 dialog. 
   Example: 
**INVITE sip:0398765432100;phone-context=0498765432100@0498765432100;user=phone SIP/2.0**  
Record-Route: <sip:mo@10.4.128.21:6101;lr=on;ftag=7b3fae13;rm=8;did=078.654>  
Via: SIP/2.0/UDP 10.4.128.21:6101;branch=z9hG4bK7a83.64fb9469779e2867fdb139eecff6c335.0  
Via: SIP/2.0/UDP 192.168.101.3:6400;received=192.168.101.3;branch=z9hG4bK-524287-1---b67029e8d52ecffc;rport=6401;transport=UDP  
Max-Forwards: 69  
Route: <sip:orig@scscf.ims.mnc001.mcc001.3gppnetwork.org:6060;lr>  
Contact: <sip:0498765432100@192.168.101.3:6400;alias=192.168.101.3~6401~1>;+sip.instance="<urn:gsma:imei:35622410-483317-0>";+g.3gpp.icsi-ref="urn%3Aurn-7%3A3gpp-service.ims.icsi.mmtel";+g.3gpp.mid-call;+g.3gpp.srvcc-alerting;+g.3gpp.ps2cs-srvcc-orig-pre-alerting;video  
To: <sip:0398765432100;phone-context=0498765432100@0498765432100;user=phone>  
From: <tel:0498765432100>;tag=7b3fae13  
**Call-ID: TF0lR-e_t0o7Jp-w5kq58A..@192.168.101.3**  
CSeq: 1 INVITE  
...
  
**SIP/2.0 100 Trying**  
Via: SIP/2.0/UDP 10.4.128.21:6101;branch=z9hG4bK7a83.64fb9469779e2867fdb139eecff6c335.0  
Via: SIP/2.0/UDP 192.168.101.3:6400;received=192.168.101.3;branch=z9hG4bK-524287-1---b67029e8d52ecffc;rport=6401;transport=UDP  
To: <sip:0398765432100;phone-context=0498765432100@0498765432100;user=phone>  
From: <tel:0498765432100>;tag=7b3fae13  
**Call-ID: TF0lR-e_t0o7Jp-w5kq58A..@192.168.101.3**  
CSeq: 1 INVITE  
Server: Kamailio S-CSCF  
Content-Length: 0  
    
    Trong cả bản tin INVITE và 100 Trying thì đều có Call-ID giống nhau. 
   * **CSeq** 
    là một cách để xác định và sắp xếp transactions. Nó bao gồm một sequence number và một method (method này là method của request đó). Sequence number bắt buộc phải là một số nguyên 32-bit là phải nhỏ hơn 2**31. 
    Example: CSeq: 1 INVITE
   * **Max-Forward**
    để giới hạn số lượng của 1 hops request có thể transit tới đích. Nó bao gồm một số nguyên mà sẽ giảm 1 sau mỗi hop. Nếu nó giảm đến 0 trước khi xong các bản tin với đích thì nó sẽ kết thúc với error response 483 (Too many hops). Cụ thể, một UAC phải insert a trường Max-Forwards vào mỗi request và bắt đầu từ giá trị 70. 
    Example: Max-Forwards: 69
   * **Via**
    dùng để xác định phương tiện vận chuyển được sử dụng cho giao dịch và xác định vị trí gửi response. Trường Via chỉ được thêm vào sau khi phương tiện truyền tải sẽ được sử dụng để đến chặng tiếp theo đã được chọn. Khi UAC tạo request, nó cần phải insert một trường Via vào request đó. Cấu trúc gồm tên protocol và version, branch parameter (xác định giao dịch tạo bởi request đó, sử dụng bởi cả client và server).
    Example: Via: SIP/2.0/UDP 192.168.101.3:6400;received=192.168.101.3;branch=z9hG4bK-524287-1---b67029e8d52ecffc;rport=6401;transport=UDP
    Trong ví dụ trên, message đó bắt nguồn từ 1 địa chỉ là  192.168.101.3
    
    
