import os
import re

def extract_titles(md_file_path, level):
    titles = []
    pattern = r'{} (.+)'.format('#' * level)
    with open(md_file_path, "r", encoding="utf-8") as file:
        for line in file:
            match = re.match(pattern, line)
            if match:
                titles.append(match.group(1).replace("*", ""))
    return titles

def extract_h1_title(md_file_path):
    titles = extract_titles(md_file_path, 1)
    return titles[0] if titles else os.path.splitext(os.path.basename(md_file_path))[0]

def extract_h2_titles(md_file_path):
    return extract_titles(md_file_path, 2)

def slugify(title):
    slug = re.sub(r'[^\w\s-]', '', title.lower()).strip()
    return re.sub(r'[-\s]+', '-', slug)

def generate_md_links(directory):
    md_files = sorted(
        os.path.relpath(os.path.join(root, file), directory)
        for root, _, files in os.walk(directory)
        for file in files if file.endswith(".md") and file != "index.md"
    )
    
    links = []
    for f in md_files:
        h1_title = extract_h1_title(os.path.join(directory, f))
        h2_titles = extract_h2_titles(os.path.join(directory, f))
        link = f"<a href='{f[:-3]}'>{h1_title}</a>"
        if h2_titles:
            sub_links = "".join(f"<li><a href='{f[:-3]}#{slugify(title)}'>{title}</a></li>" for title in h2_titles)
            link += f"<ul>{sub_links}</ul>"
        links.append(link)
    return links

def generate_html_file(file_path, links):
    with open(file_path, "w", encoding="utf-8") as file_list:
        file_list.write("<html><body>\n")
        file_list.write("<h2>章节目录</h2>\n")
        file_list.write("<ul>\n")
        file_list.write("\n".join(f"<li>{link}</li>" for link in links))
        file_list.write("</ul>\n")
        file_list.write("</body></html>\n")

def process_directory(root_dir):
    for subdir, _, files in os.walk(root_dir):
        if "index.md" in files:
            links = generate_md_links(subdir)
            file_list_path = os.path.join(subdir, "file_list.html")
            generate_html_file(file_list_path, links)

if __name__ == "__main__":
    root_directory = "./docs/docs"  # 可以根据需要修改根目录
    process_directory(root_directory)
    print("File list generated successfully!")