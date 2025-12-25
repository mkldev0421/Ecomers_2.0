# 1. Check which files have been modified
git status

# 2. Stage the files you want to update
# You can add a specific file:
git add filename.py
# OR add all changed files at once:
git add .

# 3. Commit the changes with a descriptive message
git commit -m "Update: Fixed bug in login logic"

# 4. Push the changes to the remote repository
# Note: 'main' is the branch name. It might be 'master' in older repos.
git push origin main
