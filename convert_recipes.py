import os
from datetime import datetime

def convert_recipes():
    """Converts recipe files to Jekyll posts."""
    # List of files that are not recipes
    not_recipes = [
        "README.md",
        "LICENSE",
        "convert_recipes.py",
        "_config.yml",
        "Gemfile",
        "Gemfile.lock",
    ]

    # Get a list of all files in the root directory
    files = [f for f in os.listdir('.') if os.path.isfile(f)]

    # Filter out non-recipe files
    recipe_files = [f for f in files if f not in not_recipes and not f.endswith(".md")]

    # Create the _posts directory if it doesn't exist
    if not os.path.exists("_posts"):
        os.makedirs("_posts")

    # Get the current date for the post filenames
    current_date = datetime.now().strftime("%Y-%m-%d")

    # Process each recipe file
    for recipe_file in recipe_files:
        with open(recipe_file, "r") as f:
            content = f.read()

        # Create the title from the filename
        title = recipe_file.replace("_", " ").replace("-", " ").title()

        # Create the markdown content
        markdown_content = f"""---
layout: post
title:  "{title}"
---

{content}
"""

        # Create the new filename
        new_filename = f"{current_date}-{recipe_file.lower().replace(' ', '-')}.md"

        # Write the new markdown file to the _posts directory
        with open(os.path.join("_posts", new_filename), "w") as f:
            f.write(markdown_content)

        print(f"Converted {recipe_file} to {new_filename}")

if __name__ == "__main__":
    convert_recipes()