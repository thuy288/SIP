# Dialogs
peer-to-peer SIP giữa hai UA
Một dialog được xác định ở mỗi UA với dialog ID, nó gồm giá trị Call-ID, local tag và remote tag. 
- Dialog ID ở mỗi UA trong dialog thì không giống nhau
- local tag ở mỗi UA thì xác định cho remote tag ở peer UA
- với UAC, giá trị Call-ID của dialog ID được đặt thành tag trong trường **To**. Local tag được set thành tag trong trường **From**
- với UAS, giá trị Call-ID của dialog ID được đặt thành Call-ID, remote tag được đặt thành tag trong trường **From**, local tag được đặt thành tag trong trường **To**
Tạo một Dialog
qua non-failure responses tới các yêu cầu bằng các phương pháp:
- phản hồi 2xx và 101-199 với To tag, nơi là request là INVITE sẽ thiết lập một dialog
Quá trình cụ thể sẽ được trình bày ở đoạn sau
# Method Inspection (phương pháp kiểm tra)
Khi request được xác thực (hoặc xác thực bị bỏ qua), UAS phải kiểm tra method của request đó. Nếu UAS nhận ra nhưng không hỗ trợ cho method của request thì nó sẽ tạo phản hồi 405 (Method Note Allowed). 
Quá trình tạo phản hồi như sau:
- Sending a Provisional Response: UAS nên tại phản hồi cuối tới non-INVITE request nhanh nhất có thể. Khi 100 Trying được tạo, bất kỳ trường Timestamp trong request cần phải copy vào 100 Trying đó. Nếu có thời gian delay thì UAS nên thêm giá trị delay vào giá trị Timestamp. 
- Headers and Tags: Trường **From** của response và request phải giống nhau. Trường **Call-ID, CSeq, Via** ở response = request. Nếu một request có một To tag thì trường **To** trong response = request. Tuy nhiên, nếu trường To ở request không có tag thì URI trong trường To ở response = URI trong trường **To** trong response. 
UAS cxung phải thêm một trường Allow vào phản hồi 405. Trường Allow sẽ phải gồm danh sách các methods hỗ trợ bởi UAS tạo ra cái message. 
# Stateless UAS Behavior
