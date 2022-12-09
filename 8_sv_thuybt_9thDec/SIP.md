# 10.3 Processing REGISTER Requests
Registrar phải bỏ qua Record-Route header nếu nó trong bản tin REGISTER -> không gồm REcord-Route trong bất kỳ response nào từ REGISTER. \
Khi nhận được một REGISTER request thì registrar sẽ thực hiện theo các bước sau: 
1. Register kiểm tra Request-URI để xác định xem có truy cập được các liên kết trong Request-URI được hay không. Nếu không thì server sẽ đóng vai trò như một proxy server và forward request tới địa chỉ miền/
2. Registrar phải xử lý *Require* header như đã trình bày ở trước
3. Registrar xác thực UAC. 
  - Trong SIP, UAS dùng phản hồi 401 (Unauthorized) để challenge danh tính của UAC. 
   ```
    SIP/2.0 401 Unauthorized - Challenging the UE
  From: <sip:001011234567895@ims.mnc001.mcc001.3gppnetwork.org>;tag=4130282085
  To: <sip:001011234567895@ims.mnc001.mcc001.3gppnetwork.org>;tag=a35a5806d6040414c4d26ea88c1e71a0-ec26680d
  CSeq: 909056609 REGISTER
  Call-ID: 4130282081_47464792@192.168.101.2
  Via: SIP/2.0/UDP 10.4.128.21;branch=z9hG4bKfa72.c2d75ce7f4e35a4124314640bff032ec.1
  Via: SIP/2.0/UDP 192.168.101.2:5060;rport=5060;branch=z9hG4bK3987742761
  WWW-Authenticate: Digest realm="ims.mnc001.mcc001.3gppnetwork.org",    nonce="8SA0p/qltIMlBqyAM/vqAFr2Rj1SH4AAMadojvfm1sU=", algorithm=AKAv1-MD5, ck="b12bd6d3bf809a6cf001a58187353060", ik="66cb51e13b70780e328e43ea52951d3f", qop="auth,auth-int"
  Path: <sip:term@pcscf.ims.mnc001.mcc001.3gppnetwork.org;lr>
  Server: Kamailio S-CSCF
  Content-Length: 0
  ```
  Proxies sử dụng response 407 (Proxy Authentication Required), vì trong đó có Proxy-Authenticate, Proxy-Authenrization, WWW-Authenticate, Authorization 
  *Realm*: unique, là một chuỗi có tên người dùng và domain 
  User-to-User Authentication: WWW-authenticate 
  ```
  Authorization: Digest username="001011234567895@ims.mnc001.mcc001.3gppnetwork.org",realm="ims.mnc001.mcc001.3gppnetwork.org",uri="sip:ims.mnc001.mcc001.3gppnetwork.org",qop=auth,nonce="8SA0p/qltIMlBqyAM/vqAFr2Rj1SH4AAMadojvfm1sU=",nc=00000001,cnonce="4130282079",algorithm=AKAv1-MD5,response="9dad9da7bd3272620d55ecb91d2ac017"
  ```
  Sau khi nhận phản hồi 401 thì UAC re-originate request, UAs sẽ lưu lại To và realm để tái sử dụng trong lần request tiếp theo 
Nếu không có mechanism vào sẵn sàng thì registrar có thể lấy danh tính từ From để khởi tạo request
4. Registrar xác định xem người dùng xác thực có được phép sửa đổi đăng ký for AOR hay không. Nếu người dùng được xác thực đó không được xem modify binding thì Registrar sẽ phản hồi 403 và bỏ qua các bước sau. 
5. Từ AOR ở To header nếu nó không valid với domain ở Request-URI thì registrar sẽ trả về 404 (Not Found) và bỏ quá các bước còn lại. 
6. Regsitrar check request có Contact header hay không. Nếu không thì bỏ qua bước cuối cùng (bước 8) 
   Còn nếu có thì registrar sẽ check nếu có một giá trị có "*" và Expires, nếu có thì request là không hợp lý và trả về 400 (Invalid Request). \
   Check Call-ID với giá trị được lưu trong AOR cho mỗi binding. Nếu KHông thì sẽ xóa binding, còn nếu được thì xóa binding duy nhất nếu như CSeq trong request cao hơn giá trị trong binding đó. 
   ```
   check Contact header----------> skip to the last steps 
   |                      False
   | True
   |
   v
   check '*' và Expires trong Contact -------------------> 400 Invalid Request
   |                                     True
   | False
   |
   v
   Check Call-ID --------------------> remove the binding
   |                  False
   | True
   |
   v 
   remove the binding chỉ khi Cseq ở request cao hơn giá trị lưu cho binding đó
   ```
  7. Registrar xử lý mỗi địa chỉ contact trong Contact header 
    ```
    expiration interval > 0 && < one hour && <= registrar-configured minimum ---------> reject - 403 (interval Too Brief) 
    |
    |
    |
    v
    For each address, registrar tìm danh sách  -----------------> tentatively added
    các binding đang chạy từ URI                   không tồn tại
    |
    |  tồn tại
    |
    v
    check Call-ID trong binding đang tồn tại khác với Call-ID trong request -----------------------> removed
    |                                                                          expiration time là 0
    | same
    |
    v
    registrar so sánh giá trị Cseq -------------------> update or remove the binding 
    |                                  higher
    | not higher
    |
    v
    not update and the request failed
    ```
    nếu tất cả các binding không thành công thì request sẽ fail với response 500 (server error) 
  8. Regsitrar trả về 200 OK. Trong bản tin đó có Contact header gồm tất cả các binding hiện tại. 
   


