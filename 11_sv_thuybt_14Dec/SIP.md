INVITE
# UAS Processing
```
         transaction layer
                |
                |
      receive INVITE request
      
```
## Redirected
3xx response is sent: 300 Multiple Choices, 301 Moved Permanently, 302 Moved Temporarily
Trong response đó nên có Contact header chứa một hoặc nhiều URIs của địa chỉ mới 
## Rejected
Ví dụ khi người nhận không thể trả lời cuộc gọi đó, response 406 Busy Here sẽ được return \
Hoặc nếu UAS biết rằng không có system nào chấp nhận cuộc gọi đó, response 600 Busy Everywhere sẽ được return. (hiếm thấy) \
UAS từ chối nên return 488 Not Acceptable Here, và Warning header để giải thích tạo sao lựa chọn đó lại bị từ chối. 
## Accepted
UAS tạo 2xx response ----> tạo dialog \
2xx response nên có Allow, Supported, Accept header ---> UAC xác định được những features và extensions được hỗ trợ bởi UAS trong suốt quá trình gọi/ \
Do sau khi nhận được final response và chuyển nó tới lớp transport thì INVITE server transaction sẽ bị xóa bỏ ---> cần phải gửi response định kỳ tới transport cho đến khi ACK tới. 
# 14 Modifying an Existing Session
**offfer-answer**: chỉ áp dụng vào bodies của Content-Disposition header ---> INVITE và ACK gồm một body message. 
Offer/Answer model được sử dụng để tạo session hoặc modify session đang tồn tại. 
- offer: thành phần để tạo một session hoặc  đang ở trong session mà muốn tạo mô tả của phiên đó. 
- answer: tạo một trả lời tới offer cung cấp cho nó, trong đó có:
          + media stream có được accept hay không
          + codecs mà được sử dụng
          + địa chỉ IP và ports mà người trả lời muoonons dử dụng để nhận media. 

# 15. Terminating a Session
Nếu INVITE ban đầu không tạo ra non-2xx final response thì terminates tất cả sesions và dialogs mà được tạo qua responses tới request. 
BYE request được sử dụng để kết thúc phiên, khi BYE được nhận ở trong một dialog ---> bất kỳ session nào liên quan tới dialog đó đều sẽ bị terminate. 
Với trường hợp hang up nó sẽ được người gọi coi như là CANCEL request khi chưa nhận được final response, BYE với dialogs sau final response. Người được gọi thì coi như là BYE vì khi nhận điện thoại thì 2xx đã được tạo nên hanging up sẽ là BYE sau khi nhận được ACK. 
## UAC Behavior
UAC tạo một non-INVITE client transaction và chuyển nó tới BYE request ---> BYE request được gửi tới client transaction. 
Lúc này nếu có response 481 (Call/Transaction does not exit) hoặc 408 (Request Timeout) hoặc không có response được nhận thì UAC sẽ kết thúc dialog và consider phiên. 
## UAS Behavior
```
UAS core nhận một BYE request và check em nó có match với 
dialog đang tồn tại hay không              -------------------> 481 response -> pass nó tới server transaction 
                                                   not match 
                  |
                  |
                  | match
                  |
                  v
        UAS core nhận BYE request cho một dialog đang tồn tại
        và tiến hành request. 
                  |
                  |
                  |
                  v
        UAS kết thúc phiên
```        
        
# 16. Proxy Behavior
proxy là thành phần route SIP requests, responses. 
có 2 mode: stateless và stateful đã được trình bày ở phần trước. 
## Stateful Proxy
mô hình của Stateful Proxy
```
            +--------------------+
            |                    | +---+
            |                    | | C |
            |                    | | T |
            |                    | +---+
      +---+ |       Proxy        | +---+   CT = Client Transaction
      | S | |  "Higher" Layer    | | C |
      | T | |                    | | T |   ST = Server Transaction
      +---+ |                    | +---+
            |                    | +---+
            |                    | | C |
            |                    | | T |
            |                    | +---+
            +--------------------+
```
stateful proxy có một server transaction có liên quan tới một hoặc nhiều client transaction.
```
Một requests qua một ST -----------------> nơi để request, và vị trí của hop tiếp theo (trong CT).  
                              proxy core
Responses từ CT gửi tới ST. 
```
Mỗi request thì có một ST mới, retransmissions của request sẽ xử lý bởi ST đó. 
Proxy core làm việc giống như UAS gửi các response 1xx như là 100 trying. 
Với một request mới, prxy sẽ làm việc như sau:
1. Request hợp lệ
         - *Syntax hợp lệ*: 
         - *đúng định dạng URI*: nếu fail thì sẽ phản hồi 406 Unsupported URI Scheme
         - *Max-Forwards*: Nếu Max-Forwards có giá trị 0 thì request sẽ không được chuyển đi. 
         - *Loop Detection*: Nếu mọt request có nhiều trường Via với giá trị sent-by = giá trị trong request
           đã được chuyển đi trước đó, Request lúc này bị loop hoặc rơi vào trường hợp xoắn ốc (???). 
           Để tranh trường hợp này thì *branch* sẽ được so sánh ---> match thì loop, khác thì xoắn ốc, tiếp
           tục quá trình. \
           Khi vòng lặp được phát hiện thì sẽ có phản hồi 482 Loop Detected
         - *Proxy-Require*: Nếu request chứa một Proxy-Require với một hoặc nhiều option-tags  mà không hiểu 
            được thì sẽ return 420 Bad Extension (+ Unsupported header)
         - *Proxy-Authentication*: Nếu không có credentials trong reuest, proxy có thể challenge người khởi
            tạo để yêu cầu cung cấp thông tin đó bằng response 407 (Proxy_Authenticate header) 
      Nếu có thành phần nào lỗi thì nó sẽ hoạt động như UAS và gửi error respons 
2. Tiền xử lý các thông tin cần định tuyến
```
         Proxy kiểm tra Request-URI của request. ------------------------------------>   Proxy phải thay thế 
                        |                         chứa một giá trị mà được thay thế bởi    request-URI trong 
                        |                        proxy trước đó vào Rrcord-Route          request với giá trị
       maddr parameter  |                                                                 sau cùng từ Route                           |                                                                 header
                        v
         proxy check xem nếu giá trị đó trong addresses
         hoặc domain của proxy đã được cấu hình không
                        |
                        |
                        | yes + request đã được nhận sử dụng port và transport 
                        | được chỉ định
                        |
                        v
         proxy bỏ qua maddr và các port và transport non-default
         
```                                                               
3. Xác định targets của request
         Được xác định bởi contents của request hoặc obtained từ abstract location service. Mỗi target thì được set như URI. 
         Nếu trong Request-URI có *maddr* thì nó phải thay thế vào trong target như là một target duy nhất và chuyển tới bước sau. 
         nếu domain của Request-URI không phải là doamin là element này chịu trách nhiệm, Request-URI phải đặt vào target là target duy nhất là element phải xử lý Request Forwarding.
         485 Ambigous sẽ được phản hồi khi Request-URI không cung cấp đủ thông tin cho proxy để xác định được target. 
         404 Not Found response sẽ được phản hồi khi Request-URI xác định 1 tài nguyên ở proxy mà không tồn tại. 
         480 Temporarily Unavailable response: khi target set empty (không xác định được target) 
4. Chuyển tiếp request tới mỗi target
         giá trị *q* trong trường Contact: targets được xử lý từ giá trị q lớn nhất tới nhỏ nhất, cùng giá trị q thì thực hiện song song. 
         Stateful proxy sẽ duy trì target với response context tạo bởi proxy layer trước khi chuyển tiếp request đầu tiên. 
         Với mỗi target, quá trình forward như sau: 
                  1. Tạo một bản sao của request nhận được: 
                  2. Update Request-URI
                  3. Update Max-Forward: set về 70
                  4. Add Record-route
                  5. Add additional
                  6. Tiền xử lý các thông tin cần định tuyến (như bước 2 phần trên) 
                  7. xác định địa chỉ, port, transport của hop tiếp theo
                  8. Add Via
                  9. Add Content-length
                  10. Forward request mới
                  11. Set timer 
5. Xử lý tât cả responses
       -   Tìm context phản hồi thích hợp
       -   Update timer C cho các response 1xx:
       -   Xóa Via trên cùng
       -   Add response vào response context
       -   Check xem response đó có nên chuyển tiếp luôn không
       -   Lựa chọn the best final response từ response context
       -   Tổng hợp lại các trường Authorization 
       -   Rewrite Record-route
       -   chuyển tiếp response
       -   tạo CANCEL request
 # Examples
 ## Basic SIP Trapezoid
 ```
                                                   INVITE sip:callee@domain.com SIP/2.0
                                                   Contact: sip:caller@u1.example.com
                                                   Record-Route: <sip:p1.example.com;lr>
                                           +------+                     +------+
                                          /|  P1  |-------------------->|  P2  |^\
                                         / +------+                     +------+ \\
                                        /                                         \\
INVITE sip:callee@domain.com SIP/2.0   /       SIP/2.0 200 OK                      \\            INVITE sip:callee@u2.domain.com SIP/2.0        
Contact: sip:caller@u1.example.com    /        Contact: sip:callee@u2.domain.com    \\           INVITE sip:callee@u2.domain.com SIP/2.0
                                     /         Record-Route: <sip:p2.domain.com;lr>  \\          Record-Route: <sip:p2.domain.com;lr>                  
                                    /          Record-Route: <sip:p1.example.com;lr>  \\         Record-Route: <sip:p1.example.com;lr>
                                   /                                                   \\
                                  /                                                     \\
                                                                                          v
                           +------+                                                     +------+
                           |  U1  |                                                     |  U2  | 
                           +------+                                                     +------+
        
 
 
 ```




                  
                      




