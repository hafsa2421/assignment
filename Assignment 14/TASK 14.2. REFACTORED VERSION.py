
# Python code starts here:
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Generated HTML</title>
</head>
<body>
    <h1>This HTML file was generated using Python!</h1>
</body>
</html>
"""

try:
    with open("student_portal_generated.html", "w", encoding="utf-8") as file:
        file.write(html_code)
    print("HTML file created successfully!")
except Exception as e:
    print("An error occurred:", e)
