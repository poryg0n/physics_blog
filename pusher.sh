#!/bin/bash

#git init
#git add -A
#git status
#git commit -m "Adding stuffs"
##git push main master
#git push -u master --all
#

#echo "Important! Needs at least one post to work" > README.md
git init
git add . -A
git commit -m "first commit"
git branch -M main
git remote remove origin
git remote add origin https://github.com/poryg0n/physics_blog.git
git push -fu origin main
