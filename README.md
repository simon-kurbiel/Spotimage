# Intent

The Intent of this project is to be able to download the images of your favorite spotify artists based on your listening history. The project will allow you to download all different images sizes of an artist with their respective directory/folder.

## Set up

### With virtual environment

#### Create a virtual environment

```bash
python -m venv venv
```

Then activate it

```bash
source venv/bin/activate
```

#### Get dependencies

Install all the required dependencies. Only required ones are [requests](https://requests.readthedocs.io/en/latest/), [pydantic](https://docs.pydantic.dev/latest/), and [pydantic_settings](https://pypi.org/project/pydantic-settings/)

```bash
pip install -r requirements.txt
```

## Spotify devloper api Keys

To be able to use spotify api, you must create a devloper account, which is free of charge.
Navigate to [spotify devloper](https://developer.spotify.com/dashboard). Once logged in and agree to terms and services, you must create an app. You can give it any name you want. However, make sure that your redirect url is the same as the one you intend to use.

Once that is done, navigate to the settings of your app and simply copy and paste the client_id and client_secret to your environemnt variable.

## Environment variables.

```dosini
CLIENT_ID=
CLIENT_SECRET=
REDIRECT_URI=
```

For the REDIRECT_URL, it is common practice to set it to

```dosini
REDIRECT_URI=http://localhost:8888/callback
```

for development purposes.

## Run the app

```python
python main.py
```

You will be prompted to enter the code to grant access
Simply navigate to the link & grab everything that is after code= and paste it into the running program. Once you hit enter, all the images of your favorite artists will be upload to your "uploads" directory.
