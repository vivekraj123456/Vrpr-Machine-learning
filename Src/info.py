import requests


def info(reg_no, api_key):
    url = "https://rto-vehicle-information-verification-india.p.rapidapi.com/api/v1/rc/vehicleinfo"

    payload = {
        "reg_no": reg_no,
        "consent": "Y",
        "consent_text": ("I hear by declare my consent agreement "
                         "for fetching my information via AITAN Labs API")
    }

    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": ("rto-vehicle-information-"
                            "verification-india.p.rapidapi.com")
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.json()
