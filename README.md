# Flask Paginated Response

Response maker for Flask with RFC Standards such as Link Headers

[![Build Status](https://travis-ci.org/vrcmarcos/flask-paginated-response.svg?branch=master)](https://travis-ci.org/vrcmarcos/flask-paginated-response) [![Coverage Status](https://coveralls.io/repos/github/vrcmarcos/flask-paginated-response/badge.svg?branch=master)](https://coveralls.io/github/vrcmarcos/flask-paginated-response?branch=master) [![GitHub version](https://badge.fury.io/gh/vrcmarcos%2Fflask-paginated-response.svg)](https://badge.fury.io/gh/vrcmarcos%2Fflask-paginated-response) [![Code Health](https://landscape.io/github/vrcmarcos/flask-paginated-response/master/landscape.svg?style=flat)](https://landscape.io/github/vrcmarcos/flask-paginated-response/master) [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/vrcmarcos/flask-paginated-response/master/LICENSE)

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

## Changelog

#### 1.0.0:
- **PaginatedResponse**: Created **PaginatedResponse** class