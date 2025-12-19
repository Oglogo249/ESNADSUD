<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Page 1 - Forms</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<h2>Registration Form</h2>
<form>
    <label>Full Name:</label>
    <input type="text"><br>

    <label>Email:</label>
    <input type="email"><br>

    <label>Username:</label>
    <input type="text"><br>

    <label>Password:</label>
    <input type="password"><br>

    <label>Phone:</label>
    <input type="tel"><br>
</form>

<hr>

<h2>Login Form</h2>
<form>
    <label>Username:</label>
    <input type="text"><br>

    <label>Password:</label>
    <input type="password"><br>
</form>

<br>
<a href="page2.html">Go to Page 2</a>

</body>
</html>



<DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Page 2 - HTML Info</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<header>
    <nav>
        <a href="index.html">Home</a> |
        <a href="#">About</a> |
        <a href="#">Contact</a>
    </nav>
</header>

<h2>HTML Versions</h2>
<ul>
    <li>HTML 1.0</li>
    <li>HTML 2.0</li>
    <li>HTML 3.2</li>
    <li>HTML 4.01</li>
    <li>XHTML</li>
    <li>HTML5</li>
</ul>

<h2>Semantic vs Non-Semantic Elements</h2>
<table border="1">
    <tr>
        <th>Semantic Elements</th>
        <th>Non-Semantic Elements</th>
    </tr>
    <tr>
        <td>&lt;header&gt;</td>
        <td>&lt;div&gt;</td>
    </tr>
    <tr>
        <td>&lt;nav&gt;</td>
        <td>&lt;span&gt;</td>
    </tr>
    <tr>
        <td>&lt;article&gt;</td>
        <td>&lt;b&gt;</td>
    </tr>
</table>

<h2>Image</h2>
<img src="media/html.png" width="300">

<h2>Video</h2>
<video width="400" controls>
    <source src="media/intro.mp4" type="video/mp4">
</video>

</body>
</html>
