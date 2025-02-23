



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



git remote set-url origin git@github.com:your-username/django_project.git

git remote -v


git push -u origin master




git remote set-url origin git@github.com:Rinub/Backend_application_Django.git