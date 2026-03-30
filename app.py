import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Evaluación Sistema MEAL", page_icon="📊", layout="centered")

# --- ENCABEZADO Y LOGO ---
try:
    st.image("Logo.png", width=250)
except:
    st.info("Sistema de Monitoreo y Evaluación")

st.title("Sistema Web MEAL")
st.subheader("Registro de Capacitación Técnica")

# --- INICIO DEL FORMULARIO ---
with st.form("evaluacion_meal"):
    st.info("📝 Escriba sus nombres y apellidos")
    col_nom, col_ape = st.columns(2)
    nombre = col_nom.text_input("Nombres:", placeholder="Ej. Juan Carlos")
    apellido = col_ape.text_input("Apellidos:", placeholder="Ej. Pérez")
    
    st.markdown("---")
    
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

    submit = st.form_submit_button("🚀 Finalizar Evaluación")

# --- MOSTRAR RESULTADOS AL USUARIO ---
if submit:
    if not nombre or not apellido or p1 is None or p2 is None or not p3 or p4 is None:
        st.error("❌ Por favor, ingresa tu nombre completo y responde todas las preguntas.")
    else:
        st.header(f"📝 Resultados para: {nombre} {apellido}")
        err = 0
        
        # Validación P1
        if p1 == "👥 Beneficiario: personas o sujetos / 🏗️ Ejecución: avance físico de actividades.":
            st.success("Pregunta 1: Correcta ✅")
        else:
            st.error("Pregunta 1: Incorrecta ❌")
            err += 1
            
        # Validación P2
        if p2 == "🚫 No, el sistema exige cargar evidencia técnica (fotos, actas, listas).":
            st.success("Pregunta 2: Correcta ✅")
        else:
            st.error("Pregunta 2: Incorrecta ❌")
            err += 1

        # Validación P3
        obligatorios = {"Tipo de documento", "Número de documento", "Nombres", "Apellidos", "Fecha de nacimiento", "Sexo", "Género", "Etnia", "Nacionalidad"}
        if set(p3) == obligatorios:
            st.success("Pregunta 3: Correcta ✅")
        else:
            st.error("Pregunta 3: Incorrecta ❌ (Revisa los campos obligatorios)")
            err += 1

        # Validación P4
        if p4 == "👨‍👩‍👧 Nombre y Apellido del apoderado.":
            st.success("Pregunta 4: Correcta ✅")
        else:
            st.error("Pregunta 4: Incorrecta ❌")
            err += 1

        # Mensaje Final Personalizado
        st.markdown("---")
        total_aciertos = 4 - err
        if err == 0:
            st.balloons()
            st.success(f"¡Excelente trabajo, {nombre}! Has aprobado la capacitación con 4/4 aciertos.")
        else:
            st.warning(f"{nombre}, has finalizado la evaluación con {total_aciertos} de 4 aciertos. Por favor, repasa los puntos marcados en rojo.")
