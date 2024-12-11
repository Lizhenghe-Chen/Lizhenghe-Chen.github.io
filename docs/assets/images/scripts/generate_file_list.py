import os
import re


def extract_h1_title(md_file_path):
    with open(md_file_path, "r", encoding="utf-8") as file:
        for line in file:
            match = re.match(r"# (.+)", line)
            if match:
                return match.group(1).replace("*", "")
    return os.path.splitext(os.path.basename(md_file_path))[0]


def extract_h2_titles(md_file_path):
    h2_titles = []
    with open(md_file_path, "r", encoding="utf-8") as file:
        for line in file:
            match = re.match(r"## (.+)", line)
            if match:
                # replace '*' with ''
                h2_titles.append(match.group(1).replace("*", ""))
    return h2_titles


# def extract_h3_titles(md_file_path):
#     h3_titles = []
#     with open(md_file_path, "r", encoding="utf-8") as file:
#         for line in file:
#             match = re.match(r"### (.+)", line)
#             if match:
#                 # replace '*' with ''
#                 h3_titles.append(match.group(1).replace("*", ""))
#     return h3_titles
def slugify(title):
    # 根据 `case: lower` 的规则，将字符串转换为小写
    slug = title.lower()
    # 替换空格为 `-`（常见 slug 生成规则）
    slug = re.sub(r'\s+', '-', slug)
    # 移除特殊字符（如需保留特殊字符，此步骤可以省略）
    slug = re.sub(r'[^\w\-]', '', slug)
    return slug

def generate_md_links(directory):
    md_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md") and file != "index.md":
                relative_path = os.path.relpath(os.path.join(root, file), directory)
                md_files.append(relative_path)
    md_files.sort()  # 按文件名排序
    links = []
    for f in md_files:
        h1_title = extract_h1_title(os.path.join(directory, f))
        h2_titles = extract_h2_titles(os.path.join(directory, f))
        # h3_titles = extract_h3_titles(os.path.join(directory, f))
        link = f"<a href='{f[:-3]}'>{h1_title}</a>"
        if h2_titles:
            # use # to add permnent link
            # sub_links = "".join([f"<li>{title}</li>" for title in h2_titles])
            sub_links="".join([f"<li><a href='{f[:-3]}#{slugify(title)}'>{title}</a></li>" for title in h2_titles])
            link += f"<ul>{sub_links}</ul>"
        links.append(link)
    return links


def process_directory(root_dir):
    for subdir, _, files in os.walk(root_dir):
        if "index.md" in files:
            links = generate_md_links(subdir)
            file_list_path = os.path.join(subdir, "file_list.html")
            with open(file_list_path, "w", encoding="utf-8") as file_list:
                file_list.write("<html><body>\n")
                file_list.write("<h2>章节目录</h2>\n")
                file_list.write("<ul>\n")
                for link in links:
                    file_list.write(f"<li>{link}</li>\n")
                file_list.write("</ul>\n")
                file_list.write("</body></html>\n")


if __name__ == "__main__":
    root_directory = "./docs/docs"  # 可以根据需要修改根目录
    process_directory(root_directory)
    print("File list generated successfully!")
