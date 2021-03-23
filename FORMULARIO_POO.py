import tkinter   # importando el paquete grafico tkinter
from tkinter import messagebox   # importando el modulo messagebox para mostrar mensajes en ventanas

class Formulario(tkinter.Frame): # hereda de la clase frame=ventana del paquete tkinter

    def __init__(self):  # constructor que inicializa la ventana al empezar el programa
        ventana = tkinter.Tk() # creando la ventana
        super().__init__(ventana) # utilizando las propiedad de la clase padre tkinter.Frame
        ventana.title("login") # titulo de la ventana
        ventana.geometry("400x200") # dimensiones de la ventana
        #-------------etiquetas------------------------------------
        lbl_usuario=tkinter.Label(ventana,text="Usuario:cesarmoza")
        lbl_usuario.place(x=80,y=30)

        lbl_contrasena = tkinter.Label(ventana, text="Clave:123")
        lbl_contrasena.place(x=80, y=60)
        #-------------------------caja de texto------------------------
        self.txtn1=tkinter.Entry(ventana,width=20)
        self.txtn1.place(x=200,y=30)

        self.txtn2=tkinter.Entry(ventana,width=20)
        self.txtn2.place(x=200,y=60)




        #------------------------botones-------------------------------------
        btncalcular=tkinter.Button(ventana, text="Entrar", command=self.grafica_ventana)
        btncalcular.place(x=250,y=100)

        # self.areatexto=tkinter.Text(ventana)
        # self.areatexto.config(width=50,height=10)
        # self.areatexto.place(x=100,y=150)


    def grafica_ventana(self):
        usuario=self.txtn1.get()
        contrasena=self.txtn2.get()

        #----------------validando entradas----------------------------------
        if( usuario==""):
            messagebox.showinfo(message="Ingrese usuario",title="Mensaje")
            self.txtn1.focus()
        elif(contrasena==""):
            messagebox.showinfo(message="Ingrese  contraseña", title="Mensaje")
            self.txtn2.focus()
        elif (usuario == "cesarmoza" and contrasena == "123"):
            ventana_principal=tkinter.Tk()
            ventana_principal.title("Ventana Principal")
            ventana_principal.geometry("400x200")

#------------------creando menu de la barra superioro--------------------
            menubar=tkinter.Menu(ventana_principal)

# ------------------creando submenu1-------------------------------------
            sub_menu1=tkinter.Menu(menubar, tearoff=0)
            sub_menu1.add_command(label="archivo1") # primera pestaña del elemento menu :archivo
            sub_menu1.add_separator()
            sub_menu1.add_command(label="archivo2")# segunda pestaña del elemento menu :archivo
            sub_menu1.add_separator()
# ------------------creando submenu2---------------------------------------
            sub_menu2 = tkinter.Menu(menubar, tearoff=0)
            sub_menu2.add_command(label="consulta1")
            sub_menu2.add_separator()
            sub_menu2.add_command(label="consulta2")
            sub_menu2.add_separator()
# ------------------creando submenu3---------------------------------------
            sub_menu3 = tkinter.Menu(menubar, tearoff=0)
            sub_menu3.add_command(label="mantenimiento1")
            sub_menu3.add_separator()
            sub_menu3.add_command(label="mantenimiento2")
            sub_menu3.add_separator()

# ------------------creando menu de la barra superior --------------------------------------
            menubar.add_cascade(label="archivo",menu=sub_menu1) # agregando submenu1 al primer elemento del menu "archivo"
            menubar.add_cascade(label="consulta", menu=sub_menu2)# agregando submenu2 alsegundo elemento del menu "consulta"
            menubar.add_cascade(label="mantenimiento", menu=sub_menu3)# agregando submenu3 al tercer elemento del menu " mantenimiento"

            ventana_principal.config(menu=menubar) # agregando el menu a la ventana principal

        else:
            messagebox.showinfo(message="Usuario y/o contraseña incorrecta", title="Mensaje")
            self.txtn1.focus()



objeto=Formulario( )
objeto.mainloop()