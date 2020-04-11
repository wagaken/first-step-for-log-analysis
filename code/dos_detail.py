def dos_detail(log):
    import matplotlib.pyplot as plt
    import pandas as pd
    
    df = pd.DataFrame(log)
    df.index = pd.to_datetime(df['time'], format='%d/%b/%Y:%H:%M:%S')
    
    while 1:
        print('format  : year-month-day hour:min:sec')
        print('example : 2004-05-01 15:20:00')
        print('end     : input nothing(NULL)')
        print('period  : 2004-04-25 04:01:51 ~ 2004-10-10 04:20:13\n')
        print('time_from : ')
        time_from = input()
        print('time_to   : ')
        time_to = input()
        
        if not time_from and not time_to:
            exit()
        
        extracted_log = df[time_from : time_to]
        total = len(extracted_log)
        
        print()
        print('##---------------DoS detail---------------##\n')
        for type in ['remote_host', 'method', 'request_url', 
                     'response_code', 'user_agent']:
            index, value = count_by_type(type, extracted_log)
            if type == 'remote_host':
                print('---------count by IP address--------')
            elif type == 'method':
                print('-----------count by method----------')
            elif type == 'request_url':
                print('------------count by URL------------')
            elif type == 'response_code':
                print('-------count by response code-------')
            else:
                print('-------------count by UA------------')
            print('type            | num   | ratio')
            print_result(index, value, total)
            print('------------------------------------\n')
        print('##----------------------------------------##\n')


def count_by_type(type, extracted_log):
    target = extracted_log[type]
    target_num = target.value_counts()
    index = target_num.index
    value = target_num.values
    
    return index, value


def print_result(index, value, total):
    for i in range(len(index)):
            if i > 10:
                break
            percentage = '{:.2%}'.format(value[i] / total)
            print(f'{index[i]:<15} | {value[i]:<5} | {percentage:<5}')