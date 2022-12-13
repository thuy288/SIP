# OpenSIPS architecture
get images from this link
https://subscription.packtpub.com/book/networking-and-servers/9781785280610/2/ch02lvl1sec27/the-opensips-design

# OpenSIPS configuration file 
opensips.cfg: 
```
####### Global Parameters #########                             ----------------------------------
debug=3								| Global Configuration Parameters |
log_stderror=no							-----------------------------------
fork=yes
children=4
...
####### Modules Section ########
#set module path                                                -----------------
mpath="/usr/local/lib64/opensips/modules/"           		| Module loading |
#### SIGNALING module						-----------------
loadmodule "signaling.so"
...
#----------------setting module-specific parameters
modparam("mi_fifo","fifo_name","/tmp/oprnsips_fifo")            ---------------------------
modparam("rr","enable_full_lr", 1)				| MOdule Specific parameter |
modparam("rr", "append_fromtag", 0)				----------------------------
...
####### Routing Logic ########
# main request routing logic
route{								---------------------------
	if (!mf_process_maxfwd_header("10")) {  		|      Main routing block  |
		sl_send_reply("483","Too Many Hops");		 --------------------------
		exit;
	}
...
route[1] {
	# for INVITEs enable some additional helper routes
	if (is_method("INVITE")) {                                    ----------------------		
			if (isflagset(NAT)) {		              |    Routing blocks  |
			rtpproxy_offer("ro");			      -----------------------
		}
		t_on_branch("per_branch_ops");
		t_on_reply("handle_nat");
		t_on_failure("missed_call");
	}
	if (!t_relay()) {
		send_reply("500","Internal Error");
	};
	exit;
}
branch_route[per_branch_ops] {                     		---------------------------
	xlog("new branch at $ru\n");				|   Branch route blocks   |
}								---------------------------
onreply_route[handle_nat] {
	if (nat_uac_test("1"))
		fix_nated_contact();				---------------------------
	if ( isflagset(NAT) )					|   Reply routing blocks   |
		rtpproxy_answer("ro");				---------------------------
	xlog("incoming reply\n");
}
failure_route[missed_call] {					-----------------------------
	if (t_was_cancelled()) {				|   Failure routes blocks   |
		exit;						-----------------------------
	}
	# uncomment the following lines if you want to block client 
	# redirect based on 3xx replies.
	##if (t_check_status("3[0-9][0-9]")) {
	##t_reply("404","Not found");
	##	exit;
	##}	
}
```
OpenSIPS được xây dựng trên top của core chịu trách nhiệm cho những nhiệm vụ đơn giản và xử lý các SIp mesages.
OpensSIPS modules cho thấy những nhiệm vụ bên trong OpenSIPS script được config trong file *opensips.cfg* \
## Sections of the opensips.cfg file
- GLobal definitions: gồm những thông số làm việc trong OpenSIPS như là IP:PORT for SIP service và debug level. Nó ảnh hướng tới OpenSIPS core và tất cả các modules \
- Modules: gồm những thư viện bên trong được yêu cầu để thực hiện được những functions không có sẵn trong core. Được chạy với *loadmodule* \
- Modules configuration: các thông số cần để thiết lập thích hợp sử dụng syntax: 
  *modparam(modulename, parametername, parametervalue)* \
- Main routing block: là nơi bắt đầu quá trình SIP request. Nó kiểm soát quá trình của mỗi SIP request nhận được. \
- Secondary routing blocks: *route()* command nó giống như subroutines trong OpenSIPS script. \
- REply routing blocks: xử lý các reply messages (provisional, successful final replies, negative final replies) như là 200 OK \
- Failure routing blocks: xử lý các nguyên nhân dẫn đến thất bại như là: busy hoặc timeout \
- Branch routing blocks: gồm những logix được thực thi cho mỗi branch của SIP request, trước khi chuyển tiếp nó đi \
- Local routing blocks: thực thi khi OpenSIPS tạo một request (giống như UAS) sử dụng Transaction Module \
- Error routing block: thực thi khi phát hiện lỗi cú pháp SIP request. \
- Ngoài ra còn có: Request route, Start up route, Event route. 
## Phân biệt sessions (phiên), dialogs (hộp thoại), transactions (giao dịch) 
- SIP session: luồng media giữa hai thực thể SIP, ví dụ: audio, video, text \
- SIP dialog: một mối liên hệ tồn tại giữa 2 thực thể SIP trong một khoảng thời gian, ví dụ: dialog được thiết lập giữa hai UAC từ bản tin INVITE đến bản tin BYE \
- SIP transaction: là một SIP request gồm có request và response, ví dụ như REGISTER và 200 OK \ 
## Stateful operation



