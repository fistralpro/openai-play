# Various OpenAI model sandbox

Python library https://docs.python.org/3/library/  
## Setup
Install python3 pip venv
Create venv and install requirements
```bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

Rename example environment variables file:
```bash
cp .env.example .env
```

Update your .env file with the [API key](https://beta.openai.com/account/api-keys)   
Run the app:
```bash
flask run
```

You should now be able to access the app at [http://localhost:5555](http://localhost:5555)! For the full context behind this example app, check out the [tutorial](https://beta.openai.com/docs/quickstart).
