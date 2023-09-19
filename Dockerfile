FROM python:3
RUN git clone https://github.com/PabloHerrera99/Monedas.git
WORKDIR /TMonedas
CMD ["python3", "-m", "test_tragamonedas"]