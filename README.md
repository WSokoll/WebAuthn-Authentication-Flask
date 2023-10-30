# WebAuthn-Authentication-Flask

## Overview
This Flask project serves as a WebAuthn (Web Authentication) demo with Flask-Security-Too library. 
WebAuthn is a modern, passwordless authentication method that enhances security and user experience.
It enables registering and using a security key or the operating system's password as a second factor authentication method.

## Project setup

### Installing dependencies

```
pip install -r .\app\requirements.txt
```

### Configuration
In the `.\local` folder, create a file called `config.local.py`. 
Then copy the contents of the `.\app\config.default.py` file and change the values if needed.

### Database setup
This project uses MySQL database, which can be initiated with the script from the `db/init.sql` file.