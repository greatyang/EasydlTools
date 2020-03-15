import json
import os

def main():
    labelme_json_dir='D:\\fruit-recognition.zip\\Apple\\a'
    #easydl json file dir
    labelme_json_old_dir='D:\\fruit-recognition.zip\\Apple\\Apple A'    
 
    count = os.listdir(labelme_json_old_dir) 
    for i in range(0, len(count)):
        path = os.path.join(labelme_json_old_dir, count[i])
        #print("file ",path,"\n")
        if os.path.isfile(path) and path.endswith(".json"):
            data = json.load(open(path))
            easydldata = "{\"labels\":["
            firstshape = 1
            for shape in data['shapes']:
                label_name = shape['label']
                point_list = shape['points']
                #print("label ",label_name, "\n")
                x1 = point_list[0][0]
                y1 = point_list[0][1]
                x2 = point_list[1][0]
                y2 = point_list[1][1]
                #print("x1 ",x1, " y1 ",y1, " x2 ",x2, " y2 ",y2)
                if firstshape:
                    itemdata = "{\"name\": \""+label_name+"\",\"x1\":"+ str(x1) +",\"y1\":"+str(y1)+",\"x2\":"+str(x2)+",\"y2\":"+str(y2)+"}"
                    firstshape = 0
                else:
                    itemdata = ",{\"name\": \""+label_name+"\",\"x1\":"+ str(x1) +",\"y1\":"+str(y1)+",\"x2\":"+str(x2)+",\"y2\":"+str(y2)+"}"

                easydldata = easydldata + itemdata
            easydldata = easydldata + "]}"
            #remove labelme json file to labelme_json_dir
            new_path = os.path.join(labelme_json_dir, count[i])
            os.rename(path, new_path)
            #save easydl json file
            with open(path, "w") as json_file:
                json_file.writelines(easydldata)
                json_file.close()
            
if __name__ == '__main__':
    main()

