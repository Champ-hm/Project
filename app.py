import os
from flask import Flask, jsonify, render_template
from supabase import create_client

app = Flask(__name__)

# This part connects your app to the database using secret environment variables
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

@app.route('/')
def index():
    # This serves your HTML page
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    # This reaches out to your Supabase table 'items' and grabs everything
    response = supabase.table('items').select('*').execute()
    return jsonify(response.data)

if __name__ == '__main__':
    app.run(debug=True)
