# Install

Create a .env file after clone the repository to set a DB_PASSWORD variable

```bash
git clone https://github.com/mullerfs/queshi-server.git
cd queshi-server
echo "DB_PASSWORD=<YOUR_PASSWORD_GOES_HERE>" > .env
```

Create an enviroment for python if you do not pretend to use Docker

```bash
python -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
```