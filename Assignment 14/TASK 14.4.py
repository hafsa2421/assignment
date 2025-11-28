from flask import Flask, render_template_string, request # type: ignore
app = Flask(__name__)

# HTML + JS (Task #3) served directly by Flask
login_page = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Validation</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f3f3f3;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .login-box {
            background: white;
            padding: 25px;
            width: 300px;
            border-radius: 10px;
            box-shadow: 0px 0px 8px rgba(0,0,0,0.2);
        }

        .error {
            color: red;
            font-size: 14px;
            margin-top: 5px;
        }

        input {
            width: 100%;
            padding: 10px;
            margin-top: 8px;
            border-radius: 5px;
            border: 1px solid #aaa;
        }

        button {
            width: 100%;
            padding: 10px;
            margin-top: 15px;
            background: #0055a5;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        button:hover {
            background: #004080;
        }
    </style>
</head>
<body>

    <div class="login-box">
        <h2>Login Form</h2>

        <form id="loginForm" method="POST" action="/login">

            <label>Username:</label>
            <input type="text" name="username" id="username">
            <p id="userError" class="error"></p>

            <label>Password:</label>
            <input type="password" name="password" id="password">
            <p id="passError" class="error"></p>

            <button type="submit">Login</button>
        </form>
    </div>

    <!-- JavaScript Validation -->
    <script>
        document.getElementById("loginForm").addEventListener("submit", function(event) {
            let username = document.getElementById("username").value.trim();
            let password = document.getElementById("password").value.trim();

            let userError = document.getElementById("userError");
            let passError = document.getElementById("passError");

            userError.innerHTML = "";
            passError.innerHTML = "";

            let isValid = true;

            if (username === "") {
                userError.innerHTML = "Username cannot be empty";
                isValid = false;
            }

            if (password === "") {
                passError.innerHTML = "Password cannot be empty";
                isValid = false;
            }

            if (!isValid) {
                event.preventDefault();
            }
        });
    </script>

</body>
</html>
"""

# SUCCESS PAGE
success_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Login Success</title>
</head>
<body style="text-align:center; margin-top:100px; font-family:Arial;">
    <h1>Login Successful!</h1>
    <h2>Welcome, {{ username }} 👋</h2>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    return render_template_string(login_page)

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    # Print username on backend terminal
    print("User logged in:", username)

    # Backend-level validation
    if username == "" or password == "":
        return "<h2>Error: Username or password cannot be empty!</h2>"

    # Return success page with username
    return render_template_string(success_page, username=username)


if __name__ == "__main__":
    app.run(debug=True)
