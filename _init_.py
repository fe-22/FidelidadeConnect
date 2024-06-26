from flask import Flask, request, send_file, render_template, redirect, url_for, jsonify
import pandas as pd
import os
import logging

app = Flask(__name__, template_folder="templates")

# Configuração do diretório de upload
UPLOAD_FOLDER = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Garante que o diretório de uploads existe
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Configurar logging
logging.basicConfig(level=logging.INFO)

# Página principal
@app.route("/")
def index():
    return render_template("cad_mem.html")

@app.route('/favicon.ico')
def favicon():
    return send_file(os.path.join(app.root_path, 'static', 'img', 'favicon.ico'), mimetype='image/vnd.microsoft.icon')

@app.route('/uploads', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if not file.filename.endswith('.xlsx'):
            return 'Invalid file type. Only .xlsx files are allowed.'
        filename = os.path.join(app.config['UPLOAD_FOLDER'], 'dados_formulario.xlsx')
        file.save(filename)
        app.logger.info(f"File saved at {filename}")
        return 'File uploaded successfully'
    except Exception as e:
        app.logger.error(f"Error uploading file: {e}")
        return str(e)

# Geração do arquivo Excel
@app.route('/generate_excel', methods=['POST'])
def generate_excel():
    try:
        dados_do_formulario = request.form.to_dict()
        df = pd.DataFrame([dados_do_formulario])

        excel_path = os.path.join(app.config['UPLOAD_FOLDER'], 'dados_formulario.xlsx')

        if os.path.exists(excel_path):
            df_existing = pd.read_excel(excel_path)
            df_combined = pd.concat([df_existing, df], ignore_index=True)
            df_combined.to_excel(excel_path, index=False)
        else:
            df.to_excel(excel_path, index=False)

        app.logger.info(f"Excel file generated at {excel_path}")
        return 'Excel gerado com sucesso!'
    except Exception as e:
        app.logger.error(f"Error generating Excel: {e}")
        return str(e)

# Download do arquivo Excel
@app.route('/uploads_excel')
def download_excel():
    try:
        excel_path = os.path.join(app.config['UPLOAD_FOLDER'], 'dados_formulario.xlsx')
        return send_file(excel_path, as_attachment=True, download_name='dados_formulario.xlsx')
    except Exception as e:
        app.logger.error(f"Error downloading Excel: {e}")
        return str(e)

# Mostrar os últimos 50 cadastros
@app.route('/result', methods=['GET'])
def result():
    try:
        excel_path = os.path.join(app.config['UPLOAD_FOLDER'], 'dados_formulario.xlsx')
        app.logger.info(f"Excel path: {excel_path}")

        if os.path.exists(excel_path):
            app.logger.info("Excel file exists. Loading data...")
            df = pd.read_excel(excel_path)
            ultimos_50_cadastros = df.tail(50)
            return render_template('pes.html', cadastros=ultimos_50_cadastros.to_dict(orient='records'))
        else:
            app.logger.warning("Excel file does not exist. Redirecting to index.")
            return redirect(url_for('index'))
    except Exception as e:
        app.logger.error(f"Error loading result: {e}")
        return str(e)

# Dados para o dashboard
@app.route('/dados_dashboard', methods=['GET'])
def dados_dashboard():
    try:
        excel_path = os.path.join(app.config['UPLOAD_FOLDER'], 'dados_formulario.xlsx')
        if os.path.exists(excel_path):
            df = pd.read_excel(excel_path)
            data_json = df.to_json(orient='records')
            return jsonify(data_json)
        else:
            return jsonify({"error": "Excel file not found"}), 404
    except Exception as e:
        app.logger.error(f"Error loading dashboard data: {e}")
        return jsonify({"error": str(e)}), 500

# Renderização da página 404
@app.route('/404')
def render_404_page():
    try:
        return render_template('404.html')
    except Exception as e:
        app.logger.error(f"Error rendering 404 page: {e}")
        return str(e)

if __name__ == "__main__":
    app.run(debug=False)
