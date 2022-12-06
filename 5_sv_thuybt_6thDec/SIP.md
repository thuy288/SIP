# Header Insprction
Nếu UAS không hiểu được header trong 1 request thì server sẽ bỏ qua header đó và tiếp tục quá trình message. Một UAS nên bỏ qua những header không đúng định dạng (tức là nó là những cái không cần thiết cho quá trình request)
# To and Request-URI
Header **To** xác định người nhận được chỉ định từ đầu (ví dụ là địa chỉ của người được gọi) bởi người dùng đã được xác định trong header **From**
- Người nhận không bắt buộc là UAS trong quá trình request, có thể là call forwarding hoặc các hoạt proxy khác. 
- Thường thì UAS sẽ chấp nhận requests kể cả nếu nó không nhận dạng được scheme của URI (ví dụ, tel: URI) trong header To, hoặc header To không đề cập đến người dùng đã biết hoặc hiện tại của UAS đó
- Nếu UAS reject một request thì nó sẽ tạo ra một response 403 (Forbidden) và chuyển nó tới server transaction để tiến hành truyền đi.
Request-URI xác định UAS xử lý yêu cầu. Khác với header To thì Request-URI sẽ không hỗ trợ bởi UAS nếu nó không đúng form và trả về phản hồi 416 (Unsupported URI Scheme). 
- Request-URI không xác định địa chỉ mà UAS đã có thể chấp nhận request, nó nên reject request đó với response 404 (Not Found). 
- Thông thường một UA sử dụng REGISTER method để liên két AOR tới một contact cụ thể sẽ thấy các yêu cầu mà Request-URI ~ contact address.
- Request-URI gồm có header **Contact** của requests và responses gửi bởi UA để thiết lập hoặc làm mới dialogs.
