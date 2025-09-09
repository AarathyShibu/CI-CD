from flask import Flask, render_template_string

app = Flask(__name__)

# The HTML and CSS for a beautiful "Hello World"
HTML_CONTENT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello, Beautiful World!</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
        body {
            font-family: 'Inter', sans-serif;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            color: white;
            background: linear-gradient(135deg, #1d2671, #22294f, #0c1440);
            text-align: center;
            animation: background-pan 20s linear infinite;
        }

        @keyframes background-pan {
            from { background-position: 0% 0%; }
            to { background-position: 100% 100%; }
        }

        .container {
            padding: 2rem;
            border-radius: 1rem;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        }

        h1 {
            font-size: clamp(2rem, 5vw, 4rem);
            font-weight: 700;
            letter-spacing: 0.1em;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Hello, Beautiful World!</h1>
    </div>
</body>
</html>
"""

@app.route('/')
def hello_world():
    return render_template_string(HTML_CONTENT)

if __name__ == '__main__':
    # Running in production, Gunicorn will handle this
    app.run(host='0.0.0.0', port=5000)

