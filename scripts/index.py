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


def fetch_ressources(folderName: str, basePath: Path) -> list[tuple[Path, Path]]:

    # Generate the root path
    searchPath = (basePath / Path(folderName)).resolve()

    # Search for files
    md = searchPath.rglob("*.mdx")
    toml = searchPath.rglob("*.toml")

    output = []
    for mdfile, tomlfile in zip(toml, md):
        output.append((Path(tomlfile), Path(mdfile)))

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

    print("Done !")

