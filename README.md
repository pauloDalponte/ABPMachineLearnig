# ABPMachineLearnig

# Tutorial início api Flask

### 1 Iniciar Virtual Environment

```bash
// Windows
python -m venv venv
venv\Scripts\activate

Linux & macOs
python -m venv venv
source venv/bin/activate
```

### 2 Instalar pacotes

```bash
pip install -r requirements.txt
pip install mysqlclient
pip install PyPDF2
```


### 3 Rodar servidor web

```bash
// Para rodar na porta padrão
flask run --host=0.0.0.0

// Para escolher a porta http
flask run --host=0.0.0.0 --port 5001
```
