# Stateless UAS Behavior
là một UAS không duy trì trạng trái transaction. Nó sẽ chỉ trả lời lại các request mà không lưu bất kỳ một trạng thái nào. Nếu một stateless UAS nhận 1 retransmission của request thì nó sẽ tạo response và gửi lại nó,  giống như lần đầu nó trả lời một request. 
Stateless UAS thì nhận request trực tiếp từ transport layer và gửi trực tiếp tới transport layer mà không qua transaction layer.
Những điểm quan trọng của stateless UAS là: 
- một stateless UAS không gửi 1xx response
- một statelss UAS không retransmit responses
- một stateless UAS phải bỏ qua các ACK requests
- một stateless UAS phải bỏ qua các CANCEL requests
- *To* header tags phải được tạo cho response và có tag giống nhau cho các request giống nhau
# Redirect Servers   
Nó cho phép server đẩy thông tin cho một request lại trong một response tới client
```
            ----------------                          ------------------         ------------------------  
           |Redirect Server|   <--------------------->| Registrar      |         |    Proxy Serrver     |  
            ----------------                          ------------------         ------------------------  
                   |  2. Redirect server checks Location Service to find IP address of UAB   
                   |  3. Redirect Server sends information back to the requestting UA  
 1. INVITE request |  
    is sent to     |  4. UAA sends invite to UAB  
    Redirect server|     ---------------------->  
                   |     <----------------------  
                   |  5. UAB responds to UAA  
                   |    
            ----------------                           -----------------  
            |User Agent A   |   <--------------------> | User Agent B    |  
            ----------------                           -----------------  
                               6. Once invitation is accepted UAA and UAB   
                                  can now establish a session    
```                                  
Một redirect server bao gồm có transaction layer và một transaction user có quyền truy cập vào location service của registrars và location services.    
Khi redirect server trả về một 3xx response tới request (khi server từ chối request và tìm các locations thay thế từ location service) , nó sẽ tạo list locations thay thế vào *Contact* header. *Expires* trong *Contact* header có thể thêm vào *Contact* header để tính toán được lifetime của *Contact* data. *Contact* header gồm có URIs từ các location mới hoặc user names. Một 301 (Moved Permanently) hoặc 302 (Moved Temporarily) response có thể đưa tới cùng location và username từ request ban đầu nhưng thông tin transport thêm vào như server khác hoặc địa chỉ multicast để thay đỏi SIP transport từ UCP hoặc TCP và ngược lại 
# Canceling a Request
CANCEL request được sử dụng để cancel request trước đó được gửi bởi client. Nó sẽ yêu cầu UAS dừng quá trình request và tạo một error response cho request đó. Nó sẽ không ảnh hưởng tới các request mà UAS đã đưa ra phản hồi cuối cùng. -> CANCEL request nào mà nó chiếm nhiều thời gian để phản hồi -> phù hợp với INVITE request (tốn nhiều thời gian để thực hiện) -> có thể kết thúc cuộc gọi bằng CANCEL mà không cần đợi final response 
1. CANCEL bởi UAC 
   Trong trường hợp này, nếu INVITE trả về 2xx final response tới INVITE đó, thì UAS chấp nhận INVITE trong khi CANCEL vẫn đang thực hiện thì UAC sẽ tiếp tục phiên đó bởi 2xx response hoặc sẽ kết thúc bởi BYE. 
3. CANCEL bởi proxy 
   Một stateful proxy có thể tạo CANCEL cho cho INVITE dựa trên *Expires* khi nó hết hạn. Proxy layer tìm kiếm contexts của proxy để server transaction xử lý CANCEL. Nếu context được tìm thấy thì sẽ return 200 OK response cho CANCEL request. 
## Client Behavior
- CANCEL request chỉ nên được gửi để hủy INVITE, vì các request khác thường sẽ phản hồi ngay thức thì, nếu hủy thì có thể tạo ra một race condition. 
- Các header Request-URI, Call-ID, To, CSeq, From trong CANCEL cần phải giống với request sẽ bị hủy, kể cả tags. Và có duy nhất một *Via* header và *Via* header trên cùng trong request -> hủy đúng request. *CSeq* header thì phải là giá trị của CANCEL (đếm số lần CANCEL). 
- Nếu ở request có *Route* header thì CANCEL cũng phải có *Route* header đó, để stateless proxy có thể hủy đúng request
- CANCEL request thì không chứa *Require* hoặc *Proxy-Require* header. 
- Nếu CANCEL không nhận được provisional response (1xx) thì sẽ không được gửi đi, nếu như request (muốn hủy) là nhận được final response thì CANCEL đó sẽ không được gửi đi và không ảnh hưởng tới request đó nữa. Nhưng nếu trong CANCEL có destination address, port, và transport như request thì nó cho phép server nhận CANCEL trước request ban đầu.
- CANCEL và request ban đầu sẽ thực hiện independently, Tuy nhiên một UAC canceling không thể dựa vào việc nhận 487 (Request Terminated) response cho request ban đầu. Nếu như không có final response cho request ban đầu trong 64xT1 (500ms) thì client nên hủy transaction ban đầu và hủy transaction với request ban đầu.

**Race condition in call cancellation**
```
   -----------                          ---------------                         ----------
   |   UAC   |                          | Proxy Server |                        |   UAS   |
   -----------                          ---------------                         ----------
        |  INVITE CSeq: 1 INVITE               |                                     |
        |------------------------------------ >|   INVITE CSeq: 1 INVITE             |
        | 100 CSes: 1 INVITE                   |------------------------------------>|
        |<-------------------------------------|   100 CSeq: 1 INVITE                |
        |  CANCEL Cseq: 1 CANCEL               |<------------------------------------|
        |------------------------------------->|   200 CSeq: 1 INVITE                |
        |  200 CSeq: 1 CANCEl                  |<------------------------------------|
        |<-------------------------------------|   CANCEL Cseq: 1 CANCEL             |
        |  200 CSeq: 1 INVITE                  |------------------------------------>|
        |<-------------------------------------|    200 CSeq: 1 CANCEL               |
        |                                      |<------------------------------------|
        |                               ACK CSeq: 1 ACK                              |
        |--------------------------------------------------------------------------->|
        |                               BYE CSeq: 21 BYE                             |
        |<---------------------------------------------------------------------------|
        |                               200 OK CSeq: 21 BYE                          |
        |--------------------------------------------------------------------------->|
        |                                                                            |
```
## Server Behavior
- Transaction user xác định transaction được hủy bởi CANCEL request, và sau đó giả sử method là CANCEL hoặc ACK và áp dụng nó vào quá trình transaction matching:
### Transaction matching
         Một request nhận vào phải match với transaction đang tồn tại trong server. Branch trong *Via* header trên cùng của request phải bắt đầu với "z9hG4K", và request tạo bởi client transaction cho các thông số liên quan đến nó thì nó sẽ là unique so với tất cả các transactions được gửi bởi client. Nó sẽ matches nếu:
         - *branch* của request = *branch* ở *Via* trên cùng của request tạo transaction (INVITE)
         - *sent-by* của request = *sent-by* ở trên cùng của request tạo transaction (INVITE). Sent-by là cần thiết trong trường hợp có sự trùng lặp branch từ các clients khác nhau. 
         - method của request = method tạo transaction (INVITE) ngoại trừ ACK. 
         Nếu *branch* không có trong *Via* header hoặc không bắt đầu bằng magic cookie ("z9hG4K") thì nó sẽ bỏ qua và thực hiện các bước tiếp theo.
  
  **non-INVITE server transaction**
```

                                  |Request received
                                  |pass to TU
                                  V
                            +-----------+
                            |           |
                            | Trying    |-------------+
                            |           |             |
                            +-----------+             |200-699 from TU
                                  |                   |send response
                                  |1xx from TU        |
                                  |send response      |
                                  |                   |
               Request            V      1xx from TU  |
               send response+-----------+send response|
                   +--------|           |--------+    |
                   |        | Proceeding|        |    |
                   +------->|           |<-------+    |
            +<--------------|           |             |
            |Trnsprt Err    +-----------+             |
            |Inform TU            |                   |
            |                     |                   |
            |                     |200-699 from TU    |
            |                     |send response      |
            |  Request            V                   |
            |  send response+-----------+             |
            |      +--------|           |             |
            |      |        | Completed |<------------+
            |      +------->|           |
            +<--------------|           |
            |Trnsprt Err    +-----------+
            |Inform TU            |
            |                     |Timer J fires
            |                     |-
            |                     |
            |                     V
            |               +-----------+
            |               |           |
            +-------------->| Terminated|
                            |           |
                            +-----------+
```
## CANCEL processing  
Quá trình CANCEL ở server phụ thuộc vào loại server:
- Với stateless proxy thì nó sẽ forward 
    ### stateful proxy
   Có thể phản hồi tới nó và tạo một vài CANCEL requests và UAS sẽ phản hồi tới nó 
   
