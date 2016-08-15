import requests
import time
from datetime import datetime
import json

HTTP_METHOD_POST = 'Post'
HTTP_METHOD_GET = 'Get'
AUTHORIZATION = 'Authorization'
BEARER = 'Bearer '
MIME_TYPE_JSON = 'application/json'
CONTENT_TYPE = 'Content-type'


def get_terms_api(token, url, i):
    print "loop : " + str(i)

    try:
        # https://umich.test.instructure.com/api/v1/accounts/1/terms
        # t_url = 'https://umich.test.instructure.com/api/v1/accounts/1/terms'
        t_url = url + '/api/v1/accounts/1/terms'
        headers = {CONTENT_TYPE: MIME_TYPE_JSON, AUTHORIZATION: BEARER + token}
        begin = datetime.now()
        response = requests.get(t_url, headers=headers)
        end = datetime.now()
        diff = end - begin
        print str(i) + " Api execution time: " + str(diff)
        begin = datetime.now()
        terms = json.loads(response.text)
        term_list = terms['enrollment_terms']
        for term in term_list:
            print "The term call: " + term['name']
        end = datetime.now()
        diff = end - begin
        print str(i) + " Json extraction time: " + str(diff)

    except (requests.exceptions.RequestException, Exception) as e:
        raise e


def main():
    with open("/usr/local/secret-volume/canvas-url", 'r') as url:
        canvas_url = url.read()
    with open("/usr/local/secret-volume/canvas-token", 'r') as token:
        canvas_token = token.read()
    for i in range(1, 2000):
        get_terms_api(canvas_token, canvas_url, i)


if __name__ == '__main__':
    main()
