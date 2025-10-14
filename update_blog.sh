#!/bin/bash

# Convert new recipes
python3 convert_recipes.py

# Build the Jekyll site
bundle exec jekyll build