from apache_parser_v2 import apache_parser
from sql_injection import sql_injection
from os_command_injection_v2 import os_command_injection
from dos_attack import dos_attack
from dos_detail import dos_detail
from directory_traversal import directory_traversal
from xss import xss
from csrf import csrf

log,trash = apache_parser()
#sql_injection(log, threshold=8)
os_command_injection(log, threshold=20)
#dos_attack(log)
#dos_detail(log)
#directory_traversal(log, threshold=11)
#xss(log)
#csrf(log)
