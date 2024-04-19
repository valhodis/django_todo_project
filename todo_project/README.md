**_ToDo App_**

**DESCRIERE**

ToDo App este o aplicație web simplă pentru gestionarea sarcinilor și a listelor de sarcini. 
Această aplicație permite utilizatorilor să creeze, să actualizeze, să completeze și să șteargă sarcini, 
oferindu-le o modalitate simplă și eficientă de a-și organiza activitățile de zi cu zi.

**CARACTERISTICI**

* Adăugarea, actualizarea și ștergerea de sarcini
* Marcarea sarcinilor ca completate
* Vizualizarea listei de sarcini active și a celor completate
* Autentificare utilizator pentru a asigura confidențialitatea și securitatea datelor

**TEHNOLOGII UTILIZATE**

* Python și Django pentru dezvoltarea backend-ului
* HTML, CSS pentru dezvoltarea frontend-ului
* Django's authentication pentru gestionarea autentificării utilizatorilor

**STRUCTURA PROIECTULUI**

1. [ ] todo_project/
2. [ ] │
3. [ ] ├── aplicatie/
4. [ ] │ ├── migrations/
5. [ ] │ │ └── (Fișierele de migrație)
6. [ ] │ ├── templates/
7. [ ] │ │ ├── aplicatie/
8. [ ] │ │ │ ├── add_task.html
9. [ ] │ │ │ ├── completed_tasks.html
10. [ ] │ │ │ ├── delete_task.html
11. [ ] │ │ │ ├── task_detail.html
12. [ ] │ │ │ └── task_list.html
13. [ ] │ │ └── registration/
14. [ ] │ │ ├── login.html
15. [ ] │ │ └── register.html
16. [ ] │ ├── forms.py
17. [ ] │ ├── models.py
18. [ ] │ ├── tests.py
19. [ ] │ ├── urls.py
20. [ ] │ └── views.py
21. [ ] │
22. [ ] ├── todo_project/
23. [ ] │ ├── init.py
24. [ ] │ ├── asgi.py
25. [ ] │ ├── settings.py
26. [ ] │ ├── urls.py
27. [ ] │ └── wsgi.py
28. [ ] │
29. [ ] ├── db.sqlite3
30. [ ] ├── manage.py
31. [ ] ├── README.md
32. [ ] └── requirements.txt

**INSTRUCTIUNI DE INSTALARE**

1. Clonează sau descarcă proiectul de pe repository-ul GitHub.

2. Asigură-te că ai Python și Django instalate pe sistemul tău. Dacă nu le ai deja, 
le poți instala folosind Python.org și Django.

3. În folderul proiectului creează un virtual environment cu următoarele comenzi folosind 
   terminalul:

> python -m venv nume_mediu_virtual

4. Activează virtual environment creat cu comanda:

MacOS:

> source nume_mediu_virtual/bin/activate

Windows:

> nume_mediu_virtual\Scripts\activate

5. Instalează dependențele proiectului folosind comanda:

> pip install -r requirements.txt

6. Aplică migrările pentru a inițializa baza de date:

> python manage.py migrate

7. Creează un SuperUser pentru a avea acces la interfața de administrare și pentru a adăuga și gestiona intrările:

> python manage.py createsuperuser

odată rulată comanda de mai sus trebuie să urmezi pașii care apar în terminal.

> username - yourname
> 
> email - your@email.com
> 
> password - ******** (ATENTIE!!! caracterele scrise nu apar)

8. Rulează serverul de dezvoltare folosind:

> python manage.py runserver

9. Accesează aplicația într-un browser(Chrome, Safari, Opera) folosind adresa:

> http://localhost:8000

sau

> http://127.0.0.1:8000

**CONTRIBUTII**

Contribuții sunt binevenite!

**AUTOR**

_Val H._ 