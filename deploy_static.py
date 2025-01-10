import shutil
from jinja2 import Environment, FileSystemLoader
import os

# Set up the Jinja2 environment
env = Environment(loader=FileSystemLoader("templates"))

pages = [
    {"template": "base.html", "output": "base.html"},
    {"template": "index.html", "output": "index.html"}
]

output_dir = "docs"
os.makedirs(output_dir, exist_ok=True)

for page in pages:
    template = env.get_template(page["template"])
    rendered = template.render()
    output_path = os.path.join(output_dir, page["output"])
    with open(output_path, "w") as f:
        f.write(rendered)
    print(f"Rendered: {output_path}")
    
shutil.copytree('static', os.path.join(output_dir, 'static'))
