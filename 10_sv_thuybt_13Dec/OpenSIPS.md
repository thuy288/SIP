- **menuconfig**: cung cấp bởi OpenSIPS để tự động tạo file cấu hình và trả lời trên m4 để dựng file cấu hình OpenSIPS 
# Scripting capabilities
capabilities trong dạng: functions, statements, variables, operators, assignments
## Scripting functions  
  Có 2 loại functions: 
  - cung cấp bởi OpenSIPS core: simple function, flexible protype,.. do core functions không giới hạn interface giữa OpenSIPS core và modules
  - cung cấp bởi modules: more rigorous protype, nó sử dụng 6 thông số và chỉ xử lý được các chuỗi
  Tất cả các functions thì đều trả về một giá trị integer: Failire: một giá trị âm, Success: một giá trị dương
## Scripting variables
  sử dụng để truy cập thông tin hoặc giữ thông tin tùy chỉnh. 
  OpenSIPS sử dụng nhiều biến và được nhận biết dựa trên:
  - Phạm vi hoặc khả năng của biến
  - Trạng thái read-write của biến
  - Cách xử lý multiple values  
  Example:
  ```
  $(<context>type(name)[index]{transformation})
  ```
  type: ru, var hoặc avp
  name: tên của biến đó
  index: tương tự như trong C/C++
  transformation: hành động có thể applied vào giá trị của biến
  context: reply (sử dụng trong failure route để yêu cầu một biến), request (sử dụng trong reply route để đánh giá biến trong request packet) 
  Ví dụ: 
  $ru: RIP request URI
  $hdr(from): From header
  $ci: SIP Call-ID
  $Ts: current time


