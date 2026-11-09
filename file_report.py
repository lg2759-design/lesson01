def show_file_report(file_list):
    """显示文件扫描统计报告"""
    print("=" * 30)
    print("文件扫描报告")
    print("=" * 30)
    print(f"文件总数：{len(file_list)}")
    print("=" * 30)


if __name__ == "__main__":
    test_files = [
        "main.py",
        "file1.txt",
        "file2.txt"
    ]

    show_file_report(test_files)