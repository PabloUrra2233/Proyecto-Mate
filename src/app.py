import customtkinter as ctk
from tkinter import messagebox

# from src.graph_manager import cargar_grafo_desde_csv
# from src.shortest_path import calcular_camino_mas_corto
# from src.visualization import visualizar_grafo


# Configuración básica de la apariencia
ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")  

class AppRutaOptima(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.title("Calculadora de Ruta Óptima - Matemática Discreta")
        self.geometry("600x500")
        
        # Variables de estado (Aquí guardaremos los datos seleccionados)
        self.origen_var = ctk.StringVar(value="Seleccionar Origen")
        self.destino_var = ctk.StringVar(value="Seleccionar Destino")
        
        # Lista temporal (hasta que el Compañero 2 entregue el CSV)
        self.ciudades_mock = ["Tokio", "París", "Nueva York", "Londres", "Sídney", "Berlín"]

        self._build_ui()

    def _build_ui(self):
        """Construye y posiciona todos los elementos visuales de la interfaz."""
        
        # Título
        self.lbl_titulo = ctk.CTkLabel(self, text="Ruta Óptima entre Ciudades", font=ctk.CTkFont(size=24, weight="bold"))
        self.lbl_titulo.pack(pady=(20, 30))

        # Contenedor para los selectores
        self.frame_selectores = ctk.CTkFrame(self)
        self.frame_selectores.pack(pady=10, padx=20, fill="x")

        # Selector de Origen
        self.lbl_origen = ctk.CTkLabel(self.frame_selectores, text="Ciudad de Origen:")
        self.lbl_origen.grid(row=0, column=0, padx=20, pady=10, sticky="w")
        self.combo_origen = ctk.CTkComboBox(self.frame_selectores, variable=self.origen_var, values=self.ciudades_mock)
        self.combo_origen.grid(row=0, column=1, padx=20, pady=10, sticky="e")

        # Selector de Destino
        self.lbl_destino = ctk.CTkLabel(self.frame_selectores, text="Ciudad de Destino:")
        self.lbl_destino.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        self.combo_destino = ctk.CTkComboBox(self.frame_selectores, variable=self.destino_var, values=self.ciudades_mock)
        self.combo_destino.grid(row=1, column=1, padx=20, pady=10, sticky="e")

        # Botón de Cálculo
        self.btn_calcular = ctk.CTkButton(self, text="Calcular Ruta Óptima", command=self._on_calcular_click)
        self.btn_calcular.pack(pady=20)

        # Contenedor para Resultados
        self.frame_resultados = ctk.CTkFrame(self)
        self.frame_resultados.pack(pady=10, padx=20, fill="both", expand=True)

        self.lbl_resultado_titulo = ctk.CTkLabel(self.frame_resultados, text="Resultados:", font=ctk.CTkFont(weight="bold"))
        self.lbl_resultado_titulo.pack(pady=(10, 5))

        self.txt_resultados = ctk.CTkTextbox(self.frame_resultados, height=100)
        self.txt_resultados.pack(padx=10, pady=10, fill="both", expand=True)
        self.txt_resultados.insert("0.0", "Esperando consulta...\n")
        self.txt_resultados.configure(state="disabled") 

        # Botón para Visualizar Grafo (Se conectará con la parte del Compañero 4)
        self.btn_visualizar = ctk.CTkButton(self, text="Ver Grafo de Conexiones", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.btn_visualizar.pack(pady=(0, 20))

    def _on_calcular_click(self):
        """Maneja el evento de presionar el botón de cálculo."""
        origen = self.origen_var.get()
        destino = self.destino_var.get()

        # Validaciones tempranas (Clean Code: Fail Fast)
        if origen == "Seleccionar Origen" or destino == "Seleccionar Destino":
            messagebox.showwarning("Advertencia", "Por favor, selecciona un origen y un destino.")
            return
        
        if origen == destino:
            messagebox.showinfo("Aviso", "El origen y el destino son la misma ciudad.")
            return

        # función de Pablo en shortest_path.py
        # costo, ruta = calculate_shortest_path(origen, destino)
        
        # para probar si anda la interfaz:
        ruta_falsa = f"{origen} -> Ciudad Intermedia -> {destino}"
        costo_falso = 1450.5 

        self._mostrar_resultados(ruta_falsa, costo_falso)

    def _mostrar_resultados(self, ruta, costo):
        """Actualiza la caja de texto con los resultados obtenidos."""
        self.txt_resultados.configure(state="normal")
        self.txt_resultados.delete("0.0", "end")
        
        mensaje = f"Ruta Óptima:\n{ruta}\n\nCosto Total (Distancia):\n{costo} km"
        self.txt_resultados.insert("0.0", mensaje)
        
        self.txt_resultados.configure(state="disabled")

if __name__ == "__main__":
    app = AppRutaOptima()
    app.mainloop()