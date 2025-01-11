import os
import shutil
from markdownblocks import markdown_to_html_node
def main():
    source_directory = "./static"
    destination_directory = "./public"
    if os.path.exists(destination_directory):
        shutil.rmtree(destination_directory)
    
    copy_directory(source_directory, destination_directory)
    
    generate_page("./content/index.md", "template.html", "./public/index.html")


def copy_directory(src, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.makedirs(dest)
    def recursive_copy(src, dest):
        for item in os.listdir(src):
            src_path = os.path.join(src, item)
            dest_path = os.path.join(dest, item)
            if os.path.isdir(src_path):
                os.makedirs(dest_path)
                recursive_copy(src_path, dest_path)
            else:
                shutil.copy2(src_path, dest_path)
            print(f"Copied {src_path} to {dest_path}")

    recursive_copy(src, dest)

def extract_title(markdown):
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No h1 header found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as file:
        markdown_content = file.read()
    with open(template_path, 'r') as file:
        template_content = file.read()

    html_content = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)
    full_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, 'w') as file:
        file.write(full_html)



if __name__ == "__main__":
    main()