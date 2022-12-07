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
Một redirect server bao gồm có transaction layer và một transaction user có quyền truy cập vào location service của registrars và location services. 
