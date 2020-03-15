import os
if __name__ == "__main__":
    rootdir = 'D:\\fruits-360\\Training'
    count = 0
    index = 0
    dirlist = os.listdir(rootdir) 
    for i in range(0, len(dirlist)):
        label = dirlist[i].replace(' ','')
        #print(dirlist[i] + ' ' + label + " length is " + str(len(label)))
        path = os.path.join(rootdir, dirlist[i])
        print("Now in "+path)
        filelist = os.listdir(path)
        for j in range(0, len(filelist)):
            #create and write json file
            jsonname = str(index) + "_" + filelist[j].replace('jpg','json')
            jsonpath = os.path.join(rootdir, jsonname)
            with open(jsonpath, "w") as jsonfile:
                #detection json format
                jsonfile.writelines("{\"labels\": [{\"name\": \""+label+"\",\"x1\":0,\"y1\":0,\"x2\":99,\"y2\":99}]}")
                #classification json format
                #jsonfile.writelines("{\"labels\": [{\"name\": \""+label+"\"}]}")
                jsonfile.close()
            
            #rename jpg file to rootdir
            newname = os.path.join(rootdir, str(index) + "_" + filelist[j])
            oldname = os.path.join(path, filelist[j])
            #print("newname "+newname+" oldname "+oldname)
            os.rename(oldname, newname)
            count += 1
        
        os.rmdir(path)
        index +=1
    print("Count is "+str(count)+" index is "+str(index))
                
