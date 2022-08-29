import os
import sys
import yaml
def qiangbao():
    with open('Data_DMS/biaodanData.yaml', mode='r', encoding='utf-8') as  fileopen:
        data=yaml.safe_load(fileopen)
        return data['qiangbao']
def text():
    with open('Data_DMS/biaodanData.yaml', mode='r', encoding='utf-8') as  fileopen:
        data=yaml.safe_load(fileopen)
        return data['test']
if __name__ == '__main__':
    print(text())
    # print(sys.path)
    # rootpath='工程所在目录'
    # sys.path=[]
    # sys.path.extend([rootpath+i for i in os.listdir(rootpath) if i[0]!="."])
    # sys.path.extend(sys.path)
    # print(sys.path)