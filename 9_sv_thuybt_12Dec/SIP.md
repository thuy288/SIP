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
Với UAC: \
      - CAll-ID (dialog ID) ~ Call-ID (message) \
      - remote tag ~ tag (To)  \
      - local tag ~ tag (From) \
Với UAS: \
      - CAll-ID(dialog ID) ~ CAll-ID (message) \
      - remote tag ~ tag (From) \
      - local tag ~ tag (To) \
 ## Creation of a Dialog \
 Dialogs được tạo thông qua non-failure responses tới requests với specific cụ thể. Và 2xx, 109-199 responses với To tag nơi và request đã INVITE
 ## UAS behavior
 UAS phản hồi tới một request với response mà thiết lập một dialog (ví dụ 2xx), UAS cần phải copy tất cả Record-Route header từ request tới response. UAS thêm Contact header vào response. \
 ## UAC Behavior
 UAC gửi một request có thể thiết lập một dialog, nó cần phải cung cấp một SIP hoặc SIPS URI với global scope. Khi một UAC nhận một response nó thiết lập một dialog và state của dialog đó. \
 ## Generating the Request
 URI trong trường To của request ~ remote URI (dialog state) \
 tag (To - request) ~ remote tag (dialog ID) \
 From URI (request) ~ local URI (dialog state) \ 
 tag (From-request) ~ local tag (dialog ID) \
 nếu remote hoặc local là null, thì tag được bỏ qua trong To hoặc From \
 
 UAC sử dụng remote target và route để build Request-URI và Route của request \
 Nếu route là empty, UAC thay remote targer URI vào Request-URI. \
 Nếu route không empty: \
      - URI đầu tiên có *lr*, UAC thay remote target
      URI vào Request-URI và phải gồm *Route* header.
      - URI đầu tiên không có *lr*, UAC thay URI đầu tiên từ route set thành
      Request-URI. \
 Khi request được tạo, địa chỉ của server được tính toàn là gửi đi thro quá trình của request. \
 ## Processing the Responses
 UAC nhận response từ request từ transaction layer. ----------------> 408 (Request Timeout) \                                            timeout
                  | \
                  | \
                  | \
 UAC nhận 2xx response để refresh request, nó thay thế                
 dialog's remote target URI  = URI từ *Contact* trong response đó             ---------------------> 481 Call/Transaction Does not exist / 408 Request Timeout ->                                                                                                            Terminate the dialog \
 UAS nhận request từ transaction layer, nếu request có *tag* trong To header, UAS core so sánh mã định danh của request với cái hiện đang có. \
      - Nếu match thì nó là một mid-dialog request -> UAS áp dựng cùng quá trình
      như cho request ở ngoài dialog
      - Nếu không match: UAS bị lỗi và cần khởi động lại, hoặc nó có thể được nhận
      một request cho UAS khác. 
      -> Dựa vào To tag có thể xác định là accept hay reject request. 
* Nếu UAS muốn reject request, nó cần phải phản hồi 481 Call/Transaction does not exist và chuyển nó tới server transaction. 

## Kết thúc một Dialog 
nếu một request ở ngoài dialog tạo non-2xx final response, bấy kỳ một dialog sớm được tạo ra provisional response (1xx) tới request đó thì sẽ được kết thúc.

# 13 Initiating a Session
UAC muốn khởi tạo một phiên (audio, video, game). \
INVITE requests yêu cầu server thiết lập một phiên, request đó được gửi chuyển tiếp tới proxy, rồi tới UASs. \
UASs sẽ cần truy vấn người dùng để accept invitation bằng cách gửi 2xx response. Nếu invitation không được accept thì 3xx, 4xx, 5xx, hoặc 6xx response sẽ được gửi phụ thuộc vào nguyên nhân từ chối. \
Trước khi gửi response cuối cùng, UAS có thể gửi 1xx response để nói với UAC về quá trình liên lạc với người được gọi. \
Sau tất cả final response thì UAC sẽ gửi một ACK for mỗi final response mà nó nhận được. Với 2xx thì ACK tạo bởi UAC core, còn 300-699 thì quá trình tạo ACK sẽ thực hiện bởi transaction layer.  \
-> Vì vậy có thể nói 2xx cho INVITE thiết lập một phiên. 
## Creating the initial INVITE
initial INVITE là request ngoài một dialog. Những header sau nên có trong bản tin INVITE \
      - Allow: nó cho biết method vào có thể được gọi trong dialog. \
      - Supported:  nó liệt kê tất cả các extensions được hiểu bởi UAC. \
      - Accept: nó xác định Content-Types nào được chấp nhận bởi UA
UAC có thể thêm trường Expires để hạn chế trường hợp invalid trong invitation. \
Loại hình media nào được thể hiện trong *codec*: 




 
 
                  
 
 
 
 
 
      
      
      
      
      
      
      
      
      
      



