import os
import json

root_path = r'.\images\test'
result_path = r'.\result'
paths = os.walk(root_path)
for _, dir_ls, __ in paths:
    for dir_name in dir_ls:
        dic_path = os.path.join(root_path, dir_name)
        dict_open = open(os.path.join(dic_path, 'IR_label.json'), 'r', encoding='utf-8')
        data = json.load(dict_open)
        dict_open.close()
        images = os.walk(dic_path)
        for ___, ____, file_ls in images:
            for file_name in file_ls:
                if file_name != '000001.jpg' and file_name.endswith("jpg"):
                    label_path = os.path.join(dic_path, file_name).replace("images", "labels").replace("jpg", "txt")
                    if os.path.exists(label_path):
                        fin = open(label_path)
                        line = fin.readline().split(' ')
                        fin.close()
                        xc = int(640 * float(line[1]))
                        yc = int(512 * float(line[2]))
                        w = int(640 * float(line[3]))
                        h = int(512 * float(line[4]))
                        data['res'].append([int(xc - w / 2), int(yc - h / 2), w, h])
                    else:
                        data['res'].append([])
        write_path = os.path.join(result_path, dir_name + ".txt")
        file_write = open(write_path, 'w')
        str_data = json.dumps(data)
        file_write.write(str_data)
        file_write.close()


print("results of test have saved into result folder!")
