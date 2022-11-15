import os
import random


def main():
    random.seed(0)  # 设置随机种子，保证随机结果可复现

    files_path = r"/data1/zjw/Dataset/ancient_character/test_images"

    # os.path.exists(files_path)判断括号内的文件（夹）是否存在，返回True或False
    # assert就是当其后面第一个判断语句为False时，输出后面的字符串信息，用来解释哪里出了问题
    # str.format()函数输出各式各样的字符串
    assert os.path.exists(files_path), "path: '{}' does not exist.".format(files_path)

    # 升序排列的图片文件名
    files_name =os.listdir(files_path)
    files_num = len(files_name)  

    # 建立训练数据和验证数据的空数组
    test_files = []

    # 遍历file_name数组，以val_index为索引，判断哪些文件归入训练集，哪些验证集
    for file_name in files_name:
        test_files.append(file_name)

    try:
        test_f = open("/data1/zjw/Dataset/ancient_character/test.txt", "x")  # open()打开文件，'x' for creating and writing to a new file
        test_f.write("\n".join(test_files))     # 写入文件

    except FileExistsError as e:                # except后面跟的是错误类型，如果有文件存在错误，将他as成e，并输出
        print(e)
        exit(1)


if __name__ == '__main__':
    main()
