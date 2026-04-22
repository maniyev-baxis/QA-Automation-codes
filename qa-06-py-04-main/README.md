# Playwright Browsers



```sh
$ py -m venv .venv
```

```sh
$ source .venv/Scripts/Activate
```

```sh
$ py -m pip install pytest pytest-playwright pytest-html pytest-tagging
```

```sh
py -m pip freeze > requirements.txt
```

```sh
py -m pip install -r requirements.txt
```


(optional step)
```sh
$ playwright install
``` 


```sh
py -m pytest -v --browser chromium --headed -q --tracing=on --video=on --html=reports/report.html --tags login_pom --slowmo 800
```
py -m pytest -v --browser chromium --headed -q --tracing=on --video=on --html=reports/report.html --tags neurotimepage --slowmo 800
