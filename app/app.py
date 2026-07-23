from flask import Flask
import uuid

app = Flask(__name__)

@app.route("/")
def hello():
    request_id = str(uuid.uuid4())
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Tech Challenge 2</title>
        <style>
            body {{
                margin: 0;
                height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }}
            .card {{
                background: white;
                padding: 2.5rem 3rem;
                border-radius: 16px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
                text-align: center;
            }}
            h1 {{
                color: #4a3f6d;
                margin: 0 0 0.5rem 0;
                font-size: 2rem;
            }}
            p {{
                color: #888;
                font-size: 0.85rem;
                margin: 0;
                font-family: monospace;
            }}
            .emoji {{
                font-size: 2.5rem;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <div class="emoji">👋🥳🤸🏾‍♂️</div>
            <h1>Hello, World!</h1>
            <p>GUID: {request_id}</p>
        </div>
    </body>
    </html>
    """
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)