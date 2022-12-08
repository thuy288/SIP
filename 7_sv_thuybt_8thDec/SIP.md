# 10 Registrations
Trong phần này sẽ là cả quá trình xử lý từ proxy servers và redirect servers để xác định nơi gửi request, 
Registration tạo các mối liên kết trong location server cho các domain để proxy của domain đó nhận được request mà có Request-URI matches với AOR (address ò record). \
Cách để nội dung trong location service được tạo ở đây là administratively.
Nhiệm vụ của registrar là giống như frontend của location service, nó đọc và ghi lại nội dung của REGISTER requests.
Ví dụ REGISTER
```
                                                                bob
                                                              +----+
                                                              | UA |
                                                              |    |
                                                              +----+
                                                                 |
                                                                 |   3)INVITE
                                                                 |   carol@chicago.com
         chicago.com                +--------+                   V
         +---------+    2)Store     |Location|    4)Query     +-----+
         |Registrar|===============>| Service|<===============|Proxy|     sip.chicago.com
         +---------+                |        |===============>+-----+
               A                    +--------+         |
               |                           5)Resp      |
               |                                       |
     1)REGISTER|                                       |
               |                                       |
            +----+                                     |
            | UA |<------------------------------------+
   cube2214a|    |                            6)INVITE
            +----+                    carol@cube2214a.chicago.com
             carol
```
  Figure 10.1. REGISTER example

## 10.2 Conctructing the REGISTER request
REGISTER requests có thể thêm binding mới giữa AOR và contact addresses \
trong bản tin REGISTER thì không tạo dialog \
Các trường cần phải có trong bản tin REGISTER:
- Request-URI: Trong Request-Line
  Example: 
  ```
  REGISTER sip:ims.mnc001.mcc001.3gppnetwork.org SIP/2.0
  ```
  Trong ví dụ trên thì Request-URI là: sip:ims.mnc001.mcc001.3gppnetwork.org \
  Nó là domain của location service
- To: gồm address of record mà registration được tạo, truy vấn và sửa đổi. \
  Example:
  ```
  To: <sip:001011234567895@ims.mnc001.mcc001.3gppnetwork.org>
  ```
  user part: 001011234567895
  host part: ims.mnc001.mcc001.3gppnetwork.org
- From: address of record của người chịu trách nhiệm đăng ký, nội dung giống với To header và có thể có thêm tag
  ```
  From: <sip:001011234567895@ims.mnc001.mcc001.3gppnetwork.org>;tag=4130282085
  ```
- Call-ID: tất cả các registration từ UAC thì có dùng giá trị Call-ID cho việc gửi đăng ký tới registrar cụ thể \
  ```
  Call-ID: 4130282081_47464792@192.168.101.2
  ```
- CSeq: giá trị CSeeq phải tăng lên theo đúng thứ tự của các REGISTER của một UA với cùng CAll-ID
  Example:
```
REGISTER sip:ims.mnc001.mcc001.3gppnetwork.org SIP/2.0
From: <sip:001011234567895@ims.mnc001.mcc001.3gppnetwork.org>;tag=4130282085
To: <sip:001011234567895@ims.mnc001.mcc001.3gppnetwork.org>
CSeq: 909056609 REGISTER
...

SIP/2.0 100 Trying
From: <sip:001011234567895@ims.mnc001.mcc001.3gppnetwork.org>;tag=4130282085
To: <sip:001011234567895@ims.mnc001.mcc001.3gppnetwork.org>
CSeq: 909056609 REGISTER
Call-ID: 4130282081_47464792@192.168.101.2
Via: SIP/2.0/UDP 192.168.101.2:5060;branch=z9hG4bK3987742761
Server: TelcoSuite Proxy-CSCF
Content-Length: 0
... 

SIP/2.0 401 Unauthorized - Challenging the UE
From: <sip:001011234567895@ims.mnc001.mcc001.3gppnetwork.org>;tag=4130282085
To: <sip:001011234567895@ims.mnc001.mcc001.3gppnetwork.org>;tag=a35a5806d6040414c4d26ea88c1e71a0-ec26680d
CSeq: 909056609 REGISTER
Call-ID: 4130282081_47464792@192.168.101.2
Via: SIP/2.0/UDP 192.168.101.2:5060;rport=5060;branch=z9hG4bK3987742761
WWW-Authenticate: Digest realm="ims.mnc001.mcc001.3gppnetwork.org", nonce="8SA0p/qltIMlBqyAM/vqAFr2Rj1SH4AAMadojvfm1sU=", algorithm=AKAv1-MD5, ck="b12bd6d3bf809a6cf001a58187353060", ik="66cb51e13b70780e328e43ea52951d3f", qop="auth,auth-int"
Path: <sip:term@pcscf.ims.mnc001.mcc001.3gppnetwork.org;lr>
Server: Kamailio S-CSCF
Content-Length: 0


REGISTER sip:ims.mnc001.mcc001.3gppnetwork.org SIP/2.0
From: <sip:001011234567895@ims.mnc001.mcc001.3gppnetwork.org>;tag=4130282241
To: <sip:001011234567895@ims.mnc001.mcc001.3gppnetwork.org>
CSeq: 909056610 REGISTER
Call-ID: 4130282081_47464792@192.168.101.2
Via: SIP/2.0/UDP 192.168.101.2:5060;branch=z9hG4bK1308331859
Max-Forwards: 70
P-Access-Network-Info: 3GPP-E-UTRAN-FDD; utran-cell-id-3gpp=001010001000019B
Content-Length: 0
Authorization: Digest username="001011234567895@ims.mnc001.mcc001.3gppnetwork.org",realm="ims.mnc001.mcc001.3gppnetwork.org",uri="sip:ims.mnc001.mcc001.3gppnetwork.org",qop=auth,nonce="8SA0p/qltIMlBqyAM/vqAFr2Rj1SH4AAMadojvfm1sU=",nc=00000001,cnonce="4130282079",algorithm=AKAv1-MD5,response="9dad9da7bd3272620d55ecb91d2ac017"
Expires: 600000
Supported: path
Allow: INVITE,BYE,CANCEL,ACK,NOTIFY,UPDATE,PRACK,INFO,MESSAGE,OPTIONS
Contact: <sip:192.168.101.2:5060>;+g.3gpp.icsi-ref="urn%3Aurn-7%3A3gpp-service.ims.icsi.mmtel";+g.3gpp.smsip;video;+sip.instance="<urn:gsma:imei:86728703-952237-0>";+g.3gpp.accesstype="cellular2"
```
Trong ví dụ trên Cseq tăng từ 909056609 REGISTER lên 909056610 REGISTER
  - Contact: các address bindings
    example:
    ``` 
    Contact: <sip:192.168.101.2:5060>;+sip.instance="<urn:gsma:imei:86728703-952237-0>";+g.3gpp.icsi-ref="urn%3Aurn-7%3A3gpp-service.ims.icsi.mmtel";+g.3gpp.smsip;video;+g.3gpp.accesstype="cellular2"
    ```
    Host part: 192.168.101.2
    Port: 5060
    Contact parameter: +sip.instance="<urn:gsma:imei:86728703-952237-0>"
                       +g.3gpp.icsi-ref="urn%3Aurn-7%3A3gpp-service.ims.icsi.mmtel"
                       +g.3gpp.smsip
                       video
                       +g.3gpp.accesstype="cellular2"
 - expires: tính bằng giây xác định thời gian mà UA binding có hiệu lực
### 10.2.1 Adding Binding
Như ví dụ ở hình 10.1, quá trình đăng ký bởi proxy server trong domain chicago.com và route request đó tới Carol's AOR 
#### 10.2.1.1 Setting the Expiration Interval of Contact Addresses
#### 10.2.1.2 Preferences among Contact Addresses
### 10.2.2 Removing Bindings
### 10.2.3 Fetching Bindings
### 10.2.4 Refreshing Bindings
### 10.2.6 Discovering a Registrar
### 10.2.7 Transmitting a Request
### 10.2.8 Error response
## 10.3 Processing REGISTER Requests
