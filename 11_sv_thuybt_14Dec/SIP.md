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
Một requests qua một ST -----------------> nơi để request, và vị trí của hop tiếp theo (trong CT).  
                              proxy core
Responses từ CT gửi tới ST. 
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
         - *Proxy-Require*: Nếu request chứa một Proxy-Require với một hoặc nhiều option-tags 
         - *Proxy-Authentication*: 
      Nếu có thành phần nào lỗi thì nó sẽ hoạt động như UAS và gửi error respons 
2. Tiền xử lý các thông tin cần định tuyến
3. Xác định targets của request
4. Chuyển tiếp request tới mỗi target
5. Xử lý tât cả responses




                  
                      




