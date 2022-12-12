#Processing of OPTIONS request
Sau khi 200 OK trả về, nếu UAS đang bận và có response 486 Busy Here. \
Nó cho phép OPTIONS request có thể được sử dụng để xác định xem UAS có chấp nhận INVITE request không. 
Nếu OPTIONS được tạo bởi proxy server, thì proxy sẽ trả về 200 OK cho biết về khả năng của server, và response đó sẽ không có message body. \

## Trong bản tin response:
Các trường nên có: Allow, Accept, Accept-Encoding, Accept-Language, Supported. \
Example: 
      ```
      SIP/2.0 200 OK
      Via: SIP/2.0/UDP pc33.atlanta.com;branch=z9hG4bKhjhs8ass877;received=192.0.2.4
      To: <sip:carol@chicago.com>;tag=93810874
      From: Alice <sip:alice@atlanta.com>;tag=1928301774
      Call-ID: a84b4c76e66710
      CSeq: 63104 OPTIONS
      Contact: <sip:carol@chicago.com>
      Contact: <mailto:carol@chicago.com>
      Allow: INVITE, ACK, CANCEL, OPTIONS, BYE
      Accept: application/sdp
      Accept-Encoding: gzip
      Accept-Language: en
      Supported: foo
      Content-Type: application/sdp
      Content-Length: 274
      ```
# 12. Dialogs
Dialog là thể hiện của mối quan hệ peer-to-peer SIP giữa hai UA. Mỗi dialog thì được xác định bởi mỗi UA với dialog ID, gồm có CAll-ID, local tag và remote tag. \
Một dialog được xác định bởi mỗi UA với một dialog ID, nó gồm Call-ID, local tag và remote tag. 
Với UAC:
      - CAll-ID (dialog ID) ~ Call-ID (message) 
      - remote tag ~ tag (To)
      - local tag ~ tag (From)
Với UAS:
      - CAll-ID(dialog ID) ~ CAll-ID (message)
      - remote tag ~ tag (From)
      - local tag ~ tag (To) 
 ## Creation of a Dialog
 Dialogs được tạo thông qua non-failure responses tới requests với specific cụ thể. Và 2xx, 109-199 responses với To tag nơi và request đã INVITE
 ## UAS behavior
 UAS phản hồi tới một request với response mà thiết lập một dialog (ví dụ 2xx), UAS cần phải copy tất cả Record-Route header từ request tới response. UAS thêm Contact header vào response. 
 ## UAC Behavior
 UAC gửi một request có thể thiết lập một dialog, nó cần phải cung cấp một SIP hoặc SIPS URI với global scope. Khi một UAC nhận một response nó thiết lập một dialog và state của dialog đó. 
 ## Generating the Request
 URI trong trường To của request ~ remote URI (dialog state)
 tag (To - request) ~ remote tag (dialog ID)
 From URI (request) ~ local URI (dialog state) 
 tag (From-request) ~ local tag (dialog ID)
 nếu remote hoặc local là null, thì tag được bỏ qua trong To hoặc From
 
 UAC sử dụng remote target và route để build Request-URI và Route của request
 Nếu route là empty, UAC thay remote targer URI vào Request-URI.
 Nếu route không empty:
      - URI đầu tiên có *lr*, UAC thay remote target
      URI vào Request-URI và phải gồm *Route* header.
      - URI đầu tiên không có *lr*, UAC thay URI đầu tiên từ route set thành
      Request-URI.
 Khi request được tạo, địa chỉ của server được tính toàn là gửi đi thro quá trình của request. 
 ## Processing the Responses
 UAC nhận response từ request từ transaction layer. 
 
 
      
      
      
      
      
      
      
      
      
      



