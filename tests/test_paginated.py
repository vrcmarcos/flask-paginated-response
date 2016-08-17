# -*- coding: utf-8 -*-

from unittest import TestCase

from tests import app

REL_NEXT = 'rel="next"'
REL_PREVIOUS = 'rel="prev"'
REL_FIRST = 'rel="first"'
REL_LAST = 'rel="last"'


class TestPaginatedResponse(TestCase):

    def setUp(self):
        self.test_client = app.test_client()

    def test_should_return_links_headers_next_and_last_when_has_three_pages_and_request_is_first_page(self):
        expected_refs = [REL_LAST, REL_NEXT]
        response = self.test_client.get('paginated/has_pagination')
        link_headers = response.headers.get('Link').split(',')
        self.assertEqual(len(expected_refs), len(link_headers))
        for link_header in link_headers:
            rel_ref = link_header.split('; ')[1]
            self.assertIn(rel_ref, expected_refs)

    def test_should_return_all_link_headers_when_has_has_three_pages_and_request_is_second_page(self):
        expected_refs = [REL_LAST, REL_NEXT, REL_FIRST, REL_PREVIOUS]
        response = self.test_client.get('paginated/has_pagination?page=2')
        link_headers = response.headers.get('Link').split(',')
        self.assertEqual(len(expected_refs), len(link_headers))
        for link_header in link_headers:
            rel_ref = link_header.split('; ')[1]
            self.assertIn(rel_ref, expected_refs)

    def test_should_return_link_headers_when_has_has_three_pages_and_request_is_third_page(self):
        expected_refs = [REL_FIRST, REL_PREVIOUS]
        response = self.test_client.get('paginated/has_pagination?page=3')
        link_headers = response.headers.get('Link').split(',')
        self.assertEqual(len(expected_refs), len(link_headers))
        for link_header in link_headers:
            rel_ref = link_header.split('; ')[1]
            self.assertIn(rel_ref, expected_refs)
