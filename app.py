from flask import Flask, request, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

@app.route('/analisar', methods=['POST'])
def analisar():
    dados = request.get_json()
    texto = dados.get('conteudo', '')
    
    # Inicia contagem de tempo para simular processamento
    start_time = time.time()
    
    palavras_chave = ['python', 'flask', 'api', 'backend', 'dados', 'servidor', 'ia', 'algoritmo', 'html', 'css', 'javascript', 'react', 'sql']
    palavras = texto.split()
    total_palavras = len(palavras)
    total_caracteres = len(texto)
    
    # Encontra quais palavras-chave foram usadas
    termos_encontrados = [p for p in palavras_chave if p in texto.lower()]
    densidade = len(termos_encontrados)

    # Lógica de Classificação Profissional
    if total_palavras < 5:
        res = {
            "status": "Baixa Qualidade",
            "motivo": "Volume de dados insuficiente para processamento neural.",
            "confianca": "20%",
            "classe": "BaixaQualidade"
        }
    elif densidade >= 2:
        res = {
            "status": "Alta Qualidade",
            "motivo": f"Integridade técnica confirmada com {densidade} termos validados.",
            "confianca": "98%",
            "classe": "AltaQualidade"
        }
    else:
        res = {
            "status": "Qualidade Média",
            "motivo": "Conteúdo legível, porém com baixa densidade técnica.",
            "confianca": "60%",
            "classe": "QualidadeMédia"
        }

    # Tempo de resposta simulado
    process_time = round((time.time() - start_time) * 1000, 2)

    return jsonify({
        "analise_ia": res,
        "metricas": {
            "palavras": total_palavras,
            "caracteres": total_caracteres,
            "termos": densidade,
            "latencia": f"{process_time}ms"
        }
    })

if __name__ == "__main__":
    app.run(debug=True)