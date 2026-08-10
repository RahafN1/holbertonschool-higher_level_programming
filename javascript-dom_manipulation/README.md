# JavaScript - DOM Manipulation

## Description
This project is an introduction to manipulating the DOM (Document Object
Model) using JavaScript. The DOM is the structured, tree-like representation
of an HTML document that browsers build when they load a page — it lets
JavaScript find, read, and change what's on the screen without reloading it.

In this project, we focus on:
- Selecting HTML elements with `document.querySelector` /
  `document.querySelectorAll`
- Modifying element styles and content directly through JavaScript
- Adding, removing, and toggling CSS classes
- Listening and binding to DOM and user events (clicks, etc.)
- Making network requests with `XMLHttpRequest` and the `Fetch` API to load
  and display data dynamically

The main goal of this project is to understand how the DOM works and how
JavaScript can be used to make a web page interactive without ever
refreshing the browser.

## Installation
Clone the repository:
```
git clone https://github.com/<your-username>/holbertonschool-higher_level_programming.git
```
Move into the project directory:
```
cd holbertonschool-higher_level_programming/javascript-dom_manipulation
```
Open any of the `*-main.html` files directly in Chrome (version 57.0 or
later) to run the corresponding script, or serve the folder with a simple
local server, e.g.:
```
python3 -m http.server
```

## Requirements
- All files are interpreted/tested in the Chrome browser (version 57.0 or
  later)
- All files should end with a new line
- Code must be `semistandard` compliant
- `var` is not allowed — use `let` / `const`
- The HTML should never reload for any action: DOM manipulation, updating
  values, fetching data, etc.
- A `README.md` file at the root of the project is mandatory

## Examples
```javascript
// Select an element and change its style
document.querySelector('header').style.color = '#FF0000';
```

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header>
      First HTML page
    </header>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="0-script.js"></script>
  </body>
</html>
```

## Testing
Each task comes with its own `N-main.html` file. To test a script:
1. Make sure the `N-script.js` file is saved in the same directory as its
   matching `N-main.html`.
2. Open the `N-main.html` file in Chrome.
3. Check the browser console (DevTools) for errors and confirm the expected
   visual/behavioral change on the page.

## Files
| File | Description |
| --- | --- |
| `0-script.js` | Updates the text color of the `header` element to red |
| `1-script.js` | Adds a click event that turns the header text red |
| `2-script.js` | Adds the `red` class to the header on click |
| `3-script.js` | Toggles the `red` class on the header on click |
| `4-script.js` | Lists all elements with the `red` class |
| `5-script.js` | Changes the text of the header on click |
| `6-*` | Fetches and displays a Star Wars character's name |
| `7-*` | Fetches and lists all Star Wars movie titles |
| `8-*` | Displays "Hello" after a request completes |
| `9-*` | Advanced: list, add, and remove items dynamically |
| `10-*` | Advanced: says hello to everybody based on user input |

## Author
Rahaf alabdalh 
