# App Store Database Project

## Summary
Creating a sample database and solving various queries for an app store application in PostgreSQL.  

## Creators
The queries for creating the database can be found in the `creators/` directory.

## Populators
To load the sample data for testing the queries, use the file in the `populators/` directory. (Generators generate the populators)

## GUI App (Bonus)
It’s possible to test the database with the GUI app too. The app is inside the `app/` directory and can be run with the following command:

```
python3 database.py
```

Dependencies `psycopg2` and `tkinter` are needed. To run them, you have to download them based on your OS. You can use `brew` on macOS.

## Sample Queries:
1. Name of newest apps added to the store
2. List of apps downloaded by a user
3. All comments from a user across different apps and games
4. List of apps published by a developer
5. Total income of a developer
6. Users who have downloaded a specific app in the last week
7. Users who have paid for an app or game
8. List of latest comments on a package
9. Users search for ‘Jack’
10. List of lowest rated apps and games
11. Developer’s income in the last month
12. Users who have not updated ‘Telegram’ for at least a year
13. Search for game ‘Clash of’
14. Users who have made most in-app payments on “Clash Of Clans”
15. Comments for a specific game
16. Edit a comment
17. List of apps and games with most rated reviews
18. List of developers using gmail
19. Number of apps in each category

## Triggers:
- Check game name does not contain the word ‘blood’
- Make sure payment prices are not negative

## ER Diagram
![er_diagram-1](https://github.com/dalisyron/PostgreAppStore/assets/34644374/21943f00-7af1-49ae-9af3-d88adaa1bbd5)
