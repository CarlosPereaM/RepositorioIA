class AnalizadorAnimo:
    def __init__(self):
        # Diccionario de preguntas organizadas por categoría
        self.preguntas = {
            'energia': [
                ('¿Cómo describirías tu nivel de energía hoy?', {
                    '1': ('Muy bajo, me cuesta hacer cualquier actividad', -2),
                    '2': ('Bajo, pero puedo realizar algunas tareas', -1),
                    '3': ('Normal, como siempre', 0),
                    '4': ('Bueno, me siento con energía', 1),
                    '5': ('Excelente, me siento muy energético', 2)
                }),
                ('¿Cómo fue tu sueño anoche?', {
                    '1': ('No pude dormir bien', -2),
                    '2': ('Dormí poco', -1),
                    '3': ('Normal', 0),
                    '4': ('Dormí bien', 1),
                    '5': ('Dormí excelente', 2)
                })
            ],
            'animo': [
                ('¿Cómo te sientes emocionalmente en este momento?', {
                    '1': ('Muy mal, me siento muy triste', -2),
                    '2': ('Algo triste o desanimado', -1),
                    '3': ('Normal, neutral', 0),
                    '4': ('Bien, positivo', 1),
                    '5': ('Muy bien, muy feliz', 2)
                }),
                ('¿Has experimentado cambios bruscos de humor hoy?', {
                    '1': ('Sí, muchos cambios negativos', -2),
                    '2': ('Algunos cambios de humor', -1),
                    '3': ('No realmente', 0),
                    '4': ('Me he sentido bastante estable', 1),
                    '5': ('Muy estable y positivo', 2)
                })
            ],
            'social': [
                ('¿Cómo te sientes respecto a tus interacciones sociales?', {
                    '1': ('Quiero evitar todo contacto social', -2),
                    '2': ('Prefiero estar solo', -1),
                    '3': ('Normal, como siempre', 0),
                    '4': ('Me siento sociable', 1),
                    '5': ('Muy sociable y comunicativo', 2)
                }),
                ('¿Cómo ha sido tu comunicación con otros hoy?', {
                    '1': ('No he querido hablar con nadie', -2),
                    '2': ('He hablado poco', -1),
                    '3': ('Normal', 0),
                    '4': ('Buena comunicación', 1),
                    '5': ('Excelente comunicación', 2)
                })
            ],
            'estres': [
                ('¿Qué nivel de estrés sientes?', {
                    '1': ('Muy estresado, me siento abrumado', -2),
                    '2': ('Algo estresado', -1),
                    '3': ('Normal', 0),
                    '4': ('Bastante tranquilo', 1),
                    '5': ('Muy relajado y en paz', 2)
                }),
                ('¿Cómo manejas tus responsabilidades hoy?', {
                    '1': ('Me siento incapaz de manejarlas', -2),
                    '2': ('Me cuesta un poco', -1),
                    '3': ('Normal', 0),
                    '4': ('Las manejo bien', 1),
                    '5': ('Las manejo excelentemente', 2)
                })
            ]
        }

        # Diccionario de recomendaciones según el estado de ánimo
        self.recomendaciones = {
            'muy_negativo': [
                "Considera hablar con un profesional de la salud mental",
                "Dedica tiempo a actividades que te hagan sentir bien",
                "Mantén contacto con seres queridos que te apoyen",
                "Realiza ejercicios de respiración y meditación",
                "Recuerda que está bien no estar bien y pedir ayuda"
            ],
            'negativo': [
                "Intenta hacer ejercicio suave como caminar",
                "Escucha música que te anime",
                "Habla con alguien de confianza sobre cómo te sientes",
                "Toma un descanso si lo necesitas",
                "Practica el autocuidado"
            ],
            'neutral': [
                "Mantén una rutina saludable",
                "Considera hacer algo nuevo hoy",
                "Dedica tiempo a un hobby",
                "Sal a tomar aire fresco",
                "Conéctate con amigos o familia"
            ],
            'positivo': [
                "¡Excelente! Mantén esas actividades que te hacen sentir bien",
                "Comparte tu energía positiva con otros",
                "Considera establecer nuevas metas",
                "Agradece por los buenos momentos",
                "Mantén el equilibrio en tus actividades"
            ],
            'muy_positivo': [
                "¡Fantástico! Aprovecha esta energía para proyectos importantes",
                "Comparte tu felicidad con los demás",
                "Registra qué te hace sentir así para futura referencia",
                "Mantén este impulso positivo con actividades productivas",
                "Celebra tus logros y buen estado de ánimo"
            ]
        }

    def hacer_pregunta(self, pregunta, opciones):
        while True:
            print(f"\n{pregunta}")
            for num, (texto, _) in opciones.items():
                print(f"{num}. {texto}")
            
            respuesta = input("\nSeleccione una opción (1-5): ").strip()
            if respuesta in opciones:
                return opciones[respuesta][1]
            print("Por favor, seleccione una opción válida (1-5)")

    def obtener_categoria_animo(self, puntaje_total):
        if puntaje_total <= -12:
            return 'muy_negativo'
        elif puntaje_total <= -4:
            return 'negativo'
        elif puntaje_total <= 4:
            return 'neutral'
        elif puntaje_total <= 12:
            return 'positivo'
        else:
            return 'muy_positivo'

    def obtener_emoji_animo(self, categoria):
        emojis = {
            'muy_negativo': '😢',
            'negativo': '😕',
            'neutral': '😐',
            'positivo': '😊',
            'muy_positivo': '😃'
        }
        return emojis.get(categoria, '😐')

    def analizar(self):
        print("\n=== Analizador de Estado de Ánimo ===")
        print("\nPor favor, responde las siguientes preguntas con honestidad.")
        print("Tus respuestas nos ayudarán a entender mejor cómo te sientes.")

        puntajes_categorias = {}
        puntaje_total = 0

        for categoria, preguntas in self.preguntas.items():
            puntaje_categoria = 0
            print(f"\n--- Preguntas sobre {categoria.title()} ---")
            for pregunta, opciones in preguntas:
                puntaje = self.hacer_pregunta(pregunta, opciones)
                puntaje_categoria += puntaje
                puntaje_total += puntaje
            puntajes_categorias[categoria] = puntaje_categoria

        # Análisis de resultados
        categoria_animo = self.obtener_categoria_animo(puntaje_total)
        emoji = self.obtener_emoji_animo(categoria_animo)

        # Mostrar resultados
        print("\n=== Resultados del Análisis ===")
        print(f"\nEstado de ánimo general: {categoria_animo.replace('_', ' ').title()} {emoji}")
        
        print("\nDesglose por categorías:")
        for categoria, puntaje in puntajes_categorias.items():
            nivel = "Bajo" if puntaje < 0 else "Normal" if puntaje == 0 else "Alto"
            print(f"- {categoria.title()}: {nivel}")

        print("\nRecomendaciones personalizadas:")
        for i, recomendacion in enumerate(self.recomendaciones[categoria_animo], 1):
            print(f"{i}. {recomendacion}")

        # Mensaje final
        if categoria_animo in ['muy_negativo', 'negativo']:
            print("\nNota: Si te sientes constantemente mal, considera buscar ayuda profesional.")
            print("Recuerda que no estás solo/a y que buscar ayuda es un signo de fortaleza.")
        
        return categoria_animo

if __name__ == "__main__":
    analizador = AnalizadorAnimo()
    resultado = analizador.analizar()