import json

def lambda_handler(event, context):
    # Extraímos o prompt da solicitação recebida
    prompt = event.get('prompt', '')
    conversation_history = event.get('conversation_history', [])

    # Simulação de interação com o modelo - substitua pela integração real com o Bedrock se possível
    resposta_do_modelo = f"Você perguntou: {prompt}. Este é o modelo respondendo."

    # A resposta gerada pode ser concatenada ao histórico de conversa (se necessário)
    conversation_history.append({
        "prompt": prompt,
        "resposta": resposta_do_modelo
    })

    # Retorna o status e o histórico atualizado
    return {
        'statusCode': 200,
        'body': json.dumps({
            "resposta_do_modelo": resposta_do_modelo,
            "historico_atualizado": conversation_history
        })
    }
