import os
from os import listdir, getcwd
from os.path import join
if __name__ == '__main__':
    source_folder='/home/zecheng/Desktop/dac-dataset/JPEGImages'#地址是所有图片的保存地点
    dest='/home/zecheng/Desktop/dac-dataset/train.txt' #保存train.txt的地址
    dest2='/home/zecheng/Desktop/dac-dataset/val.txt'  #保存val.txt的地址
    dest3='/home/zecheng/Desktop/dac-dataset/trainval.txt'  #保存trainval.txt的地址
    file_list=os.listdir(source_folder)       #赋值图片所在文件夹的文件列表
    train_file=open(dest,'a')                 #打开文件
    val_file=open(dest2,'a')                  #打开文件
    trainval_file=open(dest3,'a')              #打开文件
    file_num=0
    for file_obj in file_list:                #访问文件列表中的每一个文件
        file_path=os.path.join(source_folder,file_obj) 
        #file_path保存每一个文件的完整路径
        file_name,file_extend=os.path.splitext(file_obj)
        #file_name 保存文件的名字，file_extend保存文件扩展名 
        if(file_num<12949): #and file_num%4!=0):                     #前面是你的图片数目，后面是为了保留文件用于训练
            #print file_num
            trainval_file.write(file_name+'\n')
            train_file.write(file_name+'\n')  #用于训练前900个的图片路径保存在train.txt里面，结尾加回车换行
        else :
            val_file.write(file_name+'\n')    #其余的文件保存在val.txt里面
        file_num+=1
    train_file.close()#关闭文件
    val_file.close()
    trainval_file.close()
