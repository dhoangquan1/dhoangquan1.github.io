from jinja2 import Environment, FileSystemLoader
import os

# Set up the Jinja2 environment
env = Environment(loader=FileSystemLoader("templates"))

pages = [
    {"template": "index.html", "output": "index.html"}
]

output_dir = "./"
os.makedirs(output_dir, exist_ok=True)

for page in pages:
    template = env.get_template(page["template"])
    rendered = template.render()
    output_path = os.path.join(output_dir, page["output"])
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(rendered)
    print(f"Rendered: {output_path}")
    
