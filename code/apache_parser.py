import codecs

def apache_parser(file_name='access_log'):
    with codecs.open(file_name, 'r', 'utf-8', 'ignore') as f:
        log = []
        trash = []
        
        for line in f:
            try: 
                insert = {}
                
                entry = line.split(' ', 11)
                insert['remote_host'] = entry[0]
                insert['remote_log'] = entry[1]
                insert['remote_user'] = entry[2]
                insert['time'] = entry[3].lstrip('[') + ' ' + entry[4].rstrip(']')
                insert['request'] = (entry[5] + ' ' + entry[6] + ' ' + entry[7]).strip('"')
                insert['response_code'] = entry[8]
                insert['byte'] = entry[9]
                insert['referer'] = entry[10].strip('"')
                insert['user_agent'] = entry[11].strip('"')
               
                log.append(insert)
            except:
                #フォーマットに合わないものを出力
                trash.append(line)

    print('##------------parse-------------##')
    print('------------result----------')
    print(f'parsed log     : {len(log)}')
    print(f'non-parsed log : {len(trash)}')
    print('----------------------------\n')
    print('--------cannot parse--------')
    for i in range(len(trash)):
        print(trash[i])
    print('----------------------------\n')
    print('##------------------------------##\n')
    
    return log, trash
      