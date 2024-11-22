import pandas as pd

# Datos de superhéroes ficticios
data = {
    "Nombre": ["Flashman", "Aquamigo", "Volt-Woman", "ShadowKid"],
    "Superpoder": ["Velocidad", "Hablar con peces", "Electricidad", "Invisibilidad"],
    "Nivel de Poder": [8, 6, 9, 7],
    "Ciudad": ["Central City", "Atlantis", "Neo Tokyo", "Gotham"]
}

df = pd.DataFrame(data)
print(df)

# Encuentra al superhéroe más poderoso
super_poderoso = df.loc[df["Nivel de Poder"].idxmax()]
print("\nEl más poderoso es:", super_poderoso["Nombre"])
