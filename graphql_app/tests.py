from graphene_django.utils.testing import GraphQLTestCase


class GraphQLTest(GraphQLTestCase):
    fixtures = ["users.json"]

    def test_retrieve_by_id(self):
        expected = {
            "data": {
                "user": {
                    "id": "2",
                    "name": "Dan Bilzerian",
                    "followers": [
                        {
                            "name": "John Doe"
                        }
                    ]
                }
            }
        }
        res = self.query(
            """
            {
              user(id: 2) {
                id
                name
                followers {
                  name
                }
              }
            }
            """
        )
        self.assertEqual(res.status_code, 200)
        self.assertEqual(expected, res.json())



    def test_create_user(self):
         expected = {
            "data": {
                "createUser":{
                "ok":True,
                "user": {
                    "id": "3",
                    "name": "Elon Musk"
                }
                }
            }
        }
         
         res = self.query(
             """
             mutation createUser{
                createUser(input:{
                    name:"Elon Musk"
                }) {
                ok
                user {
                    id
                    name
                }
                }
             }
             """
         )
         self.assertEqual(res.status_code, 200)
         self.assertEqual(expected, res.json())
         
    def test_retrieve_user_with_posts(self):
        expected = {
            "data": {
                "user": {
                    "id": "2",
                    "name": "Dan Bilzerian",
                    "followers": [
                        {
                            "name": "John Doe"
                        }
                    ],
                    "postSet": [
                        {
                            "content": "I love to party!!!"
                        }
                    ]
                }
            }
        }

        res = self.query(
            """
            {
              user(id: 2) {
                id
                name
                followers {
                  name
                }
                postSet {
                  content
                }
              }
            }
            """
        )
        self.assertEqual(res.status_code, 200)
        self.assertEqual(expected, res.json())


    def test_list_users(self):
        res = self.query(
            """
            {
            users {
                name
                }
            }
            """
        )
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(2, len(res.json()["data"]["users"]))

# Create your tests here.
