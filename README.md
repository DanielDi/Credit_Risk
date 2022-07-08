# Credit_Risk

## Web application
http://creditrisk.eastus.cloudapp.azure.com:8050

## Cloning this repo:
On a terminal...
- Alternative 1
Via web URL:
```git clone https://github.com/DanielDi/Credit_Risk.git```
- Alternative 2
Via ssh key:
```git clone git@github.com:DanielDi/Credit_Risk.git```

## Requirements
- virtualenv
    - Install using "pip3 install virtualenv"
- docker

## Execute notebooks
1. Create virtual environment
```bash
virtualenv -p python3 env
```
2. Activate virtual environment
```bash
.\env\Scripts\activate
```
3. Install dependencies
```bash
pip install -r .\project\requirements.txt
```
3. Change the python interpreter

## Execute dash application
1. Open the directory project in terminal 
2. Build the project:
```bash
docker build -t docker-dash project/.
```
3. Run the project:
```
docker run --name dash-project -it -p 8050:8050 docker-dash
```
4. Open in a browser http://localhost:8050
