#windows中批量进行重命名文件，可以进行标号

import os
path=input('请输入文件路径(结尾加上\)：')
print('path:',path)       
out_path = 'C:\\Users\\qimos\\Desktop\\tt'
#获取该目录下所有文件，存入列表中
filelist_out=os.listdir(path)
print('filelist_out:',filelist_out)

m=0
for i in filelist_out:
	print('filelist_out[m]:',filelist_out[m])
	new_path = path+filelist_out[m]	
	print('new_path:',new_path)
	filelist=os.listdir(new_path)
	n=0
	for j in filelist:
		print('filelist[n]:',filelist[n])
		oldname=new_path + os.sep + filelist[n]
		newname=out_path + os.sep + filelist_out[m]+'_'+str(n+1)+'.jpg'
		os.rename(oldname,newname)   #用os模块中的rename方法对文件改名
		print(oldname,'======>',newname)
		n+=1
	m+=1
