#https://github.com/UT0P1C/adminfinder_python
import sys
import requests as r
#
#
#
#
#DEVELOPED BY
#  _   _   _____    ___    ____    _    ____ 
#| | | | |_   _|  / _ \  |  _ \  / |  / ___|
#| | | |   | |   | | | | | |_) | | | | |    
#| |_| |   | |   | |_| | |  __/  | | | |___ 
# \___/    |_|    \___/  |_|     |_|  \____|
                                            

url = raw_input("digite a url do site: ")

url_dir = ["adm/", "admin/", "admin.php", "administrator/", "wp-admin/", "wp-login/" ,"painel/", "panel/", "controle/", "controle.php", "painel.php", "cpanel/", "administrador", "myadmin/index.php"]

print ("testando a url: ", url)
for Dir in url_dir:
	testar = url + Dir
	checa = r.get(testar)
	if checa.status_code == 200 and "login" in checa.text:
		print ("admin encontrado > ", testar);
	else:
		print ("admin NAO encontrado > ", testar);


