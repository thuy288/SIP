# OpenSIPS configuration file 
opensips.cfg: 
```
####### Global Parameters #########
debug=3
log_stderror=no
fork=yes
children=4
...
####### Modules Section ########

#set module path
mpath="/usr/local/lib64/opensips/modules/"
#### SIGNALING module
loadmodule "signaling.so"
...
#----------------setting module-specific parameters
modparam("mi_fifo","fifo_name","/tmp/oprnsips_fifo")
modparam("rr","enable_full_lr", 1)
modparam("rr", "append_fromtag", 0)
...
####### Routing Logic ########
# main request routing logic
route{
	if (!mf_process_maxfwd_header("10")) {
		sl_send_reply("483","Too Many Hops");
		exit;
	}
...
route[1] {
	# for INVITEs enable some additional helper routes
	if (is_method("INVITE")) {
		
			if (isflagset(NAT)) {
			rtpproxy_offer("ro");
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
branch_route[per_branch_ops] {
	xlog("new branch at $ru\n");
}
onreply_route[handle_nat] {
	if (nat_uac_test("1"))
		fix_nated_contact();
	if ( isflagset(NAT) )
		rtpproxy_answer("ro");
	xlog("incoming reply\n");
}
failure_route[missed_call] {
	if (t_was_cancelled()) {
		exit;
	}
	# uncomment the following lines if you want to block client 
	# redirect based on 3xx replies.
	##if (t_check_status("3[0-9][0-9]")) {
	##t_reply("404","Not found");
	##	exit;
	##}	
}
```

