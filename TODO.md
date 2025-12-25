# --- OPTION A: GET UPDATES (Pull) ---
# Use this to update your local computer with changes from the server.
git pull origin main

# --- OPTION B: SEND UPDATES (Push) ---
# Use this to save your local changes to the server.

# 1. Check modified files
git status

# 2. Stage all changes
git add .

# 3. Commit with a message
git commit -m "Update: Describe your changes"

# 4. Push to remote
git push origin main
