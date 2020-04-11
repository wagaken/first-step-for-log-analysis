def sql_injection(log, threshold):
    keywords = [
        "'", '&#039', '*', ';', '%20', '--',
        'SELECT', 'select',
        'DELETE', 'delete',
        'CREATE', 'create',
        'DROP', 'drop',
        'ALTER', 'alter',
        'INSERT', 'insert',
        'UPDATE', 'update',
        'SET', 'set',
        'FROM', 'from',
        'WHERE', 'where',
        'UNION', 'union',
        'ALL', 'all',
        'LIKE', 'like',
        'AND', 'and', '&',
        'OR', 'or', '|',
        'user', 'username', 'passwd', 'id', 'admin', 'information_schema'
     ]
    
    command_in_line = [0 for i in range(len(log))]
    
    for i in range(len(log)):
        for j in range(len(keywords)):
            if keywords[j] in log[i]['request_url']:
                command_in_line[i] += 1
    
    sql_log = {}
    for i in range(len(log)):
        if command_in_line[i] != 0:
            sql_log[i] = command_in_line[i]
    
    sql_log_sorted = sorted(sql_log.items(), key=lambda x:x[1], reverse=True)
    
    print('##---SQL injection---##')
    print(f'total : {len(sql_log)}\n')
    print('n   | hit | request_url')
    i = 0
    while sql_log_sorted[i][1] >= threshold:
        num = sql_log_sorted[i][1]
        index = sql_log_sorted[i][0]
        output_url = log[index]['request_url']
        print(f'{i+1:<3} | {num:<3} | {output_url}')
        i += 1
    print('##-------------------##\n')

