def parse_project(projects_data: dict) -> dict:
    project = projects_data["properties"]

    info = {
        "name": project["Name Project"]["title"][0]["plain_text"],
        "description": project["Description"]["rich_text"][0]["plain_text"],
        "category": project["Category"]["select"]["name"],
        "progress": project["Progress"]["number"],
        "status": project["Status"]["select"]["name"] if project["Status"]["select"] else "Sin estado",
        "github": {
            "owner": project["GitHub Owner"]["rich_text"][0]["plain_text"],
            "repo": project["GitHub Repo Name"]["rich_text"][0]["plain_text"]
        },
        "stack": [tech["name"] for tech in project["Stack"]["multi_select"]],
    }
    return info