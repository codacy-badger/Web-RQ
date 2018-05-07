#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
class UrlSetter(object):

    @staticmethod
    def gen_url(base_url: str, params: dict) -> str:
        from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse
        components = urlparse(base_url)

        query_pairs = parse_qsl(components.query)

        query_pairs.extend((field, value) for (field, value) in params.items() if value)

        query_str = urlencode(query_pairs)

        new_url = (
            components.scheme,
            components.netloc,
            components.path,
            components.params,
            query_str,
            components.fragment
        )

        return urlunparse(new_url)
