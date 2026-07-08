# Second Style - README

Instructions to install requirements and set environment variables for Flask.

1. Create and activate a virtual environment (optional but recommended):

	 - macOS / Linux:
		 ```bash
		 python3 -m venv venv
		 source venv/bin/activate
		 ```

	 - Windows (PowerShell):
		 ```powershell
		 python -m venv venv
		 .\venv\Scripts\Activate.ps1
		 ```

2. Install requirements:

	 ```bash
	 pip install -r requirements.txt
	 ```

3. Configure Flask environment variables:

	 - macOS / Linux:
		 ```bash
		 export FLASK_APP=app.py
		 export FLASK_ENV=development
		 export FLASK_DEBUG=1
		 ```

	 - Windows (PowerShell):
		 ```powershell
		 $env:FLASK_APP = "app.py"
		 $env:FLASK_ENV = "development"
		 $env:FLASK_DEBUG = "1"
		 ```

4. Run the app:

	 ```bash
	 flask run
	 ```

That's it.
