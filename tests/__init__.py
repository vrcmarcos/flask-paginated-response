# -*- coding: utf-8 -*-

from flask import Flask, Response, request

from flask_paginated_response import PaginatedResponse

app = Flask('flask-test-response')


@app.route('/healthcheck')
def healthcheck():
    return Response(status=200)


@app.route('/paginated/has_pagination')
def paginated():
    page = int(request.args.get('page', '1'))
    return PaginatedResponse(20, page, 50, Response(status=200))
