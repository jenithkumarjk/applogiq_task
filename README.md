1) Creation of virtual environments:

   python -m venv virtual

2) Activate the Virtual Environment:
   
   virtual\Scripts\activate

3) Install dependencies using pip:		

   pip install -r req.txt

4) Migrate Database:

   cd applogiq
   	
   py manage.py makemigrations

   py manage.py migrate


5) Start Jupyter Notebook with Django Shell:
   
   python manage.py shell_plus --lab --no-browser

6) Run Jupyter note name as "h17todata.ipynb"
   
7) Run Project:

   python manage.py runserver


   
   

