FROM python:3
RUN git clone https://github.com/PabloHerrera99/Monedas.git
WORKDIR /Monedas
CMD ["python3", "-m", "test_tragamonedas"]