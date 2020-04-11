def os_command_injection(log, threshold):
    keywords = [
        ';', '|', '&', "'", '(', ')', '<', '>', '$', '*', 
        '?', '{', '}', '[', ']', '%', '!', '"', '#', '+', 
        ',', '-', '.', '/', ':', '=', '@', '^', '~',
        'rm', 'cat', 'wget', 'curl', 'sudo', 
        'ssh', 'usermod', 'useradd', 'grep',
        '/bin', '/dev', '/home', '/lib', '/misc', '/opt', 
        '/root', '/tftpboot', '/usr', '/boot', '/etc', '/initrd', 
        '/lost+found', '/mnt', '/proc', '/sbin', '/tmp', '/var'
    ]
    
    command_in_line = [0 for i in range(len(log))]
    
    for i in range(len(log)):
        for j in range(len(keywords)):
            if keywords[j] in log[i]['request_url']:
                command_in_line[i] += 1
                
        if '\\' in repr(log[i]['request_url']):
                command_in_line[i] += 1
    
    sql_log = {}
    for i in range(len(log)):
        if command_in_line[i] != 0:
            sql_log[i] = command_in_line[i]
    
    sql_log_sorted = sorted(sql_log.items(), key=lambda x:x[1], reverse=True)
    
    print('##---OS command injection---##')
    print(f'total : {len(sql_log)}\n')
    print('n   | hit | request_url')
    i = 0
    while sql_log_sorted[i][1] >= threshold:
        num = sql_log_sorted[i][1]
        index = sql_log_sorted[i][0]
        output_url = log[index]['request_url']
        print(f'{i+1:<3} | {num:<3} | {output_url}')
        i += 1
    print('##--------------------------##\n')

