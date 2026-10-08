import yaml
from pathlib import Path

def define_env(env):

    def load_tips(theme=None):

        if theme: 
            folder = Path(f"data/{theme}")
        else: 
            folder = Path(f"data")

        if not folder.exists():
            return []

        all_tips = []

        for file in sorted(folder.rglob("*.yml")):
            data = yaml.safe_load(
                file.read_text(encoding="utf-8")
            )

            if data and data.get("type") == "tip":
                all_tips.append(data)

        return all_tips

    def load_resources(theme=None):

        if theme: 
            folder = Path(f"data/{theme}")
        else:     
            folder = Path(f"data")

        if not folder.exists():
            return []

        all_resources = []

        for file in sorted(folder.rglob("*.yml")):
            data = yaml.safe_load(
                file.read_text(encoding="utf-8")
            )

            if data and data.get("type") == "resource":
                all_resources.append(data)

        return all_resources


    def get_themes():

        folder = Path("data")

        if not folder.exists():
            return []

        return sorted(
            directory.name
            for directory in folder.iterdir()
            if directory.is_dir()
        )

    env.variables["resources"] = load_resources
    env.variables["themes"] = get_themes
    env.variables["tips"] = load_tips