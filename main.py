import yaml
from pathlib import Path

def define_env(env):

    def load_tips(theme):

        folder = Path(f"data/{theme}")

        if not folder.exists():
            return []

        all_tips = []

        for file in sorted(folder.glob("*.yml")):

            data = yaml.safe_load(file.read_text(encoding="utf-8"))

            if data:
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

            if data:
                all_resources.append(data)

        return all_resources


    def get_resource_themes():

        folder = Path("datas")

        if not folder.exists():
            return []

        return sorted(
            directory.name
            for directory in folder.iterdir()
            if directory.is_dir()
        )

    def get_tip_themes():

        folder = Path("data")

        if not folder.exists():
            return []

        return sorted(
            directory.name
            for directory in folder.iterdir()
            if directory.is_dir()
        )


    env.variables["resources"] = load_resources
    env.variables["resource_themes"] = get_resource_themes
    env.variables["tip_themes"] = get_tip_themes
    env.variables["tips"] = load_tips