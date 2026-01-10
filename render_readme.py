# Libraries
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import os
import requests
import yaml
from dotenv import load_dotenv

from extra_functions import split_projects
from projects_parser import parse_project


def load_config():
    #Load configuration from .env
    load_dotenv()

    return {
        "NOTION_TOKEN": os.getenv("NOTION_TOKEN"),
        "DATABASE_ID": os.getenv("NOTION_DATABASE_ID")
    }

def fetch_notion_projects(notion_token, database_id):
    #Get projects from Notion Database
    headers = {
        "Authorization": f"Bearer {notion_token}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
    }

    url = f"https://api.notion.com/v1/databases/{database_id}/query"

    response = requests.post(url, headers=headers, json={})
    response.raise_for_status()
    return response.json()

def process_projects(notion_data):
    #Parser and normalize each project
    projects = [parse_project(project) for project in notion_data["results"]]
    projects_split = split_projects(projects)

    return projects_split

def render_YAML(filepath="additional_info.yaml"):
    #Render YAML to get static info
    with open(filepath, "r", encoding="utf-8") as f:
        additional_info = yaml.safe_load(f)
    return additional_info

def render_template(template_directory, template_name, context, output_path):
    #Render template
    env = Environment(loader=FileSystemLoader(template_directory))
    template = env.get_template(template_name)
    output = template.render(**context)
    Path(output_path).write_text(output, encoding="utf-8")

def main():
    config = load_config()

    notion_data = fetch_notion_projects(
        config["NOTION_TOKEN"], 
        config["DATABASE_ID"]
    )

    projects = process_projects(notion_data)

    yaml_data = render_YAML()

    context = {**yaml_data, "projects": projects}

    render_template(
        template_directory="templates",
        template_name="real_template.md.j2",
        context=context,
        output_path="Mock_README.md"
    )



if __name__ == "__main__":
    main()