FROM mullerfs/queshi-server
# Criando uma pasta para a aplicação
WORKDIR /app

# Copiando arquivos da pasta local para dentro do Docker
ADD *.py /app/
ADD requirements.txt /app/
ADD app /app/
ADD .env /app/

# Instalando as dependências dentro do Docker
RUN pip install -r requirements.txt

EXPOSE 5000

#Rodando a aplicação
CMD ["python", "main.py"]