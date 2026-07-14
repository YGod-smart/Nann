import requests

class Internet:
    
    def __init__(self):
        pass
    
    def can_handle(self, user_input):
        user_input = user_input.lower()

        return user_input.startswith("search ")
    
    def handle(self, user_request):
        query = user_request[7:]
        
        return self.search(query)
    
    #def search(self, query):

        #try:
        #    url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + query


        #    response = requests.get(url)

         #   data = response.json()
        #    
        #    return data.get(
        #        "extract",
        #        "I couldn't find information about that."
         #   )

        #except Exception as e:
        #    print(e)
         #   return "I cannot connect to the internet right now."
         
    def search(self, query):

        try:
            url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + query

            headers = {
                "User-Agent": "Nann Assistant/1.0"
            }

            response = requests.get(
                url,
                headers=headers
            )

            data = response.json()

            if data.get("type") == "disambiguation":
                return "I found multiple results. Please be more specific."

            return data.get(
                "extract",
                "I couldn't find information about that."
            )

        except Exception as e:
            print(e)
            return "I cannot connect to the internet right now."