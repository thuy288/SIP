# 1. SIP registering process
![image](https://user-images.githubusercontent.com/101868484/205804613-eeac5f95-f876-4f2e-90df-95e4606bbc1d.png)  
SIP protocol có một thành phần gọi là REGISTRAR, nó là máy chủ chấp nhận các yêu cầu REGISTER và lưu thông tin nhận được tỏng cái gói trên location server để quản lý domains của chúng.
Location database lưu lại các thông tin 
![317841359_875754330403070_5599846798681077280_n](https://user-images.githubusercontent.com/101868484/205807671-38081c24-2c88-4372-a62c-ed0b09cbaae3.jpg)

# OpenSIPS
Là một open source SIP proxy server 
- Speed: nó có thể handle rất nhiều cuộc gọi trong mỗi giây
- Flexibility: Script language to define the administrators's behavior. 
- OpenSIPS is exendable
- Portability: được viết trong ANSI C -> portable and available to UNIX-like systems such as Linux, Solaris, and BSD
- Small footprint: dung lượng core nhỏ nên sử dụng được ở nhiều nền tảng nhúng
- Usage scenarios
