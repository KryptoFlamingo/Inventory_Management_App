# shop_inventory_project
** Project Description **
An INternal Point of Sale system for a restaurant.
Has 3 main user pages:
    one to be used by a server at a table of guests on a handheld system
    one for a manager to manage inventory (add, remove, update meals) and track finances
    a third to be the home page to select your user ID to route you to the next screen


** Tech/framework used **
    Python
    Flask
    Jinja2
    HTML / CSS
    PostgreSQL and the psycopg (POSTICO)



** Project setup *** 
Type the below into the integrated terminal
    pip3 install python-dot env
    pip3 install Flask
    flask run 
click on the link in the terminal https://127.0.0.1:5000/

when the page opens in the browser, open the developer tools, 
got to Network tab and ensure Disable Cache is selected 
and Has blocked cookies is selected

    

    ** IF DATABASE doesnt load or is empty **
            createdb restaurant_app
            psql -d restaurant_app -f db/restaurant_app.sql 
            Open Posico
            Go to local host
            Look for database with the same name as in step 1
            Open the database and check it has tables in it
            Open an table and check it has content
            Close Postico
            In the terminal type  Flask run
            Then in terminal type python3 console.py
    Operation complete



** AIM **
To gain experience with Python and Jinja2 by creating and app which would allow a company to manage inventory via a database.

The front-end is a clean, basic grid style design which has not had much design and UX consideration.
One of the few visual components is an indicator on the menu tab (intended for a server) which states and indicates by a traffic light colour system if stock is Running Low or at the Last one As well as it being removed from the server list if Out of Stock preventing further orders.

The key goal in this project was to gain experience of using CRUD methods (Create, Remove, Update, Delete).

Issue 1 detailed below is a major bug which needs resolved in future.




** Issues **
1)      Theres a bug related to stock count on the server tab. After 'Order One' is clicked    sometimes it removes entirely instead of going down one. I suspect its something to do with an update on the browser manager tab stock quantity not updating (synchronising with) into the POSTICO database value and thus if the manager tab is updated to 10 off the database only remembers 8 off and thus it removes after 8 off. However this a total guess and needs to be investigated to confirm the problem then fixed properly.
2)      Menu tab (for servers) only allows you to order one of each meal at a time (on-click)
3)      When the Order 1 has been clicked on the menu tab (for a server) it moves to the bottom of the list. The fact it moves makes it confusing for the user.
4)      Manager tab shows Meal ID at sales detail log: needs to show meal name not ID
5)      Manager tab, sales details log needs to be graphic and made valuable
6)      Home tab has no value currently - UX design needed to make useful. 



** Nect Actions **
1)      Fix the issues listed above
2)      Make Manager tab financial data visual using graphics and charts 
3)      Add a way to apply a discount
4)      Add a way to review prior to submission of order
5)      Add a way to add a note or alarm of an allergy
6)      Update UX and CSS
