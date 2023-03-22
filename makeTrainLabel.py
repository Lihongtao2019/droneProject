import json
import os

label_path = r'.\labels\train'
paths = os.walk(r'.\images\train')
for path, dir_ls, _ in paths:
    for dir_name in dir_ls:
        new_folder_path = os.path.join(label_path, dir_name)
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)  # 新建文件夹
        json_path = os.path.join(path, dir_name)
        dict_open = open(os.path.join(json_path, "IR_label.json"), 'r', encoding='utf-8')
        load_dict = json.load(dict_open)  # 读入IR_label.json中的数据
        for i in range(1, len(load_dict['exist']) + 1):
            file_str = str(i).zfill(6) + ".txt"
            fout = open(os.path.join(new_folder_path, file_str), mode='w')
            id = load_dict['exist'][i - 1]
            if id == 1:
                x, y, w, h = load_dict['gt_rect'][i - 1]
                x = (x + w / 2) / 640
                y = (y + h / 2) / 512
                w /= 640
                h /= 512
                label_line = f"{id-1} {x:.6f} {y:.6f} {w:.6f} {h:.6f}"  # 根据位置信息计算出对应的yolo标签
                fout.write(label_line)

            fout.close()
        dict_open.close()

print("make labels of train successfully!")
