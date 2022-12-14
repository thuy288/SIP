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
một INVITE thành công sẽ tạo nên một dialog và session sử dụng offer-answer model. \
khi modify có thể thay đổi địa chỉ ports, thêm media stream, xóa media stream,... bằng cách gửi re-INVITE (re-INVITE có thể modify dialog và các thông số của session) 
## UAC Behavior






