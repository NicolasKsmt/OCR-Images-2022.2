
# Trabalho de Processamento de Imagens 2022.2 - UFRRJ

Reconhecimento de caracteres em imagens (OCR) utilizando Python + OpenCV e Tesseract 




## Grupo
Integrantes:    
Nicolas Machado Pereira     
Vitor Moreira de Brito  
Lediane Oliveira da Silva     
Matheus Montenegro Soares 
## Como rodar o projeto:

Instale as bibliotecas necessárias:  **pip install opencv-python** e **pip install pytesseract**

No linux, instale o tesseract-ocr: **sudo apt-get install tesseract-ocr**

No Windows, instale o tesseract-ocr: https://github.com/UB-Mannheim/tesseract/wiki

Tenha certeza que na linha 13 do arquivo **main.py** a variável "path" está com o caminho para o tesseract.exe correto, se não acontecerá um erro.

Dica: **which tesseract** no terminal para descobrir o path do tesseract no linux e **where tesseract** no windows.

Path default do tesseract no Linux (Ubuntu): r'/usr/bin/tesseract'  

Path default do tesseract no Windows : r'C:\Users\Python\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

Leia os comentários no código (principalmente no **main.py**) para entender melhor o que está acontecendo.

Para rodar use: **python3 main.py**


