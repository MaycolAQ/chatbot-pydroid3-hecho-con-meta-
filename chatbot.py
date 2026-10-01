# Chatbot Pydroid3 - Hecho en Arequipa
import random

respuestas = {
    "hola": ["¡Hola! 👋 ¿Qué tal?", "¡Hey! ¿Cómo vas?", "Hola! 😊"],
    "como estas": ["¡Bien! ¿Y tú?", "Todo bien por aquí 🔥"],
    "tu nombre": ["Soy tu chatbot hecho en Pydroid3", "Me llamo Bot-Pydroid 🤖"],
    "chiste": ["¿Qué hace una abeja en el gym? ¡Zum-ba! 🐝", "¿Por qué el libro fue al doctor? Porque tenía muchas hojas rotas 📚"],
    "adios": ["¡Chao! ¡Nos vemos! 👋", "¡Hasta luego!"]
}

print("🤖 Bot: ¡Hola! Escribe 'adios' para salir")
print("Tip: enseña : palabra : respuesta -> para enseñarme")

while True:
    msg = input("Tú: ").lower().strip()

    if msg == "adios":
        print("🤖 Bot:", random.choice(respuestas["adios"]))
        break

    # Para enseñarle cosas nuevas
    if msg.startswith("enseña"):
        try:
            _, clave, valor = msg.split(":", 2)
            clave = clave.strip()
            valor = valor.strip()
            if clave in respuestas:
                respuestas[clave].append(valor)
            else:
                respuestas[clave] = [valor]
            print(f"🤖 Bot: ¡Aprendido! Cuando digas '{clave}' diré '{valor}'")
        except:
            print("🤖 Bot: Usa así -> enseña : hola : que tal pe")
        continue

    # Buscar respuesta
    encontrado = False
    for clave in respuestas:
        if clave in msg:
            print("🤖 Bot:", random.choice(respuestas[clave]))
            encontrado = True
            break

    if not encontrado:
        print("🤖 Bot: No entiendo 🤔. Enséñame con: enseña : tu frase : mi respuesta")
