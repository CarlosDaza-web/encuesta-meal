import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Evaluación Sistema MEAL", page_icon="📊", layout="centered")

# --- ENCABEZADO Y LOGO ---
# Nota: Usa una URL directa a tu logo (que termine en .png o .jpg)
st.image("Logo.png", width=250) 
st.title("Sistema Web MEAL")
st.write("Capacitación Técnica")
st.info("⚠️ Responde todas las preguntas para procesar tu evaluación.")

# --- FORMULARIO ---
with st.form("evaluacion_meal"):
    # Pregunta 1
    p1 = st.radio("1. ¿Cuál es la diferencia entre el botón Beneficiario y Ejecución?", 
        ["👥 Beneficiario: personas o sujetos / 🏗️ Ejecución: avance físico de actividades.", 
         "💰 Beneficiario: presupuesto / 📋 Ejecución: listado de nombres.", 
         "🔄 No existe diferencia entre ambos."], index=None)
    
    # Pregunta 2
    p2 = st.radio("2. ¿Se puede reportar sin fuentes de verificación?", 
        ["✅ Sí, se pueden subir después al cierre del mes.", 
         "🚫 No, el sistema exige cargar evidencia técnica (fotos, actas, listas).", 
         "📧 Solo con autorización del coordinador."], index=None)
    
    # Pregunta 3
    op_p3 = ["Tipo de documento", "Número de documento", "Nombres", "Apellidos", "Fecha de nacimiento", "Sexo", "Género", "Etnia", "Nacionalidad", "Correo", "Teléfono", "Dirección"]
    p3 = st.multiselect("3. Seleccione los campos OBLIGATORIOS para mayores de edad:", op_p3)
    
    # Pregunta 4
    p4 = st.radio("4. ¿Cuál es la información adicional obligatoria para NNA (Menores)?", 
        ["🆔 Solo el número de cédula del menor.", 
         "👨‍👩‍👧 Nombre y Apellido del apoderado.", 
         "🏫 Nombre de la escuela.", 
         "📝 Declaración de ingresos."], index=None)

    submit = st.form_submit_button("🚀 Enviar Evaluación")

# --- VALIDACIÓN ---
if submit:
    if p1 is None or p2 is None or not p3 or p4 is None:
        st.error("❌ Por favor, completa todas las preguntas antes de enviar.")
    else:
        st.header("📝 Resultados de la Evaluación")
        err = 0
        
        if p1 == "👥 Beneficiario: personas o sujetos / 🏗️ Ejecución: avance físico de actividades.":
            st.success("Pregunta 1: Correcta ✅")
        else:
            st.error("Pregunta 1: Incorrecta ❌")
            err += 1
            
        if p2 == "🚫 No, el sistema exige cargar evidencia técnica (fotos, actas, listas).":
            st.success("Pregunta 2: Correcta ✅")
        else:
            st.error("Pregunta 2: Incorrecta ❌")
            err += 1

        obligatorios = {"Tipo de documento", "Número de documento", "Nombres", "Apellidos", "Fecha de nacimiento", "Sexo", "Género", "Etnia", "Nacionalidad"}
        if set(p3) == obligatorios:
            st.success("Pregunta 3: Correcta ✅")
        else:
            st.error("Pregunta 3: Incorrecta ❌ (Faltan campos obligatorios)")
            err += 1

        if p4 == "👨‍👩‍👧 Nombre y Apellido del apoderado.":
            st.success("Pregunta 4: Correcta ✅")
        else:
            st.error("Pregunta 4: Incorrecta ❌")
            err += 1

        if err == 0:
            st.balloons()
            st.success("¡Excelente! Has aprobado con 100%.")
        else:
            st.warning(f"Evaluación terminada con {err} error(es).")
