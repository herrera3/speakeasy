import azure.cognitiveservices.speech as speechsdk
import openai


def transcrever_fala():
    
    chave_assinatura = 'YOUR_API?_KEY'
    regiao = 'brazilsouth'

    
    config = speechsdk.SpeechConfig(subscription=chave_assinatura, region=regiao)

    
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=config, language='pt-BR')

    print("Fale algo...")

    result = speech_recognizer.recognize_once()

    
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        texto = result.text
        print("Texto capturado:", texto)
        return texto

    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("Não foi possível reconhecer o áudio")
        return None

    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Reconhecimento cancelado. Motivo:", cancellation_details.reason)
        return None

def resumir_texto(texto):
    openai.api_key = 'YOUR_API?_KEY'

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Resuma e diminua o seguinte texto: " + texto,
        temperature=0.7,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    resumo = response.choices[0].text.strip()
    return resumo

texto_falado = transcrever_fala()
if texto_falado:
    resumo = resumir_texto(texto_falado)
    print("Resumo:", resumo)
