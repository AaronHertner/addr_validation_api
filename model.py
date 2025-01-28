from openai import OpenAI
from init import Text

class AddressValidator():

    def __init__(self):
        self.client = OpenAI(api_key="sk-5de2b4e9a1b04f49a08673cca6ddda9b", base_url="https://api.deepseek.com")
        self.text = Text()

        try:
            self.client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": self.text.CONTEXT_MESSAGE},
                ],
                stream=False
            )
            print('\033[96m' + 'Connection accepted, welcome to the DeepSeek API!' + '\033[0m')
        except Exception as e:
            print('\033[93m'+ "Failed to establish connection...")
            print(e + '\033[0m' )

    def query(self, business, address, sugg_address):
        message = f"""
            The business is named "{business}",
            our address on file is "{address}",
            and the suggested address is "{sugg_address}"
        """
        res = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": self.text.CONTEXT_MESSAGE},
                {"role": "user", "content": message},
            ],
            stream=False
        )

        data = res.choices[0].message.content
        data = data.split("|")
        data = [item.strip() for item in data]
        data = {
            "status": data[0],
            "confidence": data[1],
            "suggested_address": data[2],
            "notes": data[3]
        }

        print(data)

        return data
    