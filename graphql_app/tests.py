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
# Create your tests here.