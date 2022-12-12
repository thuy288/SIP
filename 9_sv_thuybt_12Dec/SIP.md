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
Dialog là thể hiện của mối quan hệ peer-to-peer SIP giữa hai UA. Mỗi dialog thì được xác định bởi mỗi UA với dialog ID, gồm có CAll-ID, local tag và remote tag 



