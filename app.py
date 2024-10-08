# app.py
from flask import Flask, request, jsonify, render_template, send_file
import pandas as pd
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        # Read the Excel file
        df = pd.read_excel(file)
        columns = df.columns.tolist() 
        return jsonify(columns=columns)

@app.route('/convert', methods=['POST'])
def convert_to_json():
    file = request.files['file']
    selected_columns = request.form.getlist('columns')
    json_filename = request.form.get('json_filename')

    df = pd.read_excel(file)
    df = df[selected_columns]

    for column in df.columns:
        if pd.api.types.is_datetime64_any_dtype(df[column]):
            df[column] = df[column].apply(lambda x: x.strftime('%Y-%m-%d') if pd.notna(x) else None)

    data = df.to_dict(orient='records')

    json_filepath = f"{json_filename}.json"
    with open(json_filepath, 'w') as json_file:
        json.dump(data, json_file, indent=2)

    return send_file(json_filepath, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
