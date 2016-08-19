# Flask Paginated Response

Response maker for Flask with RFC Standards such as Link Headers

[![Build Status](https://travis-ci.org/vrcmarcos/flask-paginated-response.svg?branch=master)](https://travis-ci.org/vrcmarcos/flask-paginated-response) [![Coverage Status](https://coveralls.io/repos/github/vrcmarcos/flask-paginated-response/badge.svg?branch=master)](https://coveralls.io/github/vrcmarcos/flask-paginated-response?branch=master) [![PyPI version](https://badge.fury.io/py/Flask-Paginated-Response.svg)](https://badge.fury.io/py/Flask-Paginated-Response) [![Code Health](https://landscape.io/github/vrcmarcos/flask-paginated-response/master/landscape.svg?style=flat)](https://landscape.io/github/vrcmarcos/flask-paginated-response/master) [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/vrcmarcos/flask-paginated-response/master/LICENSE)

## Instalation

```bash
pip install Flask-Paginated-Response
```

## Usage

To use Flask Paginated Response, build your response object with the *PaginatedResponse* class:

```python
import json
from flask_paginated_response import PaginatedResponse

@app.route('/')
def index(self):
	per_page = 10
    current_page = 0
    total = 18
    response = {'status': 'online'}
	return PaginatedResponse(per_page, current_page, total, json.dumps(response))
```

Using *PaginatedResponse* class, you will get this response headers:

```bash
HTTP/1.0 200 OK
X-Total-Count: 18
Link: <http://localhost:5000/?size=3&page=5>; rel="last", <http://localhost:5000/?size=3&page=1>; rel="next"
Content-Type: application/json
Content-Length: 515
Server: Werkzeug/0.11.10 Python/2.7.10
Date: Thu, 21 Jul 2016 14:08:23 GMT
```

## Changelog

#### 1.0.1:
- **PaginatedResponse**: Extending the full *Response* **\_\_init__** method with all available *kwargs*

#### 1.0.0:
- **PaginatedResponse**: Created **PaginatedResponse** class