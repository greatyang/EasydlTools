import os
from PIL import Image
#从大小为1280*720的图片中截取区域(280,0,1000,720)的区域
if __name__ == "__main__":
    rootdir = 'E:\\apple\\test'
    count = 0
    index = 0
    x1 = 280
    y1 = 0
    x2 = 1000
    y2 = 720
    dirlist = os.listdir(rootdir) 
    for i in range(0, len(dirlist)):
        label = dirlist[i].replace(' ','')
        #print(dirlist[i] + ' ' + label + " length is " + str(len(label)))
        path = os.path.join(rootdir, dirlist[i])
        print("Now in "+path)
        filelist = os.listdir(path)
        for j in range(0, len(filelist)):
            imgpath = os.path.join(path, filelist[j])
            #print("file ",imgpath,"\n")
            if os.path.isfile(imgpath) and imgpath.endswith(".jpg"):
                img = Image.open(imgpath)
                region = img.crop((x1, y1, x2, y2))
                region.save(imgpath)
                count += 1
        index +=1
    print("Count is "+str(count)+" index is "+str(index))
                
