Cả TCP và UDP đều là 2 giao thức nằm ở Transport layer 

| **TCP** | **UDP** |
|-------------------------|-------------------------|
| ![TCP](https://user-images.githubusercontent.com/101868484/205078097-bee26faa-44d0-4fbb-8b86-cf0495ce8006.png) | ![UDP](https://user-images.githubusercontent.com/101868484/205081553-ee62cfff-d99b-4e97-860b-368a93d3947f.png) | 
| connection-oriented, nghĩa là phải thực hiện thiết lập kết nối trước khi thực hiện truyền dữ liệu | connectionless, nó sẽ không thực hiện thao tác xây dựng kết nối trước khi truyền dữ liệu mà thực hiện truyền ngay lập tức khi có dữ liệu cần truyền=> truyền tải rất nhanh cho dữ liệu của Application layer | 
| Cơ chế Acknowledgement: Khi A gửi dữ liệu cho B, B nhận được thì gửi gói tin cho A xác nhận là đã nhận. Nếu không nhận được tin xác nhận thì A sẽ gửi cho đến khi B báo nhận thì thôi | Không có cơ chế Acknowledge: nó không quan tâm gói tin có đến tích hay không, không biết gói tin có bị mất trên đường đi hay không => dễ bị lỗi | 
| Cơ chế sequencing (đánh số thứ tự) cho các đơn vị dữ liệu được truyền => ráp các gói tin chính xác ở điểm nhận và loại bỏ gói tin trùng lặp | Không thực hiện cơ chế đánh số |
| Các cơ chế điều khiển luồng thích hợp (flow control) để tránh nghẽn xảy ra | Nhanh và hiệu quả hơn đối với các dữ liệu có kích thước nhỏ và yêu cầu khắt khe về thời gian | 
| Chậm vì nó thực hiện nhiều chức năng | Nhanh chóng vì nó cung cấp các chức năng hạn chế | 
Tốt nhất cho web, truyền file, email và SSH | Tốt nhất cho VPN< phát video trực tuyến, VoIP, phát sóng trực tiếp và chơi game trực tuyến. | 
|  | |
