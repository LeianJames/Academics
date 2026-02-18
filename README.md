# Academics
My academic projects

If you create a new Python file and want to add it to your GitHub repository, you need to stage, commit, and push it just like any other change.

1. git status --> Git will show your new untracked file under: Untracked files: newfile.py
2. git add newfile.py
3. Or to add all new and modified files at once: git add .
4. git commit -m "Add new Python file"
5. git push

git add . only stages files that have changes (new, modified, or deleted).
It does not “touch” unchanged files.

To import a defined function in another directory -- > from Functions.Modules import operations
