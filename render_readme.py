from jinja2 import Environment, FileSystemLoader
from pathlib import Path

data_mock = {
    "profile":{
        "fullname": "nombre cualquiera",
        "occupation": "Estudiante",
        "description": "Hago cosas",
        "username": "leodomingue",
        "additional_info": [
            {
                "social_media_name": "Linkedin",
                "url": "https://www.linkedin.com/in/leo-dominguez-a6a113222/"
            }
        ]
    },
    "actual_languages":[
        {
            "name": "Python",
            "badge_url": "https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"
        }
    ],
    "new_languages":[
        {
            "name": "Javascript",
            "badge_url": "https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E"
        }
    ],
    "projects":[
        {
            "name": "Python-Coding-Challenge",
            "description": "Retos randoms de internet",
            "category": "in_progress",
            "progress": 45,
            "status": "En desarrollo",
            "github": {
                "owner": "leodomingue",
                "repo": "Python-Coding-Challenges"
                },
            "stack": ["Python", "2"]
        },
        {
            "name": "Conway's Game of Life Pygame",
            "description": "Simulador de conway",
            "category": "finished",
            "progress": None,
            "status": None,
            "github": {
                "owner": "leodomingue",
                "repo": "Conway-s-Game-of-Life-Pygame"
                },
            "stack": ["Python", "2"]
        }
    ]
}

env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("real_template.md.j2")
output = template.render(**data_mock)


Path("Mock_README.md").write_text(output, encoding="utf-8")