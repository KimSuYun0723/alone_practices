# alone_practice
- Any codes
- Mostly for individual practicing

# Main
- Completed folders

# Master
- Still practicing
  - HTML / CSS
  - Back-end Studying _ python DRF
  - Statistics _ python $ R
  - Data Analysis _ python & R
  - Crawling _ python
  - ML _ python
- Including completed folders

----------------------------------------------
# Connecting local - repository
- (approach into local directory)
- git init
- (create repository)
- git remote add origin [repository address]
- git remote -v   #confirm
- git add .
  - or : git add [directory name]
- git commit -m "[commti message]"
- git push origin main/[branch]

# Delete Directory
- git rm --cached -r [directory name] -> commit -> push
-   or : using .gitignore

----------------------------------------------
https://mylko72.gitbooks.io/git/content/
# Branch Manage
- git branch   #confirm registered branch
- git branch -v   #to wathch detaily
- git branch --merged   #merged branch list
- git branch --no-merged   #not merged branch list

# Create git branch
- git branch [branch name]   #create
- git checkout [branch name]   #move
- git checkout -b [branch name]   #perform above 2 lines together
- git branch -m [branch name] [new branch name]   #change branch name


# Git branch delete
- git checkout [another branch]
- git branch -d [branch name]
- git branch -D [branch name]   #forced
  - in the cases of not pushed commit 
  - in the cases of changes not merged into branch
