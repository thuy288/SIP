## Analysis of the opensips.cfg file
```
loadmodule "db_mysql.so" #make the authentication work 
loadmodule "auth.so"
loadmodule "auth_db.so"
```
```
modparam("auth_db", "calculate_ha1", 1) #MySQL support , calculate_ha1: tell the auth_db module to use plaintext passwords 
modparam("usrloc", "db_mode", 2) #db_mode: tell the usrloc module to store and retrieve the AOR records
```

## The REGISTER requests
```
if (is_method("REGISTER"))
  {
    # authenticate the REGISTER requests
    if (!www_authorize("", "subscriber"))
   {
      www_challenge("", "0"); #2 parameter: realm, "0": not include QOP 
      exit;
   }
  if (!db_check_to())
  {
    sl_send_reply("403","Forbidden auth ID");
    exit;
  }
  if ( proto==TCP) setflag(TCP_PERSISTENT);
  
  # systems lưu location data cho UAC đó
  if (!save("location"))  
    sl_reply_error();
  
  exit;
}
```
## The non-REGISTER requests
```
if (!(is_method("REGISTER")))
{
  if (from_uri==myself) #handling a domain served by our proxy
  {
    # authenticate if from local subscribers
    #(domain in FROM URI is local)
    if (!proxy_authorize("", "subscriber")) { #check the authentication headers
      proxy_challenge("", "0");
      exit;
    }
    if (!db_check_from()) { #map SIP users with authentication user
      sl_send_reply("403","Forbidden auth ID");
      exit;
    }

    consume_credentials(); #remove thr Authorize header from request before relaying
      # caller authenticated
   } else {
    # if caller is not local
    if (!uri==myself) {
      send_reply("403","Relay forbidden");
      exit;
    }
  }
}
```
