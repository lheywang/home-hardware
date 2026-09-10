# ----------------------------------------------------------------------------------
# brief : Generate the index.json library to be used for the /home/bot services.
#
# author : l.heywang
# date : 05/09/2026
# ----------------------------------------------------------------------------------

# Imports
from pathlib import Path
from processor import process
from exporter import export
from resources import list_resources, list_links, list_errors


def fetch_ressources(folderName: str, basePath: Path) -> list[tuple[Path, Path]]:

    # Generate the root path
    searchPath = (basePath / Path(folderName)).resolve()

    # Search for files
    output: list[tuple[Path, Path]] = []

    for md_file in searchPath.rglob("*.mdx"):
        if md_file.name == "index.mdx":
            continue

        toml_file = md_file.with_suffix(".toml")
        if toml_file.is_file():
            output.append((md_file, toml_file))

    return output


if __name__ == "__main__":

    # First, fetch all the files
    root = (Path(__file__) / Path("../../src/content/docs")).resolve()
    articles = fetch_ressources("articles", root)
    tutos = fetch_ressources("tutorials", root)
    blog = fetch_ressources("commu", root)

    # Now, we can start process them
    data = process([articles, tutos, blog])

    # We can export it
    output = (Path(__file__) / Path("../../public")).resolve() / Path("index.json")
    export(output, data)

    # Finally, build the ressources.json file to be fetched by the secondary command :
    output = (Path(__file__) / Path("../../public")).resolve() / Path(
        "resources/resources.json"
    )
    list_resources((Path(__file__) / Path("../../public/resources")).resolve(), output)

    output = (Path(__file__) / Path("../../public")).resolve() / Path(
        "resources/links.json"
    )
    list_links((Path(__file__) / Path("../../data/url")).resolve(), output)

    output = (Path(__file__) / Path("../../public")).resolve() / Path(
        "resources/errors.json"
    )
    list_errors((Path(__file__) / Path("../../data/errors")).resolve(), output)

    print("Done !")
