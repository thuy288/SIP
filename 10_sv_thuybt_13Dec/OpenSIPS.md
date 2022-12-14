- **menuconfig**: cung cấp bởi OpenSIPS để tự động tạo file cấu hình và trả lời trên m4 để dựng file cấu hình OpenSIPS 
# Scripting capabilities
capabilities trong dạng: functions, statements, variables, operators, assignments
## Scripting functions  
  Có 2 loại functions: 
  - cung cấp bởi OpenSIPS core: simple function, flexible protype,.. do core functions không giới hạn interface giữa OpenSIPS core và modules
  - cung cấp bởi modules: more rigorous protype, nó sử dụng 6 thông số và chỉ xử lý được các chuỗi
  Tất cả các functions thì đều trả về một giá trị integer: Failire: một giá trị âm, Success: một giá trị dương
## Scripting variables
  sử dụng để truy cập thông tin hoặc giữ thông tin tùy chỉnh. 
  OpenSIPS sử dụng nhiều biến và được nhận biết dựa trên:
  - Phạm vi hoặc khả năng của biến
  - Trạng thái read-write của biến
  - Cách xử lý multiple values  
  Example:
  ```
  $(<context>type(name)[index]{transformation})
  ```
  type: ru, var hoặc avp
  name: tên của biến đó
  index: tương tự như trong C/C++
  transformation: hành động có thể applied vào giá trị của biến
  context: reply (sử dụng trong failure route để yêu cầu một biến), request (sử dụng trong reply route để đánh giá biến trong request packet) 
  Ví dụ: 
  ```
  $ru: RIP request URI
  $hdr(from): From header
  $ci: SIP Call-ID
  $Ts: current time
  ```
  AVP (Attribute value pairs) là biến động có thể dùng để tạo demand. AVps là read-write và có thể bị xóa. \
  Các giá trị được lueu trữ trong ACP theo dạng stack (LIFO). \
  Ví dụ:
  ```
  $avp(my_ip): giá trị được thêm vào cuối cùng của AVP my_ip
  $(avp(my_ip) [-1]): giá trị dược thêm vào đầu tiên của AVP my_ip
  $(avp(ips)[*]): tất cả các giá trị của AVP my_ip
  ```
  **Script variables**: biến read-write, có thể là integer hoặc string. 
  Ví dụ:
  ```
  $var(uri) = "sip:"+$rU+"@sip.com";
  $var(i) = $var(i) + 1;
  ```
  **transformations**: xử lý và lấy kết quả từ function mà sử dụng biến đó. 
  Ví dụ: 
  ```
  # the length of From URI ($fu is variable for From URI)
  $(fu{s.len})
  # get the 2 chars from position 5
  $(var(x){s.substr,5,2})
  # get the username part of a SIP URI like value
  $(avp(my_uri){uri.user})
  ```
  *Có thể dùng nhiều transformation trong cùng 1 thời điểm*
  **string-value-oriented transformation {s.xxxxx}:** $(var(x){s.init})$ - chuyển thành integer, $(fU{s.substr,0,2})$ - lấy 2 ký tự đầu tiên của From username
  **URI-value-oriented transformation {uri.xxxxx}:** $(avp(uri){uri.host})$ - domain/host của URI , $(fu{uri.param,transport})$ - giá trị của transport trong From URI
  **VIA-value-oriented transformation {via.xxxxx}:** $(hdr(via){via.branch})$ - *branch* của Via header đầu tiên
  **parameter-list-value-oriented transformation {param.xxxxx}:** "a=1;b=2;c=3"{param.value,c} = "3"
  **name-address value-oriented transformation {nameaddr.xxxxx}:** For example, '"test <sip:test@opensips.org>;tag=dat43h' \
{nameaddr.param,tag} = dat43h
  **IP-value-oriented transformation {ip.xxxxx}:** "192.168.2.134" {ip.pton}{ip.family} = "INET"
  **CSV-value-oriented transformation {csv.xxxxx}:** "a,b,c" {csv.count} = 3
  **SDP-value-oriented transformation {sdp.xxxxx}:** SDP-value-oriented transformation {sdp.xxxxx}:
  **RE-value-oriented transformation {re.xxxxx}:** "abc"{re.subst,/a/A/g} = "Abc"
  #### Flags
  - Message flags: 
  - Branch flags: 
  - Script flags: 
  #### Operators
  
  | Operator | Function |
  | ---------|----------|
  | = | equal |
  | + | Plus |
  | - | minus |
  | * | Multiple |
  | % | Modulo |
  | | | Bitwise OR |
  | & | Bitwise AND |
  | ^ | Bitwise XOR |
  | ~ | Bitwise NOT |
  | << | Biwise left shift |
  | >> | Bitwise right shift |
  | == | Equal |
  | != | not equal |
  | =~ | regular expression matching |
  | !~ | regular expression not-matching |
  | > | Greater| 
  | >= | Greater or equal | 
  | < | less |
  | <= | less or equal |
  | && | AND |
  | || | OR |
  | ! | NOT
  | [...] | test operator |
  
  Kết thúc: 
  exit(), drop(), return(), break()
## SIP routing in OpenSIPS
Stateless and stateful routing: stateless yêu cầu ít tài nguyên hơn nên nhanh hơn, tuy nhiên statless lại bị hạn chế về một số khả năng. 
Một số certain chỉ có ở stateful mode:
- Retransmission detection: phát hiện và loại bỏ retransmission tới, nên cần transaction để nhận biết cái nào đã được nhận rồi
- Performing retransmissions: 
- Timeouts: nếu timeout thì OpenSIPS sẽ tạo phản hồi 408 Timeout. Để control thì ta có các biến: $T_fr_timeout$ và $T_fr_inv_timeout$. 
- Parllel and serial forking: lưu lại các thông tin về branches và trạng thái của mỗi branch. 
- Script routes: lưu trữ thông tin trong transaction và kích hoạt bởi transaction liên quan. Branch route, failure route, onreply route, local route phụ thuộc vào context nên chỉ được sử dụng ở stateful mode
*Sự khác nhau về functions*
| Operation | Stateless | Stateful |
|-----------|-----------|----------|
| SIP forward | forward() | t_relay() |
| SIP replying | sl_send_reply() | t_reply() |
| Create transaction | n/a | t_newtran() |
| Match transaction | n/a | t_check_trans() | 

# SUBSCRIBER MANAGEMENT
![image](https://user-images.githubusercontent.com/101868484/207365252-f682f147-1dc4-47f0-afb8-92e771523eb1.png)
DB_MYSQL: drive cho database
USRLOC: duy trì user location table và exposrts commands
REGISTRAR: registration process
PERMISSIONS: xác thực IP 
ALIAS_DB: alias translation
GROUP: quá trình xác thực
## AUTH_DB module: quá trình xác thực từ database
Các parameters của module  này là: 
![image](https://user-images.githubusercontent.com/101868484/207370362-e5a7d267-fbe2-4a47-8947-008e287da3a5.png)
| Parameter | Default | Description |
|-----------|---------|-------------|
| db_url | mysql://opensipsro:opensipsro@localhost/opensips | URI của database | 
| user_column | username | tên của cột giữ tên của người dùng |
| domain_column | domain | tên của cột giữ domains của người dùng |
| password column | ha1 | tên của cột giữ passwords | 
| password_column2 | ha1b | tên của cột chứa chuỗi HA1 đã được tính toán trước (gồm có cả domain của username) |
| calculate_ha1 | 0 | nó sẽ nói với server rằng là nó có plain text passwords trong database hay không | 
| use_domain | 0 | set tới một nếu có multidomain | 
| load_credentials | rpid | chỉ định thông tin đăng nhập được nạp từ database khi xác thực; thông tin đó được lưu trữ trong Attribute Value Pair (AVP). | 

2 chức năng của AUTH_DB: 
- table: database table để tìm subscribers (subscriber)
- realm: domain name, nếu realm trống thì nó xác thực bất kỳ domain nào
- *www_authorize (realm, table)*: dùng cho registration authentication khi server là endpoint của request
- *proxy_authorize (realm, table)*: khi final destination của request không phải là server của mình, nó có thể chuyển tiếp request tới hop tiếp theo
### Register authentication sequence
![image](https://user-images.githubusercontent.com/101868484/207386789-4f1ab12c-112c-4c2b-8bd2-e029a43863c4.png)
Sau khi challenged thì UAC gửi bản tin REGISTER với trường Authorization
```
REGISTER sip:192.168.1.155 SIP/2.0.
Via: SIP/2.0/UDP 192.168.1.119:29040;branch=z9hG4bK-d87543-
13517a5a8218ff45-1--d87543-;rport.
Max-Forwards: 70.
Contact: <sip:1000@192.168.1.119:29040;rinstance=2286bddd834b3cfe>.
To: "1000"<sip:1000@192.168.1.155>.
From: "1000"<sip:1000@192.168.1.155>;tag=0d10cc75.
Call-ID: e0739d571d287264NjhiZjM2N2UyMjhmNDViYTgzY2I4ODMxYTVlZTY0NDc..
CSeq: 1 REGISTER.
Expires: 3600.
Allow: INVITE, ACK, CANCEL, OPTIONS, BYE, REFER, NOTIFY, MESSAGE,
SUBSCRIBE, INFO.
User-Agent: X-Lite release 1003l stamp 30942.
Content-Length: 0.
U 192.168.1.155:5060 -> 192.168.1.119:29040
```
```
SIP/2.0 401 Unauthorized.
Via: SIP/2.0/UDP 192.168.1.119:29040;branch=z9hG4bK-d87543-
13517a5a8218ff45-1--d87543-;rport=29040.
To: "1000"<sip:1000@192.168.1.155>;tag=329cfeaa6ded039da25ff8cbb8668bd2.4
1bb.
From: "1000"<sip:1000@192.168.1.155>;tag=0d10cc75.
Call-ID: e0739d571d287264NjhiZjM2N2UyMjhmNDViYTgzY2I4ODMxYTVlZTY0NDc..
CSeq: 1 REGISTER.
WWW-Authenticate: Digest realm="192.168.1.155", nonce="46263864b3abb96a42
3a7ccf052fa68d4ad5192f".
Server: Opensips (2.1-notls (i386/linux)).
Content-Length: 0.
```
```
REGISTER sip:192.168.1.155 SIP/2.0.
Via: SIP/2.0/UDP 192.168.1.119:29040;branch=z9hG4bK-d87543-
da776d09bd6fcb65-1--d87543-;rport.
Max-Forwards: 70.
Contact: <sip:1000@192.168.1.119:29040;rinstance=2286bddd834b3cfe>.
To: "1000"<sip:1000@192.168.1.155>.
From: "1000"<sip:1000@192.168.1.155>;tag=0d10cc75.
Call-ID: e0739d571d287264NjhiZjM2N2UyMjhmNDViYTgzY2I4ODMxYTVlZTY0NDc..
CSeq: 2 REGISTER.
Expires: 3600.
Allow: INVITE, ACK, CANCEL, OPTIONS, BYE, REFER, NOTIFY, MESSAGE,
SUBSCRIBE, INFO.Subscriber Management
User-Agent: X-Lite release 1003l stamp 30942.
Authorization: Digest username="1000",realm="192.168.1.155",nonce="462638
64b3abb96a423a7ccf052fa68d4ad5192f",uri="sip:192.168.1.155",response="d7b
33793a123a69ec12c8fc87abd4c03",algorithm=MD5.
Content-Length: 0.
```
```
SIP/2.0 200 OK.
Via: SIP/2.0/UDP 192.168.1.119:29040;branch=z9hG4bK-d87543-
da776d09bd6fcb65-1--d87543-;rport=29040.
To: "1000"<sip:1000@192.168.1.155>;tag=329cfeaa6ded039da25ff8cbb8668bd2.
c577.
From: "1000"<sip:1000@192.168.1.155>;tag=0d10cc75.
Call-ID: e0739d571d287264NjhiZjM2N2UyMjhmNDViYTgzY2I4ODMxYTVlZTY0NDc..
CSeq: 2 REGISTER.
Contact: <sip:1000@192.168.1.119:29040;rinstance=2286bddd834b3cfe>;expir
es=3600.
Server: Opensips (2.1-notls (i386/linux)).
Content-Length: 0.
```
code trong opensips.cfg: 
```
if (is_method("REGISTER"))
{
  # authenticate the REGISTER requests
  if (!www_authorize("", "subscriber")) #Register không xác thực bởi www_authorize() 
  {
    www_challenge("", "0"); #gửi challenge 401, có chứa authentication challenge
    exit;
  }
  if (!db_check_to()) #kiểm tra URI của user trong trường To.
  {
    sl_send_reply("403","Forbidden auth ID");
    exit;
  }
  if (proto==TCP) setflag(TCP_PERSISTENT);
  if (!save("location")) #lưu AOR vào trong MySQL 
  sl_reply_error();
  exit;
}
```
 ### INVITE authentication sequence
 ![image](https://user-images.githubusercontent.com/101868484/207391760-ba51db4b-7b20-49ff-a9dd-515767d9f488.png)
 407 Proxy Authentication Required: gồm thông tin về Digest Authentication như là *realm* và *nonce* 
 Sequence: 
```
INVITE sip:1000@192.168.1.155 SIP/2.0.
Via: SIP/2.0/UDP 192.168.1.169;branch=z9hG4bKf45d977e65cf40e0.
From: <sip:1001@192.168.1.155>;tag=a83bebd75be1d88e.
To: <sip:1000@192.168.1.155>.
Contact: <sip:1001@192.168.1.169>.
Supported: replaces.
Call-ID: 8acb7ed7fc07c369@192.168.1.169.
CSeq: 39392 INVITE.
User-Agent: TMS320V5000 TI50002.0.8.3.
Max-Forwards: 70.
Allow: INVITE,ACK,CANCEL,BYE,NOTIFY,REFER,OPTIONS,INFO,SUBSCRIBE.
Content-Type: application/sdp.
Content-Length: 386.
(sdp body striped off).
```
```
SIP/2.0 407 Proxy Authentication Required.
Via: SIP/2.0/UDP 192.168.1.169;branch=z9hG4bKf45d977e65cf40e0.
From: <sip:1001@192.168.1.155>;tag=a83bebd75be1d88e.
To: <sip:1000@192.168.1.155>;tag=329cfeaa6ded039da25ff8cbb8668bd2.b550.
Call-ID: 8acb7ed7fc07c369@192.168.1.169.
CSeq: 39392 INVITE.
Proxy-Authenticate: Digest realm="192.168.1.155", nonce="4626420b4b162ef8
4a1a1d3966704d380194bb78".
Server: Opensips (2.1-notls(i386/linux)).
Content-Length: 0.
```
```
ACK sip:1000@192.168.1.155 SIP/2.0.
Via: SIP/2.0/UDP 192.168.1.169;branch=z9hG4bKf45d977e65cf40e0.
From: <sip:1001@192.168.1.155>;tag=a83bebd75be1d88e.
To: <sip:1000@192.168.1.155>;tag=329cfeaa6ded039da25ff8cbb8668bd2.b550.
Contact: <sip:1001@192.168.1.169>.
Call-ID: 8acb7ed7fc07c369@192.168.1.169.
CSeq: 39392 ACK.
User-Agent: TMS320V5000 TI50002.0.8.3.
Max-Forwards: 70.
Allow: INVITE,ACK,CANCEL,BYE,NOTIFY,REFER,OPTIONS,INFO,SUBSCRIBE.
Content-Length: 0.
```
```
INVITE sip:1000@192.168.1.155 SIP/2.0.
Via: SIP/2.0/UDP 192.168.1.169;branch=z9hG4bKcdb4add5db72d493.
From: <sip:1001@192.168.1.155>;tag=a83bebd75be1d88e.
To: <sip:1000@192.168.1.155>.
Contact: <sip:1001@192.168.1.169>.
Supported: replaces.
Proxy-Authorization: Digest username="1001", realm="192.168.1.155",
algorithm=MD5, uri="sip:1000@192.168.1.155", nonce="4626420b4b162ef84a1a1
d3966704d380194bb78", response="06736c6d7631858bb1cbb0c86fb939d9".
Call-ID: 8acb7ed7fc07c369@192.168.1.169.
CSeq: 39393 INVITE.
User-Agent: TMS320V5000 TI50002.0.8.3.
Max-Forwards: 70.
Allow: INVITE,ACK,CANCEL,BYE,NOTIFY,REFER,OPTIONS,INFO,SUBSCRIBE.
Content-Type: application/sdp.
Content-Length: 386.
(sdp header striped off)
```
Trong code: 
```
if (!proxy_authorize("","subscriber")) { #nếu proxy_authorize không xác thực
  proxy_challenge("","0"); #gửi response 407 Authentication Required
  exit;
};

consume_credentials(); #xóa bỏ trường xác thực trước đó bởi server. 
# native SIP destinations are handled using our USRLOC DB
if (!lookup("location")) { 
  sl_send_reply("404", "Not Found");
  exit;
};
route(relay);
```
### Digest authentication
![image](https://user-images.githubusercontent.com/101868484/207402437-62309ad9-361e-4763-a227-95151c07239e.png)
hệ thống cơ bản \
Nó challenges UA sử dụng **nonce**. Một response hợp lệ gồm checksum của tất cả các parameters -> password không truyền đi dưới dạng simple text. \
Sau khi xác thực, xóa trường Authorize từ request
## Analysis of the opensips.cfg file
```
loadmodule "db_mysql.so" #make the authentication work 
loadmodule "auth.so"
loadmodule "auth_db.so"
```
```
modparam("auth_db", "calculate_ha1", 1) #MySQL support , calculate_ha1: tell the auth_db module to use plaintext passwords 
modparam("usrloc", "db_mode", 2) #db_mode: tell the usrloc module to store and retrieve the AOR records
```

## The REGISTER requests
```
if (is_method("REGISTER"))
  {
    # authenticate the REGISTER requests
    if (!www_authorize("", "subscriber"))
   {
      www_challenge("", "0"); #2 parameter: realm, "0": not include QOP 
      exit;
   }
  if (!db_check_to())
  {
    sl_send_reply("403","Forbidden auth ID");
    exit;
  }
  if ( proto==TCP) setflag(TCP_PERSISTENT);
  
  # systems lưu location data cho UAC đó
  if (!save("location"))  
    sl_reply_error();
  
  exit;
}
```
## The non-REGISTER requests
```
if (!(is_method("REGISTER")))
{
  if (from_uri==myself) #handling a domain served by our proxy
  {
    # authenticate if from local subscribers
    #(domain in FROM URI is local)
    if (!proxy_authorize("", "subscriber")) { #check the authentication headers
      proxy_challenge("", "0");
      exit;
    }
    if (!db_check_from()) { #map SIP users with authentication user
      sl_send_reply("403","Forbidden auth ID");
      exit;
    }

    consume_credentials(); #remove thr Authorize header from request before relaying
      # caller authenticated
   } else {
    # if caller is not local
    if (!uri==myself) {
      send_reply("403","Relay forbidden");
      exit;
    }
  }
}
```



  
  
  
  
  
  
  
  
  
  
  
  
  


