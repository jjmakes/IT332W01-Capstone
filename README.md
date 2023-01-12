# Getting Started

Place the contents of this folder into the directory you intend to backup.

Install dependencies:

```
pip install -r requirements.txt
```

# AWS Credentials

[Refer to AWS documentation for generating credentials.](https://docs.aws.amazon.com/keyspaces/latest/devguide/access.credentials.html)

[Make sure to add the proper permissions to the IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html)

The user will need `AmazonS3FullAccess` permissions to create and upload to the bucket.

Create a .env file at the project's root, and store the credentials as follows:

```
AWS_ACCESS_KEY_ID=<YOUR_ACCESS_KEY_ID>
AWS_SECRET_ACCESS_KEY=<YOUR_SECRET_ACCESS_KEY>
```

**DO NOT SHARE THESE CREDENTIALS WITH ANYONE**

# Backup

To run a manual backup, use command:

```
python3 -B main.py
```

# Scheduled Backups

Once it's confirmed that the script is working, you can configure your machine to run it on a schedule.

### Ubuntu (cron)

Add the following via `crontab -e`, replacing `path/to/script.py` with the path to `main.py`

```
* * * * * /usr/bin/python3 /path/to/script.py
```
