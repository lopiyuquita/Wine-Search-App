# Project Name: *Wine Search/ Finder Django App* #  


## Purpose  ##
There are technical and applicaiton purposess for this project as described below:  

**1. The technical purpose:**  
    • To demonstrate the mastery of the course objective of SI664 (DBMS)  
        - To learn the necessary skills for building and deploying database-backed websites:  

**(1) Database using MySQL:**  
            (a) Demonstrate the understanding and designing of data modeling.  The deliverable will be an EER (ERD) 
            model using MySQL Workbench. The completed model will address the three main requirements of the course
             final project:  
             - The minimum 7 tables  
             - Adherence to the normalization standards --Third Normal Form (3NF)
             - At least one Many-to-Many relationship in the database  
            (b) Manipulate data using SQL

**(2) App Development using Django:**  
    • To advance skills in Python and demonstrate the understanding of Django framework 
 mechanisms:  
    • Advance skills in Python by write Django ORM code  
        - The deliverable/requirements:  
            (1) GitHub repository (in progress)
            (2) Data model in .mwb file (in progress)
            (3) MySQL database:  
                (a) Data import script  
                (b) Database  
                (c) Database dump file  
            (4) Django app (MVP):  
                (a) Home/About page  
                (b) Login page (+Social Login)  
                (c) List page/ Detail pages  
                (d) Add/Update/Delete forms  
                (e) Filter form (basic list search)  
                (f) Navigation bar  
                (g) Bootstrap for styling  
            (5) Django REST API app:  
                (a) POST/ PUT/DELETE (one entity)  
                (b) Token Authentication  
                (c) Swagger Doc
                (d) CRUD minimum requirements:  
                    (i) REST API:  
                        • POST  
                        • PUT  
                        • DELETE    
                    (ii) Web Forms:  
                        • create()  
                        • modify()  
                        • delete()  
                                                                   
**2. The application purpose)**  
    • To develop a webapp which allows users to run general/ starting-point search to find wines that 
    may be be of their interests.  
    • To that end, the intended users of this app will be people who are not familiar with wines, who are not
     looking for specific labels.  
        - To meet this purpose, the app should allow the users to search based on taste notes -(e.g.) "fruity", "bold", 
        "spicy', etc.
        - Also, the app should return query results for the wines grouped by red, white, rose, sparkling, etc.
        
## Data set
(1) The original dataset is obtained at Kaggle's wine review data as a csv file:
•	Wine Reviews (130k-version2 wine reviews with variety, location, winery, price, 
and description): <https://www.kaggle.com/zynicide/wine-reviews>  

(2) There are three files on this Kaggle page (two csv files and one json file).  
I will use winemag-data-130k-v2.csv  

(4) Many-to-Many relationships:  
    •	There will be more than one Many-to-Many relationships in the database.  
        - wine tasters and wine information  See the [data model the actual model file will be added later](https://github.com/lopiyuquita/si664finalproject)
        - Ohter many-to-many relationshps exist:
            * An example of such is “varieties” and “region_1” tables


## Data model
(1) [Wine Review Datamodel -the actual model file will be added later](https://github.com/lopiyuquita/si664finalproject)  

As of December 4, 2018:  
![alt text](https://github.com/lopiyuquita/si664finalproject/blob/master/winesearch/static/si664finalprojectdatamodelDec4-1311.png)

## Package Dependencies (Not finalized as of November 30, 2018)
certifi==2018.10.15  
chardet==3.0.4  
coreapi==2.3.3  
coreschema==0.0.4  
defusedxml==0.5.0  
Django==2.1.2  
django-allauth==0.38.0  
django-cors-headers==2.4.0  
django-crispy-forms==1.7.2  
django-filter==2.0.0  
django-rest-auth==0.9.3  
django-rest-swagger==2.2.0  
django-test-without-migrations==0.6  
djangorestframework==3.9.0  
idna==2.7  
itypes==1.1.0  
Jinja2==2.10  
MarkupSafe==1.1.0  
mysqlclient==1.3.13  
oauthlib==2.1.0  
openapi-codec==1.3.2  
PyJWT==1.6.4  
python3-openid==3.1.0  
pytz==2018.5  
PyYAML==3.13  
requests==2.20.0  
requests-oauthlib==1.0.0  
simplejson==3.16.0  
six==1.11.0  
social-auth-app-django==3.1.0  
social-auth-core==2.0.0  
uritemplate==3.0.0  
urllib3==1.24.1  
virtualenv==16.0.0  


