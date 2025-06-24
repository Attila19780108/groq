import requests

try:
    response = requests.post(
        "https://groq-chatbot.onrender.com/chat",
        headers={"Content-Type": "application/json"},
        json={"message": "Mondj egy magyar viccet!"}
    )

    print("HTTP status kód:", response.status_code)

    if response.status_code == 200:
        print("✅ Válasz a szervertől:")
        print(response.json()["response"])
    else:
        print("⚠️ Hiba a válasznál:")
        print(response.text)

except Exception as e:
    print("❌ Hiba történt:")
    print(e)
