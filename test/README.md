Go to https://github.com/praup02/test-automation.
Copy the git url from Code.

Create a working directory in your machine.
Execute the command to clone "https://github.com/praup02/test-automation.git"
You should be able to see the directory structure test-automation\DistaCartTestAutomation.

-> Steps to pull the latest code from git:
git pull

-> Steps to create scratch branch:
git checkout -b scratch/newtest

-> Steps to add modified or new files to commit:
git add <file>

-> Steps to add commit message:
git commit -m "commit message"

-> Steps to push your working scratch branch to server:
git push -u origin scratch/newtest

-> Create a pull request in github and assign the reviewers.
Reviewers will review the pull request and approve or provide comments on the PR.
PR Approved -> Merge to master.
PR commented -> Incorporate the comments and then raise a new pull request.

-> One PR is merged, delete the branch from local and github.
git branch -D scratch/newtest

