from tkinter import *
from interfaz_usuario import *
from validacion import *

def interfaz_ingresar():
    
    jugadores_y_puntos={}
    #---------------------------Funciones llamadas por la PRINCIPAL----------------#
    #___________________________BOTON INGRESAR__________________________#
    def permiso_ingreso():
        control()
        condicion=validar_ingreso(cuadroJugador.get(), cuadroClave.get())    
        if condicion:
            mensaje='Registrado'
            diccionario_jugadores()
               
        else:
            mensaje='No registrado'
        Permiso=Label(ingresoFrame,text=mensaje)
        Permiso.grid(row=3,column=1, padx=10,pady=10)
        Permiso.config(bg='#0B615E',fg='white')
    
    def control():
        Permiso=Label(ingresoFrame,text='\t\t')
        Permiso.grid(row=3,column=1, padx=10,pady=10)
        Permiso.config(bg='#0B615E',fg='white')
        
    def diccionario_jugadores():
        nombre_ingresado, clave_usuario = validar_registro(cuadroJugador.get(), cuadroClave.get(),cuadroClave.get())
        if 0<=len(jugadores_y_puntos.keys())<2 and nombre_ingresado=='ocupado':
            ingreso_jugadores(cuadroJugador.get(), jugadores_y_puntos)
            
        if len(jugadores_y_puntos.keys())==2:
            botonIngresar.grid_forget()
            botonJugar=Button(root, text='Comenzar',command=cerrar_interfaz)
            botonJugar.pack()
            botonJugar.config(bg="#0B615E",fg='white')
               
    def consulta():
        control()
        condicion=validar_ingreso(cuadroJugador.get(), cuadroClave.get())    
        if condicion:
            mensaje='Registrado'
               
        else:
            mensaje='No registrado'
        Permiso=Label(ingresoFrame,text=mensaje)
        Permiso.grid(row=3,column=1, padx=10,pady=10)
        Permiso.config(bg='#0B615E',fg='white') 
    
    def cerrar_interfaz():
        root.destroy()
        
    #___________________________BOTON REGISTRAR-Principal__________________________#    
    def interfaz_registro():
        #___________________________BOTON VOLVER A INGRESO-Secundario__________________________#
        def cerrar_ventana():
            root.deiconify()  
            root_registro.destroy()  
        #___________________________BOTON REGISTRAR-Secundario__________________________#
        def registrar_jugador():
            par_condicion=validar_registro(cuadroJugador_registro.get(),cuadroClave_registro.get(),cuadroConfirmacion.get())
            estado_registro(par_condicion,cuadroJugador_registro.get(),cuadroClave_registro.get(),cuadroConfirmacion.get())   
                   
        def estado_registro(par_condicion,nombre, clave, confirmacion_clave):
            control_ventana()
            if par_condicion[0]=='invalido':
                if par_condicion[1]=='invalido':
                    informacion='Nombre y contraseña inválidas.'
                    
                elif par_condicion[1]=='valido':
                    informacion='Nombre inválido.'
                    
            elif par_condicion[0]=='valido':
                if par_condicion[1]=='valido':
                    informacion='Jugador registrado correctamente.'
                    cargar_jugador(nombre, clave)
                    
                elif par_condicion[1]=='invalido' and clave != confirmacion_clave:
                    informacion='No coindicen las claves ingresadas.'
                    
                elif par_condicion[1]=='invalido':
                    informacion='Contraseña inválida.'
                                        
            else:
                informacion='Usuario no disponible.'
            
            info=Label(ingreso_registro,text=informacion)
            info.grid(row=4,column=1,padx=10,pady=10)
            info.config(bg='#0B615E',fg='white') 
                    
        def control_ventana():   
            info=Label(ingreso_registro,text='\t\t\t\t')
            info.grid(row=4,column=1,padx=10,pady=10)
            info.config(bg='#0B615E',fg='white')
        
        root.withdraw()
        #_____________________Ventana Secundaria______________________________#
        root_registro=Toplevel(root)
        root_registro.title('Registro FIUBLE')
        root_registro.resizable(0,0)
        root_registro.geometry("500x280")
        root_registro.config(bg = "#088A85")   
        root_registro.iconbitmap("icono.ico")
        #---------------------Frames---------------------------#
        ingreso_registro=Frame(root_registro)
        ingreso_registro.pack(padx = "50", pady="30")
        ingreso_registro.config(bg="#0B615E")
        #---------------------Etiquetas---------------------------#
        jugador_registro=Label(ingreso_registro, text='Usuario:')
        jugador_registro.grid(row=1,column=0, padx=10,pady=10)
        jugador_registro.config(bg='#0B615E',fg='white')

        clave_registro=Label(ingreso_registro, text="Contraseña:")
        clave_registro.grid(row=2,column=0, padx=10,pady=10)
        clave_registro.config(bg='#0B615E',fg='white')

        confirmacion_clave=Label(ingreso_registro, text="Reingrese contraseña:")
        confirmacion_clave.grid(row=3,column=0,sticky="e", padx=10,pady=10)
        confirmacion_clave.config(bg='#0B615E',fg='white')
        
        situacionLabel=Label(ingreso_registro, text="Situacion del registro:")
        situacionLabel.grid(row=4,column=0,sticky="e", padx=10,pady=10)
        situacionLabel.config(bg='#0B615E',fg='white')                
        #---------------------Cuadros---------------------------#
        usuario=StringVar()
        cuadroJugador_registro=Entry(ingreso_registro,textvariable=usuario)
        cuadroJugador_registro.grid(row=1,column=1, padx=50,pady=10)

        password=StringVar()
        cuadroClave_registro=Entry(ingreso_registro,show="*",textvariable=password)
        cuadroClave_registro.grid(row=2,column=1, padx=50,pady=10)
        
        confirmacion_password=StringVar()
        cuadroConfirmacion=Entry(ingreso_registro,show="*",textvariable=confirmacion_password)
        cuadroConfirmacion.grid(row=3,column=1, padx=50,pady=10)
        #---------------------Botones---------------------------#    
        botonRegistro=Button(ingreso_registro, text='Registrar', command=registrar_jugador)
        botonRegistro.grid(row=5,column=1, padx=10,pady=10)
        botonRegistro.config(bg="#088A85",fg='white')
        
        botonRegresar=Button(ingreso_registro, text='Volver a Ingreso', command=cerrar_ventana)
        botonRegresar.grid(row=5,column=0, padx=10,pady=10)
        botonRegresar.config(bg="#088A85",fg='white')
        
#______________________________Ventana Principal___________________________________#
    root=Tk()
    root.title('Ingreso FIUBLE')
    root.resizable(0,0)
    root.geometry("450x280")
    root.config(bg = "#088A85")   
    root.iconbitmap("icono.ico")
    #---------------------Frames---------------------------#
    ingresoFrame=Frame(root)
    ingresoFrame.pack(padx = "30", pady="30")
    ingresoFrame.config(bg="#0B615E")
    #---------------------Etiquetas---------------------------#
    jugadorLabel=Label(ingresoFrame, text='Usuario:')
    jugadorLabel.grid(row=1,column=0, padx=20,pady=10)
    jugadorLabel.config(bg='#0B615E',fg='white')

    claveLabel=Label(ingresoFrame, text="Contraseña:")
    claveLabel.grid(row=2,column=0, padx=20,pady=10)
    claveLabel.config(bg='#0B615E',fg='white')

    nombre=StringVar()
    cuadroJugador=Entry(ingresoFrame,textvariable=nombre)
    cuadroJugador.grid(row=1,column=1, padx=30,pady=10)

    contrasenia=StringVar()
    cuadroClave=Entry(ingresoFrame,show="*",textvariable=contrasenia)
    cuadroClave.grid(row=2,column=1, padx=30,pady=10)
    #---------------------Botones---------------------------#    
    botonIngresar=Button(ingresoFrame, text='Ingresar',command=permiso_ingreso)
    botonIngresar.grid(row=4,column=1, padx=20,pady=10)
    botonIngresar.config(bg="#088A85",fg='white')
    
    botonConsulta=Button(ingresoFrame, text='Consulta registro',command=consulta)
    botonConsulta.grid(row=3,column=0, padx=20,pady=10)
    botonConsulta.config(bg="#088A85",fg='white')
    
    botonRegistrar=Button(ingresoFrame, text='Registrarse',command=interfaz_registro)
    botonRegistrar.grid(row=4,column=0, padx=10,pady=10)
    botonRegistrar.config(bg="#088A85",fg='white')
    
    root.mainloop()
    return jugadores_y_puntos

