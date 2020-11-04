# Python Google Speech API CLI

Questo progetto ha lo scopo di fornire un'interfaccia da riga di comando alle API di Speech To Text di Google. 

## Prerequisiti

Windows/Linux/Mac sul quale è installato python 3. Se non lo si ha ci sono tutorial in internet che spiegano, per ciascun sistema operativo, come installarlo. 

- Per verificare la versione di python che si ha installata sul proprio PC, aprire il terminale (o la console di python se si è in Windows) e digitare `python -V`. Se nessuna versione di python è installata sul PC, dovreste ottenere un messaggio del tipo "`python. Command not found`", altrimenti verrà stampata a video la versione di python. Se la versione è < 3, allora provare a digitare il comando `python3 -V`. Se il comando risponde qualcosa del tipo `command not found`, allora non è installato python 3 sul vostro sistema operativo e seguire quindi un tutorial di installazione adatto per il vostro sistema operativo. Se invece il comando stampa la versione di python, allora avete python 3 installato sul vistro sistema.

## Uso

- creare un file chiamato `requirements.txt`, (oppure scaricare quello già presente nella stessa cartella di questo README) e inserire questo contenuto:

  ```
  certifi==2020.6.20
  chardet==3.0.4
  future==0.18.2
  idna==2.10
  pydub==0.24.1
  requests==2.24.0
  tqdm==4.51.0
  urllib3==1.25.11
  ```

- creare un virtual environment dentro il quale eseguire l'eseguibile da riga di comando

  - andare in una cartella a piacere (consiglio di crearne una e chiamarla con un nome a piacere, in questa guida "workdir")
  - aprire il terminale in quella cartella e digitare `virtualenv -p python3 <nome_a_piacere>`. Questo comando creerà dentro "workdir" un mini-abiente autocontenuto di python3
    - se il comand o fallisce installarlo `pip3 install virtualenv`
  - Attivare il virtualenv: `source <nome_a_piacere>/bin/activate`
  - sul terminale a inizio riga dovresti vedere prima del cursore una cosa del genere: `(<nome_a_piacere>)`. è il segno che il virtualenv si è attivato correttamente. **Tutto quello inerente a python che faremo da qua in avanti (installazione pacchetti compresa) verrà fatta nel virtualenv e non andrà ad intaccare nè python, nè i pacchetti installati nel "python di sistema"**. Qua siamo quindi in un ambiente isolato e autocontenuto
  - per verificare che il virtualenv stia effettivamente usando la versione di python 3, controllare con il comando `python -V` che la versione sia `> 3`. Per un'ulteriore verifica eseguire anche il comando `pip -V` che visualizzerà da qualche parte nella stringa che verrà visualizzata, anche la versione di python alla quale fa riferimento.
  - `pip install -r requirements.txt`  dopo aver copiato il file `requirements.txt` del punto precedente in "workdir". Questo comando installerà nel virtualenv tutte le dipendenze python all'interno del virtualenv e sarà **quindi possibile lanciare lo script**

  ## Eseguire da file sorgente

  ### <u>Attenzione!!!!!</u> Non distribuire il file sorgente in quanto contiene la chiave per chiamare le API di Google. Utilizzare il file sorgente solo per test di sviluppo, se si vuole aggiornare il software o se si è più che sicuri che il sorgente non verrà diffuso dalla persona alla quale lo state distribuendo. **Utilizzate il file compilato** per la distribuzione e l'utilizzo normale

  Partendo dallo **script sorgente** di seguito è descritto il suo utilizzo.

  - Nella forma più base è possibile eseguire lo script così: `python client.py <path_audio_file.wav>`. Per informazioni sull'utilizzo dell'utility è sempre possibile digitare `python client.py -h`. 
    - Di default la lingua impostata è quella italiana per gli audio in input. Se si desidera trascrivere file in lingua inglese digitare `python client.py --lang eng <path_audio_file_wav>`.

  Nella sezione **Release** di questo repository su GitHub è possibile scaricare la versione compilata (.pyc) del medesimo sorgente. Il codice al suo interno è oscurato, non accessibile, ne modificabile.

  Per eseguirlo guardare i punti sopra sostituendo al posto di `client.py` `client.pyc` (notare la "c" in fondo)

