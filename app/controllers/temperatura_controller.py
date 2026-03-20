from app.database import get_connection

# 🔹 INSERT
def guardar_temperatura(valor: float):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO temperaturas (valor) VALUES (%s)",
        (valor,)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return {"mensaje": "Guardado en DB", "valor": valor}


# 🔹 SELECT
def obtener_datos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, valor FROM temperaturas")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    datos = [{"id": r[0], "valor": r[1]} for r in rows]

    rata = [3,4,23,32]
    for i in range(len(rata) - 1):
        for j in range(i + 1, len(rata)):
            if rata[i] < rata[j]:
                aux = rata[i]
                rata[i] = rata[j]
                rata[j] = aux
    return {
        "datos": datos,rata
    }
