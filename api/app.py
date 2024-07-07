from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

data = {
    "cortes": [
        { "id": 1, "nome": "Militar", "preco": "R$10" },
        { "id": 2, "nome": "Social", "preco": "R$15" },
        { "id": 3, "nome": "Degradê", "preco": "R$30" },
        { "id": 4, "nome": "Feminino", "preco": "R$40" }
    ],
    "barbas": [
        { "id": 1, "nome": "Simples", "preco": "R$10" },
        { "id": 2, "nome": "Desenhada", "preco": "R$30" },
        { "id": 3, "nome": "Completa", "preco": "R$35" }
    ],
    "outrosServicos": [
        { "id": 1, "nome": "Design de sobrancelhas", "preco": "R$20" },
        { "id": 2, "nome": "Limpeza de sobrancelhas", "preco": "R$25" }
    ]
}

@app.route('/cortes', methods=['GET'])
def get_cortes():
    return jsonify(data['cortes'])

@app.route('/cortes', methods=['POST'])
def create_corte():
    corte = request.json
    data['cortes'].append(corte)
    return jsonify(corte), 201

@app.route('/cortes/<int:corte_id>', methods=['PUT'])
def update_corte(corte_id):
    updated_corte = request.json
    for i, corte in enumerate(data['cortes']):
        if corte['id'] == corte_id:
            data['cortes'][i] = updated_corte
            return jsonify(updated_corte)
    return jsonify({'error': 'Corte not found'}), 404

@app.route('/cortes/<int:corte_id>', methods=['DELETE'])
def delete_corte(corte_id):
    global data
    data['cortes'] = [corte for corte in data['cortes'] if corte['id'] != corte_id]
    return jsonify({'message': 'Corte deleted'}), 204

@app.route('/barbas', methods=['GET'])
def get_barbas():
    return jsonify(data['barbas'])

@app.route('/barbas', methods=['POST'])
def create_barba():
    barba = request.json
    data['barbas'].append(barba)
    return jsonify(barba), 201

@app.route('/barbas/<int:barba_id>', methods=['PUT'])
def update_barba(barba_id):
    updated_barba = request.json
    for i, barba in enumerate(data['barbas']):
        if barba['id'] == barba_id:
            data['barbas'][i] = updated_barba
            return jsonify(updated_barba)
    return jsonify({'error': 'Barba not found'}), 404

@app.route('/barbas/<int:barba_id>', methods=['DELETE'])
def delete_barba(barba_id):
    global data
    data['barbas'] = [barba for barba in data['barbas'] if barba['id'] != barba_id]
    return jsonify({'message': 'Barba deleted'}), 204

@app.route('/outrosServicos', methods=['GET'])
def get_outros_servicos():
    return jsonify(data['outrosServicos'])

@app.route('/outrosServicos', methods=['POST'])
def create_outro_servico():
    outro_servico = request.json
    data['outrosServicos'].append(outro_servico)
    return jsonify(outro_servico), 201

@app.route('/outrosServicos/<int:servico_id>', methods=['PUT'])
def update_outro_servico(servico_id):
    updated_servico = request.json
    for i, servico in enumerate(data['outrosServicos']):
        if servico['id'] == servico_id:
            data['outrosServicos'][i] = updated_servico
            return jsonify(updated_servico)
    return jsonify({'error': 'Serviço not found'}), 404

@app.route('/outrosServicos/<int:servico_id>', methods=['DELETE'])
def delete_outro_servico(servico_id):
    global data
    data['outrosServicos'] = [servico for servico in data['outrosServicos'] if servico['id'] != servico_id]
    return jsonify({'message': 'Serviço deleted'}), 204

if __name__ == '__main__':
    app.run(debug=True)
