import streamlit as st
import requests
streamlit
requests

st.set_page_config(page_title="Evaluación Sistema MEAL", page_icon="📊", layout="centered")

# --- CONFIGURACIÓN DE RECEPCIÓN DE DATOS ---
# Reemplaza con tu correo institucional o personal
MI_CORREO = "cadf_98@hotmail.com" 
URL_FORM_SUBMIT = f"https://formsubmit.co/ajax/{MI_CORREO}"

# --- ENCABEZADO Y LOGO ---
st.image("Logo.png", width=250) 
st.title("Sistema Web MEAL")
st.subheader("Registro de Capacitación")

with st.form("evaluacion_meal"):
    st.info("📝 Identificación")
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

    submit = st.form_submit_button("🚀 Enviar Evaluación")

if submit:
    if not nombre or not apellido or p1 is None or p2 is None or not p3 or p4 is None:
        st.error("❌ Por favor, completa tu nombre y todas las preguntas.")
    else:
        # --- CÁLCULO DE RESULTADOS ---
        resultados = []
        p1_ok = (p1 == "👥 Beneficiario: personas o sujetos / 🏗️ Ejecución: avance físico de actividades.")
        p2_ok = (p2 == "🚫 No, el sistema exige cargar evidencia técnica (fotos, actas, listas).")
        
        obligatorios = {"Tipo de documento", "Número de documento", "Nombres", "Apellidos", "Fecha de nacimiento", "Sexo", "Género", "Etnia", "Nacionalidad"}
        p3_ok = (set(p3) == obligatorios)
        p4_ok = (p4 == "👨‍👩‍👧 Nombre y Apellido del apoderado.")

        total_aciertos = sum([p1_ok, p2_ok, p3_ok, p4_ok])
        
        # --- ENVÍO DE DATOS AL CORREO ---
        datos_envio = {
            "Especialista": f"{nombre} {apellido}",
            "Nota": f"{total_aciertos}/4",
            "P1_Diferencia": "Correcta" if p1_ok else "Incorrecta",
            "P2_Evidencia": "Correcta" if p2_ok else "Incorrecta",
            "P3_Obligatorios": "Correcta" if p3_ok else "Incorrecta",
            "P4_NNA": "Correcta" if p4_ok else "Incorrecta"
        }
        
        try:
            resp = requests.post(URL_FORM_SUBMIT, json=datos_envio)
            if resp.status_code == 200:
                st.success(f"✅ ¡Gracias {nombre}! Tu evaluación ha sido enviada con éxito.")
                if total_aciertos == 4: st.balloons()
            else:
                st.warning("⚠️ Los resultados se muestran pero no se pudieron enviar al servidor.")
        except:
            st.error("Error de conexión al enviar resultados.")

        # Mostrar resumen al técnico
        st.write(f"**Tu calificación final: {total_aciertos} de 4**")
