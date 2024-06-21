import os


def just_copy_dir(source_dir, target_dir, need_sub_folder):
    """
    只拷贝文件夹目录，不拷贝里面的文件

    :param source_dir: 源路径
    :param target_dir: 目标路径
    :param need_sub_folder: 是否需要遍历子目录（0：不需要 1：需要）
    :return: None
    """
    # 检查源目录是否存在
    if not os.path.exists(source_dir):
        # 如果源目录不存在，则退出程序
        print(f"源目录不存在：'{source_dir}'")
        exit()
    print(f"源目录存在：{source_dir}")
    # 检查目标目录是否存在
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
        print(f"目标目录创建成功：{target_dir}")
    for entry in os.scandir(source_dir):
        if entry.is_dir():
            # print(f"目录：{entry.name}")
            # 用这个文件夹的名称，在新的目录下创建一个新的空文件夹
            # print(target_dir + os.path.sep + entry.name)
            if not os.path.exists(target_dir + os.path.sep + entry.name):
                os.mkdir(target_dir + os.path.sep + entry.name)
                print(f"目录创建成功：{target_dir + os.path.sep + entry.name}")
            else:
                print(f"目录已存在：{target_dir + os.path.sep + entry.name}")
            if need_sub_folder == 1:
                just_copy_dir(entry.path, target_dir + os.path.sep + entry.name, need_sub_folder)
        elif entry.is_file():
            # print(f"文件：{entry.name}")
            pass
        else:
            pass
            # print(f"其他：{entry.name}")


if __name__ == '__main__':
    source = input("请输入源目录：")
    target = input("请输入目标目录：")
    flag = int(input("是否需要遍历子目录（0：不需要 1：需要）："))
    just_copy_dir(source, target, flag)
