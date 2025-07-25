import os

def generate_invitations(template, attendees):
    # Verificación de tipo del template
    if not isinstance(template, str):
        print("Error: El template debe ser una cadena de texto (str).")
        return

    # Verificación de tipo del attendees
    if not isinstance(attendees, list) or not all(isinstance(att, dict) for att in attendees):
        print("Error: attendees debe ser una lista de diccionarios.")
        return

    # Verificación de template vacío
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Verificación de lista vacía
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Procesamiento de cada asistente
    for index, person in enumerate(attendees, start=1):
        filled_template = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = person.get(key, "N/A")
            if value is None:
                value = "N/A"
            filled_template = filled_template.replace(f"{{{key}}}", value)

        # Escribir a archivo
        filename = f"output_{index}.txt"
        try:
            with open(filename, 'w') as f:
                f.write(filled_template)
        except Exception as e:
            print(f"Error writing to file {filename}: {e}")
