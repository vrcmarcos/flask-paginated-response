# -*- coding: utf-8 -*-

from urllib import urlencode
from urlparse import urlparse, parse_qs, urlunparse

from flask import Response, request


class PaginatedResponse(Response):

    LINK_TEMPLATE = '<{0}size={1}&page={2}>; rel="{3}"'

    def __init__(self, per_page, current_page, total, **kwargs):
        headers = dict()

        link_header = self.__get_link_header(per_page, current_page, total)
        headers.update(link_header)

        headers['X-Total-Count'] = total

        super(PaginatedResponse, self).__init__(headers=headers, **kwargs)

    def __get_link_header(self, per_page, current_page, total):
        links = list()

        url = PaginatedResponse.__get_url_without_pagination()

        if not PaginatedResponse.__is_first_page(current_page):
            links.append(self.LINK_TEMPLATE.format(url, per_page, 1, 'first'))

        if not PaginatedResponse.__is_last_page(per_page, current_page, total):
            links.append(self.LINK_TEMPLATE.format(url, per_page, (total / per_page) + 1, 'last'))

        if PaginatedResponse.__has_next(per_page, current_page, total):
            links.append(self.LINK_TEMPLATE.format(url, per_page, current_page + 1, 'next'))

        if PaginatedResponse.__has_previous(current_page):
            previous_page = min(current_page - 1, total / per_page)
            links.append(self.LINK_TEMPLATE.format(url, per_page, previous_page, 'prev'))

        return dict(Link=', '.join(links))

    @staticmethod
    def __get_url_without_pagination():
        url = request.url
        parsed_url = urlparse(url)
        query = parse_qs(parsed_url.query)
        query.pop('size', None)
        query.pop('page', None)
        connector = '&' if query else '?'
        parsed_url = parsed_url._replace(query=urlencode(query, True))
        return '{0}{1}'.format(urlunparse(parsed_url), connector)

    @staticmethod
    def __is_first_page(current_page):
        return current_page == 1

    @staticmethod
    def __is_last_page(per_page, current_page, total):
        return per_page * current_page >= total > per_page * (current_page - 1)

    @staticmethod
    def __has_next(per_page, current_page, total):
        return current_page * per_page < total

    @staticmethod
    def __has_previous(current_page):
        return current_page > 1
