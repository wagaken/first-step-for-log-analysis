# First step for log analysis
「ログ分析ことはじめ: セキュリティのためのApacheログ分析」のレポジトリです。<br>
https://www.amazon.co.jp/%E3%83%AD%E3%82%B0%E5%88%86%E6%9E%90-%E3%81%93%E3%81%A8%E3%81%AF%E3%81%98%E3%82%81-%E3%82%BB%E3%82%AD%E3%83%A5%E3%83%AA%E3%83%86%E3%82%A3%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AEApache%E3%83%AD%E3%82%B0%E5%88%86%E6%9E%90-%E6%88%91%E7%94%B0-%E5%81%A5%E4%BB%8B-ebook/dp/B0871YGBXW<br>
これらのコードはPython3で書かれています。<br>
They are writen in Python3.<br>
コードの可変や共有など、ご自由にお使いください。<br>

## Table of contents
1. combine_log.py
2. apache_parser.py 
3. check_request.py
4. apache_parser_v2.py
5. sql_injection.py
6. os_command_injection.py
7. os_command_injection_v2.py
8. directory_traversal.py
9. xss.py
10. csrf.py
11. dos_attack.py
12. dos_detail.py
## About dataset
Data hosted and ReadMe file provided by AZSecure Data and the University of Arizona Artificial Intelligence Lab. Citation information below.

file contains:
hnet-hon-10122004-var.tar.bz2
readme.txt

DESCRIPTION
This dataset consists of system logs from a Linux Redhat 7.1 system deployed in a honeynet.  The owner of the data runs a site for public domain, real-world log data in which malicious activities are captured.  One interesting aspect of this data is that there is no sanitization or anonymization; the data is provided unmodified (and no modifications are needed or required to use the data for research).  

file types:

Date range of data: 2006-2007, 590 days of continuous operation

Collection method: The data was collected from a Linux Redhat 7.1 system.
The following system logs were collected: /var/log/messages, /var/log/secure, /var/log/pacct, /var/log/httpd/access_log, /var/log/httpd/error-log, /var/log/mailog, /var/log/squid/access_log, /var/log/squid/store_log, /var/log/squid/cache_log, some other applications which write log data under /var
The raw logs are provided as-is, with no post-processing (sanitization or anonymization) performed.

Topics covered or keywords used:	honeynet, honeypot, linux, redhat, syslog, apache, sendmail, squid


HOW TO CITE THIS DATASET

Author(s): Anton A. Chuvakin


Title:  Linux Redhat 7.1 System Deployed in a Honeynet Logs

Publisher: AZSecure Data

Location: Copy and paste the location where you retrieve this file from within http://www.azsecure-data.org/ or use the DOI assigned to this digital object.

Publication date: May 2018


IEEE formatted citation:
A. A. Chuvakin, Linux Redhat 7.1 System Deployed in a Honeynet Logs, AZSecure Data. Available http://www.azsecure-data.org/ [2018]
