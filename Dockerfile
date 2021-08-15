FROM python:3.6.5
# Criando uma pasta para a aplicação
WORKDIR /app

# Copiando arquivos da pasta local para dentro do Docker
ADD main.py /app/
ADD main.py /app

# Instalando as dependências dentro do Docker
RUN pip install -r requirements.txt

EXPOSE 5000

#Rodando a aplicação
CMD ["python", "main.py"]