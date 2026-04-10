# Sistema di Gestione Sicura delle Password

## Obiettivo del Progetto
Lo scopo di questo progetto è dimostrare alcuni principi fondamentali della sicurezza informatica attraverso una semplice applicazione web. L'applicazione gestisce in modo sicuro la registrazione e il login degli utenti, memorizza le password in formato sicuro tramite hashing, permette la verifica dell'integrità e fornisce una base per esplorare vulnerabilità e relative contromisure nell'ambito dell'autenticazione.

## Tecnologie Utilizzate
* **Linguaggio:** Python
* **Framework Web:** Flask (micro-framework per creare l'interfaccia web)
* **Librerie di Sicurezza:** `bcrypt` (per l'hashing e il salting delle password)
* **Salvataggio Dati:** File `.json` locale (`users.json`)
* **Frontend:** HTML e CSS base per l'interfaccia utente

## Linguaggio di Programmazione
Il progetto è stato sviluppato interamente in **Python**. La scelta di questo linguaggio è dettata dalla sua versatilità, semplicità sintattica e dall'ampio ecosistema di librerie disponibili. Questo ha permesso di gestire in modo efficiente sia la logica di backend dell'applicazione sia le operazioni di sicurezza, mantenendo il codice pulito e facilmente manutenibile.

## Funzionalità Implementate
1. **Registrazione Sicura:** L'utente inserisce username e password. La password viene "saltata" e "hashata" tramite l'algoritmo bcrypt, che offre elevata resistenza contro attacchi brute-force e rainbow-table grazie alla sua lentezza computazionale. Le credenziali vengono poi salvate nel file `users.json`.
2. **Login Sicuro:** In fase di accesso, il sistema confronta l'hash della password inserita dall'utente con l'hash salvato nel file `.json` per autenticarlo.
3. **Verifica di integrità:** Il sistema permette di rilevare modifiche o manomissioni al file JSON confrontando l'hash inserito con quello salvato.
4. **Simulazione di Attacco a Dizionario:** È incluso uno script (`attacco_dizionario.py`) che tenta di indovinare le password degli utenti utilizzando una lista predefinita di parole comuni (dizionario). Lo script calcola l'hash di ogni parola e lo confronta con quelli salvati per rilevare password deboli.

## Struttura del Progetto
* `app.py`: Il file principale che avvia l'applicazione web Flask e gestisce le rotte (`/`, `/login`, `/register`).
* `auth.py`: Modulo che gestisce la logica di sicurezza, inclusa la lettura/scrittura su JSON, la generazione dell'hash bcrypt e la verifica delle credenziali.
* `attacco_dizionario.py`: Script standalone per simulare e testare la vulnerabilità delle password salvate tramite un attacco a dizionario.
* `users.json`: Database locale (file JSON) dove vengono memorizzati gli username e gli hash delle password.
* `templates/`: Cartella contenente le pagine HTML (`index.html`, `login.html`, `register.html`).
* `static/`: Cartella contenente il foglio di stile (`style.css`) per l'interfaccia web.

## Come avviare il progetto

### Prerequisiti
Assicurati di avere Python installato sul tuo sistema. Installa le dipendenze necessarie eseguendo questo comando nel terminale:

```bash
pip install flask bcrypt
```

### Avvio dell'Applicazione Web
- Apri il terminale nella directory del progetto.
- Esegui il file principale dell'applicazione Flask:
```bash
python app.py
```
- Apri il browser e vai all'indirizzo indicato nel terminale (solitamente `http://127.0.0.1:5000/`).

### Esecuzione dell'Attacco a Dizionario
Per testare la robustezza delle password salvate nel file `users.json`, puoi eseguire lo script di attacco:
```bash
python attacco_dizionario.py
```
Il terminale mostrerà quali account (se presenti) sono stati compromessi perché utilizzano password deboli presenti nel dizionario.
