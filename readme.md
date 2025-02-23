
Django app


Custom API Key Authentication:
You're requiring the client to include a specific header (like X-API-PASSWORD or X-MY-API-KEY) with a pre-shared secret value. The server then checks this value to decide if the request is authorized.

ssh-keygen -t rsa -b 4096 -C "rinubronic@gmail.com"
Get-ChildItem ~/.ssh
Get-Content ~/.ssh/id_rsa.pub
Go to GitHub → Settings → SSH and GPG keys.
Click New SSH Key.
Title: Give it a name (e.g., "My Laptop SSH Key").
Key: Paste the copied key.
Click Add SSH Key.
ssh -T git@github.com

git init
git add .
git commit -m "Initial commit - Django project"
git remote set-url origin git@github.com:your-username/django_project.git
git remote -v
git config --global user.name "Rinu B"
git config --global user.email "rinubronic@gmail.com"
git config --global --list
git push -u origin master
git branch -m feature/dev
git branch
git add .
git status
git commit -m "Initial commit - Django Backend Project"...
git push origin feature/dev


