# import pytest

# PRODUCTS_ENDPOINT = "/products"


# @pytest.mark.tags("products_tag")
# def test_users_can_see_products(
#     fakestore_api
# ):
#     response = fakestore_api.get(
#         f"{PRODUCTS_ENDPOINT}"
#     )
#     assert response.status == 200


# @pytest.mark.tags("visible")
# @pytest.mark.parametrize("id, title", [
#     (1, "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops"),
#     (2, "Mens Casual Premium Slim Fit T-Shirts ")
# ])
# def test_product_title_should_be_visible(
#     fakestore_api, id, title
# ):
#     response = fakestore_api.get(
#         f"{PRODUCTS_ENDPOINT}/{id}"
#     )
#     assert response.json()["title"] == title


# @pytest.mark.tags("create")
# def test_product_must_be_created(
#     fakestore_api
# ):
#     response = fakestore_api.post("/products",
#                                   data={
#                                       "title": "string",
#                                       "price": 0.1,
#                                       "description": "string",
#                                       "category": "string",
#                                       "image": "http://example.com"
#                                   })
#     assert response.status == 201


# @pytest.mark.tags("update")
# def tests_users_should_be_able_to__put_metod(
#     fakestore_api
# ):
#     response = fakestore_api.put("products/1",
#                                  data={
#                                      "id": 0,
#                                      "title": "string",
#                                      "price": 0.1,
#                                      "description": "string",
#                                      "category": "string",
#                                      "image": "http://example.com"
#                                  })
#     assert response.status == 200


# @pytest.mark.tags("delete")
# def test_users_should_be_able_to_delete_their_account(
#     fakestore_api
# ):
#     response = fakestore_api.delete("products/1")
#     assert response.status == 200


# @pytest.mark.tags("make")
# def test_product_must_be_make(
#     fakestore_api
# ):
#     response = fakestore_api.post("/carts",
#                                   data={

#                                       "products": [
#                                           {
#                                               "title": "string",
#                                               "price": 0.1,
#                                               "description": "string",
#                                               "category": "string",
#                                               "image": "http://example.com"
#                                           }
#                                       ]

#                                   })
#     assert response.status == 201


# @pytest.mark.tags("invent")
# def test_product_should_be_invent(
#     fakestore_api
# ):
#     response = fakestore_api.post("/carts",
#                                   data={
#                                       "products": [
#                                           {
#                                               "title": "string",
#                                               "price": 0.1,
#                                               "description": "string",
#                                               "category": "string",
#                                               "image": "http://example.com"
#                                           }
#                                       ]
#                                   })

#     assert response.status == 201


# @pytest.mark.tags("milka")
# def test_products_should_be_create_products(
#     fakestore_api
# ):
#     response = fakestore_api.post("/users",
#                                   data={
#                                       "id": 0,
#                                       "username": "string",
#                                       "email": "string",
#                                       "password": "string"
#                                   })
#     assert response.status == 201


# @pytest.mark.tags("update_email")
# def test_product_should_be_update_email(
#     fakestore_api
# ):
#     response = fakestore_api.put("/carts/1",
#                                  data={
#                                      "id": 0,
#                                      "userId": 0,
#                                      "products": [
#                                          {
#                                              "id": 0,
#                                              "title": "string",
#                                              "price": 0.1,
#                                              "description": "string",
#                                              "category": "string",
#                                              "image": "http://example.com"
#                                          }
#                                      ]
#                                  })
#     assert response.status == 200


# @pytest.mark.tags("limma")
# def test_result_should_be_limma_mode(
#     fakestore_api
# ):
#     response = fakestore_api.put("/users/1",
#                                  data={
#                                      "id": 0,
#                                      "username": "string",
#                                      "email": "string",
#                                      "password": "string"
#                                  })
#     assert response.status == 200


# @pytest.mark.tags("clear")
# def test_product_should_be_clear_type(
#         fakestore_api
# ):
#     response = fakestore_api.delete("/carts/1")
#     assert response.status == 200


# @pytest.mark.tags("lucky")
# def test_result_should_be_lucky(
#     fakestore_api
# ):
#     response = fakestore_api.delete("/users/1")
#     assert response.status == 200


# @pytest.mark.tags("maqa")
# def test_result_should_be_post_metod(
#     fakestore_api
# ):
#     response = fakestore_api.post("/auth/login",
#                                   data={
#                                       "token": "string"
#                                   })
#     assert response.status == 400
#     print(response.status)


# @pytest.mark.tags("matlab")
# def test_result_should_be_post_metod(
#     petstore_swagger
# ):
#     response = petstore_swagger.post("/v2/user",
#                                      data={
#                                          "id": 0,
#                                          "username": "string",
#                                          "firstName": "string",
#                                          "lastName": "string",
#                                          "email": "string",
#                                          "password": "string",
#                                          "phone": "string",
#                                          "userStatus": 0
#                                      }
#                                      )
#     assert response.status == 200
#     print(response.status)


# @pytest.mark.tags("mali")
# def test_result_should_be_post_metod(
#     petstore_swagger
# ):
#     response = petstore_swagger.post("/v2/user/createWithArray",
#                                      data=[
#                                          {
#                                              "id": 0,
#                                              "username": "string",
#                                              "firstName": "string",
#                                              "lastName": "string",
#                                              "email": "string",
#                                              "password": "string",
#                                              "phone": "string",
#                                              "userStatus": 0
#                                          }
#                                      ])
#     assert response.status == 200


# @pytest.mark.tags("beliver")
# def test_result_should_be_access(
#     petstore_swagger
# ):
#     response = petstore_swagger.post("/v2/user/createWithList",
#                                      data=[
#                                          {
#                                              "id": 0,
#                                              "username": "string",
#                                              "firstName": "string",
#                                              "lastName": "string",
#                                              "email": "string",
#                                              "password": "string",
#                                              "phone": "string",
#                                              "userStatus": 0
#                                          }
#                                      ])
#     assert response.status == 200


# @pytest.mark.tags("emil")
# def test_result_should_be_true_userName(
#     petstore_swagger
# ):
#     response = petstore_swagger.put("/v2/user/emin.muhammadi",
#                                     data={
#                                         "id": 0,
#                                         "username": "string",
#                                         "firstName": "string",
#                                         "lastName": "string",
#                                         "email": "string",
#                                         "password": "string",
#                                         "phone": "string",
#                                         "userStatus": 0
#                                     })
#     assert response.status == 200


# @pytest.mark.tags("alessandro")
# def test_result_should_be_maqa_format(
#     petstore_swagger
# ):
#     response = petstore_swagger.delete("/v2/user/baxis.maniyev")
#     assert response.status == 404


# @pytest.mark.tags("null")
# def test_result_should_be_pain(
#     petstore_swagger
# ):
#     response = petstore_swagger.get("/v2/user/login?username=baxis.maniyev&password=1234lamao",
#                                     data={
#                                         "code": 200,
#                                         "type": "unknown",
#                                         "message": "logged in user session:1773491746636"
#                                     })
#     assert response.status == 200


# @pytest.mark.tags("holy")
# def test_result_should_be_access_temple(
#     petstore_swagger
# ):
#     response = petstore_swagger.get("/v2/user/logout",
#                                     data={
#                                         "code": 200,
#                                         "type": "unknown",
#                                         "message": "ok"
#                                     })
#     assert response.status == 200


# @pytest.mark.tags("manizada")
# def test_result_should_be_mogged(
#     petstore_swagger
# ):
#     response = petstore_swagger.get("/v2/user/bakhishowski",
#                                     data={
#                                         "code": 1,
#                                         "type": "error",
#                                         "message": "User not found"
#                                     })
#     assert response.status == 404

# import os
# from playwright.sync_api import expect
# import pytest



# @pytest.mark.tags("smartphone")
# def test_result_should_catacory(forTesting):
#     forTesting.goto('https://mgstore.az/?gad_source=1&gad_campaignid=22451628657&gbraid=0AAAAADdE1OoQKf1cASRNMSlOd4v2npl69')
#     forTesting.locator('#maincontent > div.columns > div > section.sect.s1 > div.container.container_s1 > div.container__elem.fz.fw.container__elem--3.menu > nav > ul > li:nth-child(2) > a > span').click()
#     expect(forTesting.locator('#maincontent > div.category-cms > div:nth-child(2) > div > div > div > div:nth-child(1) > div > div.cont__top.cont__top--catalog > div > h1')).to_contain_text('Smartfonlar və aksessuarlar')

