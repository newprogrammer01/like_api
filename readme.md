The like and dislike

# Setup environment

## Create virtual environment

```bash
python3 -m venv venv
```

## Activate virtual environment

```bash
source venv/bin/activate
```

## Install requirements

```bash
pip install -r requirements.txt
```

## Git ignore

```bash
echo "venv" >> .gitignore
```

# Set environment variables

## Telegram bot token

```bash
export TOKEN="your token"
```

# Database structure

## User table

| type | name | description |
|------|------|-------------|
| int  | userid | user id |
| int  | imageid | image id |
| int  | like | like |
| int  | dislike | dislike |

## Image table

| type | name | description |
|------|------|-------------|
| int  | imageid | image id |
| char| url | image url |

## Endpoints

[endpoints](endpoints.md)