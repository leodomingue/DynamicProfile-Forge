#Libraries
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import os
import requests
import yaml
from dotenv import load_dotenv

from extra_functions import split_projects
from projects_parser import parse_project

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json",
}


# Read Projects from Notion
url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

response = requests.post(url, headers=headers, json={})
response.raise_for_status()

data = response.json()
projects = [parse_project(p) for p in data["results"]]
projects_split = split_projects(projects)


# Read additional data from YAML
with open("data_mock.yaml", "r", encoding="utf-8") as f:
    context = yaml.safe_load(f)

context["projects"] = projects_split

#Render Readme
env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("real_template.md.j2")
output = template.render(**context)


Path("Mock_README.md").write_text(output, encoding="utf-8")