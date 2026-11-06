# My first Git mananged project
from pathlib import Path
import csv

def create_file_list(folder):
    folder = Path(folder)

    if not folder.exists() or not folder.is_dir():
        print("文件夹不存在，请检查路径。")
        return

    output = Path("file_list.csv")

    with output.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["文件名称", "文件类型", "大小（KB）"])
        file_count=0;

        for item in folder.rglob("*"):
            if not item.is_file():
                continue
            if ".git" in item.relative_to(folder).parts:
               continue
            if item.resolve() == output.resolve():
              continue
            
            file_count += 1
            writer.writerow([
                item.name,
                item.suffix,
                round(item.stat().st_size / 1024, 2)
            ])

    print(f"清单生成成功：{output.resolve()}")
    print(f"文件总数：{file_count}")

if __name__ == "__main__":
    target = input("请输入需要扫描的文件夹路径：")
    create_file_list(target)
