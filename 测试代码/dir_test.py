import os
def get_fileList_from_dir_string(dir='./dcm'):
    file_list=[]
    paths=os.walk(dir)
    for path,dir_list,file_lst in paths:
        for filename in file_lst:
            file_list.append (os.path.join(path,filename))
    return file_list

if __name__=="__main__":
    dir='./dcm'
    filelist=get_fileList_from_dir_string(dir)
    for file in filelist:
        print(file)
        