<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="/static/styles.css" />
</head>
<body>
<h1>Things to bring to our picnic</h1>
<table>
<tr><th>Item</th><th>Quantity</th></tr>
%for row in rows:
    <tr>
    %for col in row:
        <td>{{col}}</td>
    %end
    </tr>
%end
</table>
</body>
</html>
