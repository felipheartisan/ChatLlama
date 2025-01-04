from googletrans import Translator

def traduzir_texto_para_pt(texto, idioma_origem='en', idioma_destino='pt'):
   
    translator = Translator()
    traducao = translator.translate(texto, src=idioma_origem, dest=idioma_destino)
    return traducao.text

def traduzir_texto_para_en(texto, idioma_origem='pt', idioma_destino='en'):

    translator = Translator()
    traducao = translator.translate(texto, src=idioma_origem, dest=idioma_destino)
    return traducao.text