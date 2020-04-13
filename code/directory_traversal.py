def directory_traversal(log, threshold):
    import matplotlib.pyplot as plt
    import pandas as pd
    
    weighted_keywords = [
        '../', '..\\', ':\\'
    ]
    
    keywords = [
        '/bin', '/dev', '/home', '/lib', '/misc', '/opt', 
        '/root', '/tftpboot', '/usr', '/boot', '/etc/', '/initrd', 
        '/lost+found', '/mnt', '/proc', '/sbin', '/tmp', '/var'
    ]
    
    hit_log = []
    keywords_in_line = [0 for i in range(len(log))]
    
    for i in range(len(log)):
        for j in range(len(weighted_keywords)):
            if weighted_keywords[j] in log[i]['request_url'].lower():
                keywords_in_line[i] += 10
                hit_log.append(log[i])
                
        for j in range(len(keywords)):
            if keywords[j] in log[i]['request_url'].lower():
                keywords_in_line[i] += 1
    
    dt_log = {}
    for i in range(len(log)):
        if keywords_in_line[i] != 0:
            dt_log[i] = keywords_in_line[i]
    
    dt_log_sorted = sorted(dt_log.items(), key=lambda x:x[1], reverse=True)
    
    dt_index,dt_value,dt_request = dt_per_time(hit_log)
    print_result(log, dt_log_sorted, dt_index, dt_value, len(dt_log), threshold)
    
    #グラフを表示
    dt_request.plot()
    plt.show()
    plt.close()
    
    
def dt_per_time(hit_log):
    import pandas as pd
    
    df = pd.DataFrame(hit_log)
    dt = df['remote_host']
    dt.index = pd.to_datetime(df['time'], format='%d/%b/%Y:%H:%M:%S')

    #リクエストを1分ごとにカウント
    dt_request = dt.resample('T').count()
    dt_request_sorted = dt_request.sort_values(ascending=False)
    index = dt_request_sorted.index
    value = dt_request_sorted.values
    
    return index, value, dt_request
    

def print_result(log, dt_log_sorted, dt_index, dt_value, total, threshold):
    print()
    print('##---------directory traversal---------##\n')
    print(f'total : {total}')
    print('---suspicious log per minute---')
    print('datetime            | num   | ratio')
    for i in range(5):
        datetime = dt_index[i]
        num = dt_value[i]
        percentage = '{:.2%}'.format(num / total)
        print(f'{datetime} | {num:<5} | {percentage:<5}')
    print('-------------------------------\n')
    print('-------suspicious log----------')
    print('n   | hit | request_url')
    i = 0
    while dt_log_sorted[i][1] >= threshold:
        num = dt_log_sorted[i][1]
        index = dt_log_sorted[i][0]
        output_url = log[index]['request_url']
        print(f'{i+1:<3} | {num:<3} | {output_url}')
        i += 1
    print('-------------------------------\n')
    print('##-------------------------------------##')

