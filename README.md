
# py-monitor




Simple monitor app for controling a web apps online and saving history of app status. Its dockerize with makes app work easly.Github actions workflow helps with future continus integration
## Features

- Cheks status of selected website
- Logs the results for every request
- Runs in loop (repets by every 2 minutes)
- Works in docker
- Integrated github actions

## Installation

Install my-project with npm


### 1. Run locally

```bash
git clone https://github.com/Karmel00/py-monitor.git
```
```bash
cd py-monitor
```
```bash
pip install -r app/requirements.txt
```
```bash
python app/monitor.py
```
### 2. Run with Docker
```bash
docker build -t py-monitor .
```
```bash
docker run py-monitor
```
### 3. Run with docker compose (Recommended)
```bash
docker compose up
```
## Example of web_log_status.log
after staring the app the web_log_status.log should shows something familar to this:
```log
2025-08-01 19:23:01,722 - INFO - Adres: https://github.com - Status: działa
2025-08-01 19:23:01,819 - INFO - Adres: https://google.com - Status: działa
2025-08-01 19:23:02,359 - INFO - Adres: https://example.com - Status: działa
```


## 📫 Kontakt

- LinkedIn: www.linkedin.com/in/kamil-j-51ba2833a
- GitHub: [github.com/Karmel00](https://github.com/Karmel00)

