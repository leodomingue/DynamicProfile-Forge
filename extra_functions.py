def progress_color(progress: int) -> str:
    if progress < 25:
        return "red"
    elif progress <= 50:
        return "orange"
    elif progress <= 75:
        return "yellow"
    return "brightgreen"


def progress_badge_url(progress: int) -> str:
    color = progress_color(progress)
    return f"https://img.shields.io/badge/progreso-{progress}%25-{color}"

def normalize_project(project: dict) -> dict:
    # Principal Function to divide projects
    project = project.copy()

    # Build GitHub-related URLs
    owner_repo = project["github"]["owner"]
    repo_githubname = project["github"]["repo"]
    project["repo_url"] = f"https://github.com/{owner_repo}/{repo_githubname}"
    project["stars_badge_url"] = (f"https://img.shields.io/github/stars/{owner_repo}/{repo_githubname}?style=social")


    #Logic to divide projects in "Special/in_progress/finished"
    # Handle Special Category: These projects are infinite progress
    if project["category"] == "special":
        project["progress_badge_url"] = "https://img.shields.io/badge/progreso-∞-blue"

        return project


    # Handle Standard Projects: Check if they are still in progress or completed
    elif project["category"] == "in_progress":
        progress = project.get("progress", 0)

        #Return a finished project
        if progress >= 100:
            project["category"] = "finished"
            return project
        
        #If progress < 100
        project["progress_badge_url"] = progress_badge_url(progress)

    return project


def split_projects(projects: list) -> dict:
    #Groups projects into categories for template rendering
    result = {
        "in_progress": [],
        "finished": [],
        "special": []
    }

    for project in projects:
        normalized_project = normalize_project(project)
        result[normalized_project["category"]].append(normalized_project)

    return result

