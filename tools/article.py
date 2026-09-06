#!/bin/python
# ----------------------------------------------------------------------------------
# brief : Create an article and pre-complete the TOML file !
#
# author : l.heywang
# date : 05/09/2026
# ----------------------------------------------------------------------------------

from pathlib import Path
import datetime
import os


def init_toml(file: Path, data: dict):

    # We just write to the file "manually" to keep the format :
    with open(file, "w+") as f:
        f.write(f'title = "{data.get("title", "Write your title here !")}"\n')
        f.write(
            f'slug = "{data.get("slug", "Write the file slug here (path from src/content/docs/)")}"\n'
        )
        f.write(f'date = "{datetime.datetime.now().strftime("%Y-%m-%d")}"\n\n')

        f.write("[author]\n")
        f.write(f'pseudo = "{data.get("author", "Add your pseudo here !")}"\n')
        f.write(f'name = "{data.get("name", "Add your name here !")}"\n')
        f.write(f'role = "{data.get("role", "Add your role here !")}"\n')
        f.write(f'avatar = "/avatars/{data.get("author", "author").lower()}.png"\n\n')

        f.write("[metadata]\n")
        f.write(f'title_keyword = "{data.get("title", "Add your main keyword !")}"\n')
        f.write("aux_keywords = [ Add your article keywords here ]\n")
        f.write("misc_keywords = [ Add your generic keywords here ]\n")


def init_mdx(file: Path, data: dict):

    # We just write the standard header
    with open(file, "w+") as f:
        f.write("---\n")
        f.write(f"title: {data.get("title", "Write your title here !")}\n")
        f.write("---\n\n")

        f.write('import ArticleHeader from "../../../components/header.astro";\n')
        f.write('import HardwareModule from "../../../components/module.astro";\n')
        f.write('import Step from "../../../components/step.astro";\n')

        f.write('import { Tabs, TabItem } from "@astrojs/starlight/components";\n')
        f.write('import { Card, CardGrid } from "@astrojs/starlight/components";\n\n')

        f.write(
            f'<ArticleHeader tomlPath="{data.get("slug", "Write the file slug here (path from src/content/docs/)")}.toml" />\n\n'
        )

        f.write('<p class="article-lead">\n\tWrite here your recap !\n</p>\n\n')


def create_files(base: Path, data: dict):

    # First, build the paths
    toml = base / Path(data.get("target", "unknown") + ".toml")
    mdx = base / Path(data.get("target", "unknown") + ".mdx")

    # Create the parents
    base.mkdir(parents=True, exist_ok=True)

    # Init the files
    init_mdx(mdx, data)
    init_toml(toml, data)


def main():
    """
    Fetch the required data in the console, and update :
    """

    # First, verify that the current path is correct
    if Path(__file__).parent.parent != Path(os.getcwd()):
        print("This script MUST be launched from the root repo")
        exit(-1)

    # Now, collect the required data :
    # - title
    # - path
    # - author
    # - name
    # - role

    data = dict()
    data["title"] = input("Enter the title : ")
    data["title"] = data["title"].lower().replace(" ", "-").capitalize()

    type = input(
        "Enter the type [tutorials, article, commu] starting from : src/content/docs/"
    )
    target = input(f"Enter the file name : src/content/docs/{type}/{data['title']}/")
    data["author"] = input("Enter the author : ")
    data["name"] = input("Enter the name : ")
    data["role"] = input("Enter the role : ")

    # Build the slug
    data["slug"] = f"{type}/{data['title']}/{target}"

    # Build the full path
    data["path"] = Path(f"src/content/docs/{type}/{data['title']}/{target}")
    data["target"] = target

    # Root path
    base = Path(f"src/content/docs/{type}/{data['title']}")

    # Create the files
    create_files(base, data)

    # End
    print("Done !")


if __name__ == "__main__":
    main()
