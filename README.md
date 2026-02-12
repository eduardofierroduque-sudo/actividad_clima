<img width="1897" height="938" alt="image" src="https://github.com/user-attachments/assets/c196bd98-5588-417e-8a54-1648fdfbc788" />
<img width="1888" height="379" alt="image" src="https://github.com/user-attachments/assets/d9909472-4443-4367-9195-cbb3a916cf71" />



En lugar de que el programa muera tras darte una recomendación, lo envolví en un bucle infinito. Esto permite que el programa se mantenga "vivo" y regrese al inicio automáticamente después de cada consulta.
Como un bucle infinito puede ser molesto si no puedes detenerlo, añadí una pregunta de control al final. Si el usuario escribe algo distinto a "si", el comando break rompe el ciclo y cierra el programa de forma elegante.
Organicé todo dentro de una función llamada ejecutar_asistente().
Antes, el programa aceptaba cualquier número. Ahora, le pusimos "sentido común":
Si es imposible (> 42°C): El programa se detiene y te dice: "Oye, esto no tiene sentido". No intenta darte recomendaciones de ropa porque el dato es erróneo.
Si es extremo (> 35°C): El programa duda. Te da el consejo de ropa ligera, pero primero te lanza una advertencia para que confirmes si el termómetro no está fallando.


<img width="883" height="630" alt="image" src="https://github.com/user-attachments/assets/b2011885-d5ea-4562-b136-67e95b49454d" />

En el código original, se usaba float, lo que permitía temperaturas como 35.7. A petición tuya, ahora usamos int.
Esto hace que el programa sea más directo y trabaje con números redondos (25, 30, 40), que es como normalmente hablamos del clima en el día a día.
Se reorganizó el orden de las preguntas. El asistente ahora piensa así:
¿Es un número válido?
¿Es una temperatura lógica?
Si todo está bien, recién ahí te dice qué ropa ponerte.




