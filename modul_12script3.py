import pandas as pd

df = pd.read_csv("C:/Users/tito_/PythonChatting/pythonProject/Negara.csv")
mean = df.groupby(['Benua']).mean(numeric_only=True)
std = df.groupby(['Benua']).std(numeric_only=True)

print("=== Rata-rata ===")
print(mean)
print("\n=== Standar Deviasi ===")
print(std)

mean.to_csv("C:/Users/tito_/PythonChatting/pythonProject/NegaraMean.csv", index=True)
std.to_csv("C:/Users/tito_/PythonChatting/pythonProject/NegaraStandarDeviasi.csv", index=True)

