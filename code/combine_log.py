import codecs

def read_logfile(file_path):
    with codecs.open(file_path, 'r', 'utf-8', 'ignore') as f:
        #１ファイル丸ごと読み取り
        log = f.read()
    return log
    
    
def merge_log(file_name='access_log'):
    log =[]
    for i in range(26):
        #読み込むファイルのファイルパス
        if i == 0:
            read_file = 'httpd/' + file_name
        else:
            read_file = 'httpd/' + file_name + '.' + str(i);
        
        print(read_file)
        
        #対象のファイルを読み込んで、配列logに格納
        with codecs.open(read_file, 'r', 'utf-8', 'ignore') as f:
            add_log = f.read()
            
            if add_log: 
                log.extend(add_log)
            
    #配列logをfile_nameに書き込む
    with open(file_name, 'w') as output:
        for i in range(len(log)):
            output.write(log[i])
            


