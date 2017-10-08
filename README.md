# HebbenZeHetAlGedaan.nl
Een website waar men kan controleren of mensen het al hebben gedaan.

## Installeren van de server
1. Installeer Django.
2. Migreer de database:
  ```
  > python manage.py makemigrations
  > python manage.py check
  > python manage.py migrate
  ```
3. Run de server:
  ```
  > python manage.py runserver
  ```
4. Geniet van localhost access.

## Migreren van de database
Het migreren van de database moet opnieuw gebeuren wanneer er een verandering is in het datamodel.
In andere woorden, wanneer er in de model classes een property is veranderd, toegevoegd of verwijderd.
