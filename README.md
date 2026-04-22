# Petstore API testing using Playwright



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
py -m pytest tests/. -v --tags smartphone --html=reports/report.html
```
```
```
```
py -m pytest tests/. -v --html=reports/report.html
