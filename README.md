# Homework for lesson #5, python course spring 2020
**The goal**:
 * learn how to get things from internet without much efforts and hustle
 **המטרה**: ללמוד כיצד להשיג דברים מהאינטרנט בלי הרבה מאמצים והמולה.
 * get used to work with files in a simple way,
 להתרגל לעבוד עם קבצים בצורה פשוטה
 * probably, start using DB
 גם בן, ישנה אפשרות להתחיל לעבוד עם בסיסי נתונים
 
## 1. create a project
The idea is to create multiple files project somehow reflecting what's going on in the reality.
Separate functions/classes and a place, where you work with them

הרעיון הוא ליצור פרויקט  של כמה קבצים שמשקפים איכשהו את המתרחש במציאות. הפרד פונקציות /מחלקות ומקום, שבו אתם עובדים איתם
## 2. scrape initial data | גרדו נתונים ראשוניים
* **WHERE TO GET:** https://www.google.com
* **SEARCH PHRASE:** "python books" /you can get any other of your choice.
* **GOAL 1:** Get data from first 2 pages of google results, save to a file
* **GOAL 2:** from a results file, create a viewable HTML file
* **GOAL 3:** from a results file, for every url get a file content, save 
 
### 2.1. Get results from first 2 pages of google results, save to a file in a following format (CSV):

 | url | name | description | 
 | --- | ---- | ----------- |
 
### 2.2: Create a viewable HTML file
Create simple HTML file with results.
as a **Table**
```html
<table>
  <tr><td>index</td>
    <td><a href="url">page name</a></td>
    <td>description</td>
  </tr>
  <tr>...</tr>
</table> 
```
 | index | url and name | description | 
 | ----- | ------------ | ----------- |
 |   1. | <a href="https://medium.com/......  10 Amazing Python Books for Beginners & Professionals</a> | To get an in-depth understanding of Python, books are the best way to learn Python. Python is one of the famous programming languages. Also, it's used by ...|

or **numbered list**
```html
<ol>
    <li>#: <a href="url">page name</a>
       <br>description</li>
    <li> ... </li>
</ol>
```
 1. <a href="https://medium.com/@rinu.gour123/10-amazing-python-books-for-beginners-professionals-7ee5ee0334f4">10 Amazing Python Books for Beginners & Professionals</a>
  To get an in-depth understanding of Python, books are the best way to learn Python. Python is one of the famous programming languages. Also, it's used by ...
 1. ...
 
* 2.3. For every url get a file content, save to file
for every url in the results file  
 