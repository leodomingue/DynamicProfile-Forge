from jinja2 import Environment, FileSystemLoader
import yaml
from pathlib import Path
from extra_functions import split_projects

with open("data_mock.yaml", "r", encoding="utf-8") as f:
    data_mock = yaml.safe_load(f)

data_mock["projects"] = split_projects(data_mock["projects"])
env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("real_template.md.j2")
output = template.render(**data_mock)


Path("Mock_README.md").write_text(output, encoding="utf-8")