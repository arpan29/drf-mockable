## Synopsis

This is a package which makes building mockable APIs a breeze for Django developers. The dependencies for this package are:

* Django
* Django Rest Framework (DRF)

## Installation

pip install drf-mockable


## Code Example

In your view class, just inherit the MockableView and define your mock_response. Thats it !!


from drf_mockable.mockable import MockableView

class MyMockAPI(MockableView):
    ''' 
        My Mock API which will return a mock response in case a need arises
    '''
    
    mock_response = {
        "message": "Here I am with a mock response", 
        "status": "success"
    }

    def post(self, request):
        '''
        '''
        print("Do your stuff here if mocked response is not required")


Now, just hit your MockAPI from any REST client with a header 'Mockable' set as 'True' and you should be able to get the mocked response. 

Sample Curl Request: 

curl -X <MY_HTTP_REQUEST_METHOD> http://<PATH_TO_MY_MOCK_API>/ -H 'content-type: application/json' -H 'mockable: True' -d '<MY_REQUEST_DATA>'

In case you do not want the mock response and want the API to run normally, just remove the Mockable header and your API will work normally.


## Motivation

In the world of APIs and Microservices, it often happens the front-end team (Mobile or UI Development) needs a sample API for testing out their integrations. The backend developers need to create mock APIs to help them in this regard. This package solves two problems which occur during this process:

1) Provide backend developers with a fast & easy way to get the mock APIs up and running.
2) In case the backend APIs are internally calling other third-party APIs and in case those third-party APIs are down, this will still allow you to keep your API up and running with a mock response.


## License

This package comes under the MIT License.