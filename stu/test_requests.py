
import requests

from stu.mock import Mock


def get_token():

    res = requests.request(method="post",
                           url="https://test4.teletraan.io/graphql/?login",
                           json={
                                  "operationName": "login",
                                  "variables": {
                                    "input": {
                                      "account": "srm115",
                                      "password": "teletraa",
                                      "tenantCode": "admin"
                                    }
                                  },
                                  "query": "mutation login($input: LoginInput!) "
                                           "{\n  login(input: $input) {\n    token\n    userId\n    __typename\n  }\n}"
                                })

    res = res.json()

    token = res["data"]["login"]["token"]
    return token


def create_api(token, post="post"):

    mock = Mock()

    res = requests.request(method=post,
                           url="https://test4.teletraan.io/graphql/?createScmUnit",
                           headers={"Authorization": f"bearer {token}"},
                           json={
                              "operationName": "createScmUnit",
                              "variables": {
                                "input": {
                                  "abbreviation": mock.mock_data(),
                                  "name": mock.mock_data(),
                                  "remark": "213"
                                }
                              },
                              "query": "mutation createScmUnit($input: CreateScmUnitInput!)"
                                       " {\n  createScmUnit(input: $input)\n}"
                            })

    return res.json()


if __name__ == '__main__':

    se = get_token()

    for i in range(3):
        danyuan = create_api(se)

        print(danyuan)
