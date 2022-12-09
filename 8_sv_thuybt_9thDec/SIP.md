# 10.3 Processing REGISTER Requests
Registrar phải bỏ qua Record-Route header nếu nó trong bản tin REGISTER -> không gồm REcord-Route trong bất kỳ response nào từ REGISTER. \
Khi nhận được một REGISTER request thì registrar sẽ thực hiện theo các bước sau: 
1. Register kiểm tra Request-URI để xác định xem có truy cập được các liên kết trong Request-URI được hay không. Nếu không thì server sẽ đóng vai trò như một proxy server và forward request tới địa chỉ miền, 



