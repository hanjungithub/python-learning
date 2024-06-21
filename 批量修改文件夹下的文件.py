"""
批量修改文件夹下的文件名
1.开头添加
2.替换文件名中的内容
3.结尾添加
"""
import os


def modify_files_name():
    """
    批量修改文件名
    :return:
    """
    target_dir = input("请输入文件夹路径：")
    if not os.path.exists(target_dir):
        # 如果目录不存在，则退出程序
        print(f"目录不存在：'{target_dir}'")
        exit()
    flag = int(input("请输入操作(1:开头添加 2:替换文件名中的内容 3:结尾添加)："))
    if flag == 1:
        pre_content = input("请输入开头添加的内容：")
    elif flag == 3:
        end_content = input("请输入结尾添加的内容：")
    elif flag == 2:
        replace_signal = input("请输入文件名中的内容：")
        replace_content = input("请输入替换后的内容：")
    else:
        print("没有这种操作，程序结束")
        exit()
    for entry in os.scandir(target_dir):
        if entry.is_dir():
            pass
        elif entry.is_file():
            print(os.path.dirname(entry.path))
            print(f"原文件名：{entry.name}")
            file_name, file_ext = os.path.splitext(entry.name)
            if flag == 1:
                new_filename = pre_content + file_name + file_ext
                print(f"替换后文件名：{pre_content}{entry.name}")
                os.rename(entry.path, os.path.dirname(entry.path) + os.path.sep + new_filename)
            elif flag == 3:
                new_filename = file_name + end_content + file_ext
                print(f"替换后文件名：{new_filename}")
                os.rename(entry.path, os.path.dirname(entry.path) + os.path.sep + new_filename)
            elif flag == 2:
                file_name, file_ext = os.path.splitext(entry.name)
                new_filename = file_name.replace(replace_signal, replace_content) + file_ext
                print(f"替换后文件名：{new_filename}")
                os.rename(entry.path, os.path.dirname(entry.path) + os.path.sep + new_filename)
            else:
                pass


if __name__ == '__main__':
    modify_files_name()
