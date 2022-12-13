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
  **string-value-oriented transformation {s.xxxxx}:** $(var(x){s.init}) - chuyển thành integer, $(fU{s.substr,0,2}) - lấy 2 ký tự đầu tiên của From username
  **URI-value-oriented transformation {uri.xxxxx}:** $(avp(uri){uri.host}) - domain/host của URI , $(fu{uri.param,transport}) - giá trị của transport trong From URI
  **VIA-value-oriented transformation {via.xxxxx}:** $(hdr(via){via.branch}) - *branch* của Via header đầu tiên
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
- Timeouts: nếu timeout thì OpenSIPS sẽ tạo phản hồi 408 Timeout. Để control thì ta có các biến: $T_fr_timeout và $T_fr_inv_timeout. 
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
// thêm ảnh map của MySQL 
## AUTH_DB module: xử lý xác thực từ database
## DB_MYSQL: drive cho database
## USRLOC: duy trì user location table và exposrts commands
## REGISTRAR: registration process
## PERMISSIONS: xác thực IP 
  
  
  
  
  
  
  
  
  
  
  
  
  


