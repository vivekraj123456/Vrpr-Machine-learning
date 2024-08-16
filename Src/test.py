from datetime import datetime

currentTime = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
fileName = f"vrpr_{currentTime}"
print(fileName)
