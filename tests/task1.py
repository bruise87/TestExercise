import pytest
import requests
import json
import time
from http import HTTPStatus

with open('../data.json') as dj:
    params = json.load(dj)

status_codes = params['status_codes']
delays = params['delays']
freeform = params['freeform_values']


class TestHttpBin:

    @property
    def base_url(self):
        return "http://httpbin.org"


    def test_httpbin_get(self):
        resp = requests.get(f'{self.base_url}/get')
        assert resp.status_code == HTTPStatus.OK


    def test_httpbin_post(self):
        resp = requests.post(f'{self.base_url}/post', data={'key': 'value'})
        assert resp.status_code == HTTPStatus.OK


    @pytest.mark.parametrize('status_code', status_codes)
    def test_httpbin_status(self, status_code):
        resp = requests.get(f'{self.base_url}/status/{status_code}')
        assert resp.status_code == status_code


    @pytest.mark.parametrize('delay', delays)
    def test_httpbin_delay(self, delay):
        start_time = time.time()
        resp = requests.get(f'{self.base_url}/delay/{delay}')
        end_time = time.time()
        assert resp.status_code == HTTPStatus.OK
        assert end_time - start_time >= delay


    @pytest.mark.parametrize('freeform', freeform)
    def test_httpbin_headers(self, freeform):
        resp = requests.get(f'{self.base_url}/response-headers?freeform={freeform}')
        assert resp.status_code == HTTPStatus.OK
        assert resp.json()['freeform'] == freeform
