import yaml
from pathlib import Path

def define_env(env):

    def load_tips(theme):

        folder = Path(f"data/tips/{theme}")

        if not folder.exists():
            return []

        all_tips = []

        for file in sorted(folder.glob("*.yml")):

            data = yaml.safe_load(file.read_text(encoding="utf-8"))

            if data:
                all_tips.append(data)

        return all_tips

    def load_resources():

        folder = Path(f"data/resources")

        if not folder.exists():
            return []

        all_resources = []

        for file in sorted(folder.glob("*.yml")):
            data = yaml.safe_load(
                file.read_text(encoding="utf-8")
            )

            if data:
                all_resources.append(data)

        return all_resources


    def get_resource_themes():

        folder = Path("data/resources")

        if not folder.exists():
            return []

        return sorted(
            directory.name
            for directory in folder.iterdir()
            if directory.is_dir()
        )


    env.variables["resources"] = load_resources
    env.variables["resource_themes"] = get_resource_themes
    env.variables["tips"] = load_tips