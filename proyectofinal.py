import tkinter as tk
import sympy as sp
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from funciones import *

root = tk.Tk()
root.geometry('1200x1000')
root.title('Análisis Númerico')

def home_page():
    home_frame = tk.Frame(main_frame, bg="light cyan")
    lb = tk.Label(home_frame, text='Bienvenido al curso de Análisis Númerico', font=('Great vibes', 38), bg='Light cyan',fg = 'red')
    lb.pack(pady=80)
    msg = '''
    En este curso, explorarás los siguientes temas clave:
    - Series de Taylor
    - Ceros de funciones
    - Interpolación
    - Ecuaciones diferenciales

    Tendrás la oportunidad de aplicar y probar cada uno de estos métodos de manera interactiva.

    ¡Estamos emocionados de que te unas a nosotros en este fascinante viaje de descubrimiento y aprendizaje!
    '''
    lb1 = tk.Label(home_frame, text=msg, font=('Dancing Script', 14), bg='Light cyan')
    lb1.pack(pady=10)
    home_frame.pack(pady=20)

def insertar_operador(lb):
    funciones = {'e': 'exp()','sin':'sin()','cos':'cos()'}
    contenido_actual = entry_funcion.get()  # Obtener el contenido actual del Entry
    nuevo_contenido = contenido_actual + funciones[lb]
    entry_funcion.delete(0, tk.END)  # Limpiar el contenido actual del Entry
    entry_funcion.insert(tk.END, nuevo_contenido)

def obtener_datos():
    f = entry_funcion.get()
    f = sp.sympify(f)
    punto = entry_point.get()
    punto = int(punto)
    grade = entry_grade.get()
    grade = int(grade)
    poli = taylor(f,punto,grade)
    entry_solution_taylor.delete(0, tk.END)  # Limpiar el contenido actual del Entry
    entry_solution_taylor.insert(tk.END, poli)

def taylor_page():
    global entry_funcion
    global entry_point
    global entry_grade
    global entry_solution_taylor
    taylor_frame = tk.Frame(main_frame, bg="light cyan")
    lb = tk.Label(taylor_frame, text='Método de Taylor', font=('Bold', 40), bg='Light cyan')
    lb.pack()

    lb1 = tk.Label(taylor_frame, text='Este método te permite aproximar un polinomio del grado que tu desees a una función dada alrededor de un punto \n\n para ejecutar este método inserte la función en el recuadro, seleccione el grado al cual lo va aproximar e ingrese el punto', font=('Arial', 12), bg='Light cyan')
    lb1.pack(pady=10)

    entry_funcion_frame = tk.Frame(taylor_frame, bg="light cyan")
    lb_insert_funcion = tk.Label(entry_funcion_frame, text='Inserte la función:', font=('Arial', 12), bg='light cyan')
    lb_insert_funcion.pack(side=tk.LEFT, padx=(0, 5))

    entry_funcion = tk.Entry(entry_funcion_frame, font=('Arial', 12), width=60)
    entry_funcion.pack(side=tk.LEFT)

    entry_funcion_frame.pack(pady=5)

    buttons_frame = tk.Frame(taylor_frame, bg="light cyan")
    exp_btn = tk.Button(buttons_frame, text="e", font=('Bold', 12), fg='blue4', bd=5, bg='#c3c3c3', command=lambda: insertar_operador('e'))
    exp_btn.pack(side=tk.LEFT, padx=(0, 5))

    sin_btn = tk.Button(buttons_frame, text="Sin", font=('Bold', 12), fg='blue4', bd=5, bg='#c3c3c3', command=lambda: insertar_operador('sin'))
    sin_btn.pack(side=tk.LEFT)

    cos_btn = tk.Button(buttons_frame, text="Cos", font=('Bold', 12), fg='blue4', bd=5, bg='#c3c3c3', command=lambda: insertar_operador('cos'))
    cos_btn.pack(side=tk.LEFT)

    buttons_frame.pack(pady=5)

    entry_grade_frame = tk.Frame(taylor_frame, bg="light cyan")
    lb_insert_grade = tk.Label(entry_grade_frame, text='Inserte el grado:', font=('Arial', 12), bg='light cyan')
    lb_insert_grade.pack(side=tk.LEFT, padx=(0, 5))

    entry_grade = tk.Entry(entry_grade_frame, font=('Arial', 12), width=30)
    entry_grade.pack(side=tk.LEFT)

    entry_grade_frame.pack(pady=5)

    entry_point_frame = tk.Frame(taylor_frame, bg="light cyan")
    lb_insert_point = tk.Label(entry_point_frame, text='Inserte el punto:', font=('Arial', 12), bg='light cyan')
    lb_insert_point.pack(side=tk.LEFT, padx=(0, 5))

    entry_point = tk.Entry(entry_point_frame, font=('Arial', 12), width=30)
    entry_point.pack(side=tk.LEFT)

    entry_point_frame.pack(pady=5)

    execute_btn = tk.Button(taylor_frame, text="Ejecutar", font=('Bold', 15), fg='red', bd=5, bg='#c3c3c3',command= lambda : obtener_datos())
    execute_btn.pack(pady=10)

    solution_taylor_frame = tk.Frame(taylor_frame, bg="light cyan")
    lb_solution = tk.Label(solution_taylor_frame, text='Solución', font=('Bold', 30), bg='Light cyan',fg='red')
    lb_solution.pack()

    lb_enunciado_solution = tk.Label(solution_taylor_frame, text='El polinomio aproximado a la función dada es:', font=('Arial', 12), bg='Light cyan')
    lb_enunciado_solution.pack(pady=10)

    entry_solution_frame = tk.Frame(solution_taylor_frame, bg="light cyan")
    entry_solution_taylor = tk.Entry(entry_solution_frame, font=('Arial', 12), width=60)
    entry_solution_taylor.pack(side=tk.LEFT)

    entry_solution_frame.pack(pady=5)
    solution_taylor_frame.pack(pady=20)

    grafica_btn = tk.Button(solution_taylor_frame, text="Ver gráfica", font=('Bold', 15), fg='red', bd=5, bg='#c3c3c3',command=lambda: indicate_grafica_taylor(taylor_indicate,grafica_taylor_page,entry_solution_taylor.get()))
    grafica_btn.pack(pady=10)

    taylor_frame.pack(pady=20)


def grafica_taylor_page(funcion):
    grafica_taylor_frame = tk.Frame(main_frame, bg="light cyan")
    lb = tk.Label(grafica_taylor_frame, text='Gráfica', font=('Bold', 40), bg='Light cyan')
    lb.pack()

    # Crear una figura de Matplotlib
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)

    # Convertir la función simbólica a una función lambda
    x = np.linspace(0,1, 100)
    y = funcion
    funcion = lambda x: eval(y)
    
    # Graficar la función
    ax.plot(x, funcion(x), label='Polinomio aproximado', color='blue')

    ax.legend()

    # Agregar cuadrícula
    ax.grid(True, linestyle='--', alpha=0.7)

    # Crear un lienzo de Matplotlib para Tkinter
    canvas = FigureCanvasTkAgg(fig, master=grafica_taylor_frame)
    canvas.draw()

    # Mostrar el lienzo en la interfaz gráfica
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    grafica_taylor_frame.pack(pady=20)

def insertar_operador_ceros(lb):
    funciones = {'tan': 'np.tan()','sin':'np.sin()','cos':'np.cos()'}
    contenido_actual = entry_funcion_ceros.get()  # Obtener el contenido actual del Entry
    nuevo_contenido = contenido_actual + funciones[lb]
    entry_funcion_ceros.delete(0, tk.END)  # Limpiar el contenido actual del Entry
    entry_funcion_ceros.insert(tk.END, nuevo_contenido)

def obtener_datos_newton(lb):
    y = entry_funcion_ceros.get()
    y = sp.sympify(y)
    punto_x0 = float(entry_x0.get())
    tol = float(entry_tol.get())
    raiz = lb(y,punto_x0,tol)
    entry_solution_ceros.delete(0, tk.END)  # Limpiar el contenido actual del Entry
    entry_solution_ceros.insert(tk.END, raiz)

def obtener_datos_ceros(lb):
    y = entry_funcion_ceros.get()
    f1 = lambda x: eval(y)
    punto_x0 = float(entry_x0.get())
    punto_x1 = float(entry_x1.get())
    tol = float(entry_tol.get())
    raiz = lb(f1,punto_x0,punto_x1,tol)
    entry_solution_ceros.delete(0, tk.END)  # Limpiar el contenido actual del Entry
    entry_solution_ceros.insert(tk.END, raiz)

def grafica_ceros_page(funcion, punto_i, punto_f,raiz):
    grafica_ceros_frame = tk.Frame(main_frame, bg="light cyan")
    lb = tk.Label(grafica_ceros_frame, text='Gráfica', font=('Bold', 40), bg='Light cyan')
    lb.pack()

    lb1 = tk.Label(grafica_ceros_frame, text=f"Raiz = {raiz}", font=('Bold', 20), bg='Light cyan')
    lb1.pack()
    
    # Crear una figura de Matplotlib
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)

    # Convertir la función simbólica a una función lambda
    x = np.linspace(float(punto_i), float(punto_f), 100)
    y = funcion
    funcion = lambda x: eval(y)
    
    # Graficar la función
    ax.plot(x, funcion(x), label='Función dada', color='blue')

    # Graficar los puntos iniciales y finales
    ax.scatter(float(punto_i), funcion(float(punto_i)), color='red', marker='o', label='Punto Inicial')
    ax.scatter(float(punto_f), funcion(float(punto_f)), color='green', marker='o', label='Punto Final')

    # Graficar la raíz
    ax.axvline(x=float(raiz), color='purple', linestyle='--', label='Raíz')

    ax.legend()

    # Agregar cuadrícula
    ax.grid(True, linestyle='--', alpha=0.7)

    # Crear un lienzo de Matplotlib para Tkinter
    canvas = FigureCanvasTkAgg(fig, master=grafica_ceros_frame)
    canvas.draw()

    # Mostrar el lienzo en la interfaz gráfica
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    
    grafica_ceros_frame.pack(pady=20)

def ceros_page():
    global entry_funcion_ceros
    global entry_x0
    global entry_x1
    global entry_tol
    global entry_solution_ceros 

    ceros_frame = tk.Frame(main_frame, bg="light cyan")
    lb = tk.Label(ceros_frame, text='Ceros', font=('Bold', 40), bg='Light cyan')
    lb.pack()

    lb1 = tk.Label(ceros_frame, text='Esta sección te permite hallar la raiz de una funcion por diferentes métodos, ingresa la función y selecciona el método', font=('Arial', 12), bg='Light cyan')
    lb1.pack(pady=10)

    entry_funcionceros_frame = tk.Frame(ceros_frame, bg="light cyan")
    lb_insert_funcion = tk.Label(entry_funcionceros_frame, text='Inserte la función:', font=('Arial', 12), bg='light cyan')
    lb_insert_funcion.pack(side=tk.LEFT, padx=(0, 5))

    entry_funcion_ceros = tk.Entry(entry_funcionceros_frame, font=('Arial', 12), width=60)
    entry_funcion_ceros.pack(side=tk.LEFT)

    entry_funcionceros_frame.pack(pady=5)

    buttons_frame = tk.Frame(ceros_frame, bg="light cyan")
    tan_btn = tk.Button(buttons_frame, text="tan", font=('Bold', 12), fg='blue4', bd=5, bg='#c3c3c3', command=lambda: insertar_operador_ceros('tan'))
    tan_btn.pack(side=tk.LEFT, padx=(0, 5))

    sin_btn = tk.Button(buttons_frame, text="Sin", font=('Bold', 12), fg='blue4', bd=5, bg='#c3c3c3', command=lambda: insertar_operador_ceros('sin'))
    sin_btn.pack(side=tk.LEFT)

    cos_btn = tk.Button(buttons_frame, text="Cos", font=('Bold', 12), fg='blue4', bd=5, bg='#c3c3c3', command=lambda: insertar_operador_ceros('cos'))
    cos_btn.pack(side=tk.LEFT)

    buttons_frame.pack(pady=5)

    entry_x0_frame = tk.Frame(ceros_frame, bg="light cyan")
    lb_insert_x0 = tk.Label(entry_x0_frame, text='Ingrese el punto inicial: ', font=('Arial', 12), bg='light cyan')
    lb_insert_x0.pack(side=tk.LEFT, padx=(0, 5))

    entry_x0 = tk.Entry(entry_x0_frame, font=('Arial', 12), width=30)
    entry_x0.pack(side=tk.LEFT)

    entry_x0_frame.pack(pady=5)

    entry_x1_frame = tk.Frame(ceros_frame, bg="light cyan")
    lb_insert_x0 = tk.Label(entry_x1_frame, text='Ingrese el punto final: ', font=('Arial', 12), bg='light cyan')
    lb_insert_x0.pack(side=tk.LEFT, padx=(0, 5))

    entry_x1 = tk.Entry(entry_x1_frame, font=('Arial', 12), width=30)
    entry_x1.pack(side=tk.LEFT)

    entry_x1_frame.pack(pady=5)

    entry_tol_frame = tk.Frame(ceros_frame, bg="light cyan")
    lb_insert_tol = tk.Label(entry_tol_frame, text='Ingrese la tolerancia: ', font=('Arial', 12), bg='light cyan')
    lb_insert_tol.pack(side=tk.LEFT, padx=(0, 5))

    entry_tol = tk.Entry(entry_tol_frame, font=('Arial', 12), width=30)
    entry_tol.pack(side=tk.LEFT)

    entry_tol_frame.pack(pady=5)

    lb2 = tk.Label(ceros_frame, text='En caso de que quiera resolverlo por el método de newton solo necesita un punto inicial', font=('Arial', 12), bg='Light cyan',fg='red')
    lb2.pack(pady=10)

    entry_method_frame = tk.Frame(ceros_frame, bg="light cyan")
    lb_insert_method = tk.Label(entry_method_frame, text='Eliga el método:', font=('Arial', 12), bg='light cyan')
    lb_insert_method.pack(side=tk.LEFT, padx=(0, 5))

    entry_method_frame.pack(pady=5)

    buttons_methods_frame = tk.Frame(ceros_frame, bg="light cyan")
    bis_btn = tk.Button(buttons_methods_frame, text="Bisección", font=('Bold', 12), fg='blue4', bd=5, bg='#c3c3c3', command=lambda: obtener_datos_ceros(Biseccion))
    bis_btn.pack(side=tk.LEFT, padx=(0, 5))

    pos_btn = tk.Button(buttons_methods_frame, text="Pos Falsa", font=('Bold', 12), fg='blue4', bd=5, bg='#c3c3c3', command=lambda: obtener_datos_ceros(Pos_falsa))
    pos_btn.pack(side=tk.LEFT)

    newton_btn = tk.Button(buttons_methods_frame, text="Newton", font=('Bold', 12), fg='blue4', bd=5, bg='#c3c3c3', command=lambda: obtener_datos_newton(Newton))
    newton_btn.pack(side=tk.LEFT)

    secante_btn = tk.Button(buttons_methods_frame, text="Secante", font=('Bold', 12), fg='blue4', bd=5, bg='#c3c3c3', command=lambda: obtener_datos_ceros(Secante))
    secante_btn.pack(side=tk.LEFT)

    buttons_methods_frame.pack(pady=5)

    solution_ceros_frame = tk.Frame(ceros_frame, bg="light cyan")
    lb_solution = tk.Label(solution_ceros_frame, text='Solución', font=('Bold', 30), bg='Light cyan',fg='red')
    lb_solution.pack()

    lb_enunciado_solution = tk.Label(solution_ceros_frame, text='la raíz de la función dada es:', font=('Arial', 12), bg='Light cyan')
    lb_enunciado_solution.pack(pady=10)

    entry_solution_frame = tk.Frame(solution_ceros_frame, bg="light cyan")
    entry_solution_ceros = tk.Entry(entry_solution_frame, font=('Arial', 12), width=60)
    entry_solution_ceros.pack(side=tk.LEFT)

    entry_solution_frame.pack(pady=5)
    solution_ceros_frame.pack(pady=20)

    grafica_btn = tk.Button(solution_ceros_frame, text="Ver gráfica", font=('Bold', 15), fg='red', bd=5, bg='#c3c3c3',command=lambda: indicate_grafica_ceros(ceros_indicate,grafica_ceros_page,entry_funcion_ceros.get(),entry_x0.get(),entry_x1.get(),entry_solution_ceros.get()))
    grafica_btn.pack(pady=10)

    ceros_frame.pack(pady=20)

def obtener_datos_interpolacion(lb):
    xd = entry_datax.get()
    xd_num = xd.split(',')
    xd_num = [float(numero) for numero in xd_num]
    yd = entry_datay.get()
    yd_num = yd.split(',')
    yd_num = [float(numero) for numero in yd_num]
    poli, f = lb(xd_num,yd_num)
    entry_solution_interpolacion.delete(0, tk.END)  # Limpiar el contenido actual del Entry
    entry_solution_interpolacion.insert(tk.END, poli)

def grafica_interpolacion_page(xd,yd):
    grafica_interpolacion_frame = tk.Frame(main_frame, bg="light cyan")
    lb = tk.Label(grafica_interpolacion_frame, text='Gráfica', font=('Bold', 40), bg='Light cyan')
    lb.pack()

    xd_num = xd.split(',')
    xd_num = [float(numero) for numero in xd_num]
    xd_num = np.array(xd_num)
    yd_num = yd.split(',')
    yd_num = [float(numero) for numero in yd_num]
    yd_num = np.array(yd_num)
    poli, f = p_simple(xd_num,yd_num)


    # Crear una figura de Matplotlib
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    
    # Convertir la función simbólica a una función lambda
    x = np.linspace(min(xd_num),max(xd_num), 100)
    
    # Graficar la función
    ax.plot(xd_num, yd_num, 'md',label='Datos Dados', color='blue')
    ax.plot(x, f(x), label='Polinomio', color='red')

    ax.legend()

    # Agregar cuadrícula
    ax.grid(True, linestyle='--', alpha=0.7)

    # Crear un lienzo de Matplotlib para Tkinter
    canvas = FigureCanvasTkAgg(fig, master=grafica_interpolacion_frame)
    canvas.draw()

    # Mostrar el lienzo en la interfaz gráfica
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    
    grafica_interpolacion_frame.pack(pady=20)

def interpolacion_page():
    global entry_datax
    global entry_datay
    global entry_solution_interpolacion
    interpolacion_frame = tk.Frame(main_frame, bg="light cyan")
    lb = tk.Label(interpolacion_frame, text='Interpolación', font=('Bold', 40), bg='Light cyan')
    lb.pack()

    lb1 = tk.Label(interpolacion_frame, text='Esta sección te permite hallar un polinomio que se aproxime atraves de dos conjuntos de datos dados', font=('Arial', 12), bg='Light cyan')
    lb1.pack(pady=10)

    entry_datax_frame = tk.Frame(interpolacion_frame, bg="light cyan")
    lb_insert_datax = tk.Label(entry_datax_frame, text='Inserte los datos x separados por coma:', font=('Arial', 12), bg='light cyan')
    lb_insert_datax.pack(side=tk.LEFT, padx=(0, 5))

    entry_datax = tk.Entry(entry_datax_frame, font=('Arial', 12), width=60)
    entry_datax.pack(side=tk.LEFT)

    entry_datax_frame.pack(pady=5)

    entry_datay_frame = tk.Frame(interpolacion_frame, bg="light cyan")
    lb_insert_datay = tk.Label(entry_datay_frame, text='Inserte los datos y separados por coma:', font=('Arial', 12), bg='light cyan')
    lb_insert_datay.pack(side=tk.LEFT, padx=(0, 5))

    entry_datay = tk.Entry(entry_datay_frame, font=('Arial', 12), width=60)
    entry_datay.pack(side=tk.LEFT)
    entry_datay_frame.pack(pady=5)

    entry_method_frame = tk.Frame(interpolacion_frame, bg="light cyan")
    lb_insert_method = tk.Label(entry_method_frame, text='Eliga el método:', font=('Arial', 12), bg='light cyan')
    lb_insert_method.pack(side=tk.LEFT, padx=(0, 5))

    entry_method_frame.pack(pady=5)

    buttons_methods_frame = tk.Frame(interpolacion_frame, bg="light cyan")
    pols_btn = tk.Button(buttons_methods_frame, text="Pol Simple", font=('Bold', 12), fg='blue4', bd=5, bg='#c3c3c3', command=lambda: obtener_datos_interpolacion(p_simple))
    pols_btn.pack(side=tk.LEFT, padx=(0, 5))

    lag_btn = tk.Button(buttons_methods_frame, text="Lagrange", font=('Bold', 12), fg='blue4', bd=5, bg='#c3c3c3', command=lambda: obtener_datos_interpolacion(lagrange))
    lag_btn.pack(side=tk.LEFT)

    buttons_methods_frame.pack(pady=5)

    solution_interpolacion_frame = tk.Frame(interpolacion_frame, bg="light cyan")
    lb_solution = tk.Label(solution_interpolacion_frame, text='Solución', font=('Bold', 30), bg='Light cyan',fg='red')
    lb_solution.pack()

    lb_enunciado_solution = tk.Label(solution_interpolacion_frame, text='El polinomio interpolante es:', font=('Arial', 12), bg='Light cyan')
    lb_enunciado_solution.pack(pady=10)

    entry_solution_frame = tk.Frame(solution_interpolacion_frame, bg="light cyan")
    entry_solution_interpolacion = tk.Entry(entry_solution_frame, font=('Arial', 12), width=120)
    entry_solution_interpolacion.pack(side=tk.LEFT)

    entry_solution_frame.pack(pady=5)
    solution_interpolacion_frame.pack(pady=20)

    grafica_btn = tk.Button(solution_interpolacion_frame, text="Ver gráfica", font=('Bold', 15), fg='red', bd=5, bg='#c3c3c3',command=lambda: indicate_grafica_interpolacion(interpolacion_indicate,grafica_interpolacion_page,entry_datax.get(),entry_datay.get()))
    grafica_btn.pack(pady=10)

    interpolacion_frame.pack(pady=20)

def grafica_ecuaciones_page(funcion,h,y0,x0,x1):
    grafica_ecuaciones_frame = tk.Frame(main_frame, bg="light cyan")
    lb = tk.Label(grafica_ecuaciones_frame, text='Solución', font=('Bold', 40), bg='Light cyan')
    lb.pack()

    fun = funcion
    g = lambda t,y: eval(fun)
    h = float(h)
    y0 = float(y0)
    x0 = float(x0)
    x1 = float(x1)
    t_e, u = Euler(g,x0,x1,h,y0)
    t_r,rk = Runge4(g,x0,x1,h,y0)

    u = np.array(u)


    # Crear una figura de Matplotlib
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    
    # Graficar la función
    ax.plot(t_e, u,'og',label='Euler', color='blue')
    ax.plot(t_r, rk,'k', label='Runge4', color='red')

    ax.legend()

    # Agregar cuadrícula
    ax.grid(True, linestyle='--', alpha=0.7)

    # Crear un lienzo de Matplotlib para Tkinter
    canvas = FigureCanvasTkAgg(fig, master=grafica_ecuaciones_frame)
    canvas.draw()

    # Mostrar el lienzo en la interfaz gráfica
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    
    grafica_ecuaciones_frame.pack(pady=20)

def ecuaciones_page():
    ecuaciones_frame = tk.Frame(main_frame, bg="light cyan")
    lb = tk.Label(ecuaciones_frame, text='Ecuaciones diferenciales', font=('Bold', 40), bg='Light cyan')
    lb.pack()

    lb1 = tk.Label(ecuaciones_frame, text='Esta sección te permite resolver ecuaciones diferenciales ordinarias', font=('Arial', 12), bg='Light cyan')
    lb1.pack(pady=10)

    entry_datax_frame = tk.Frame(ecuaciones_frame, bg="light cyan")
    lb_insert_datax = tk.Label(entry_datax_frame, text='Inserte la ecuacion diferencial:', font=('Arial', 12), bg='light cyan')
    lb_insert_datax.pack(side=tk.LEFT, padx=(0, 5))

    entry_ecuacion = tk.Entry(entry_datax_frame, font=('Arial', 12), width=60)
    entry_ecuacion.pack(side=tk.LEFT)

    entry_datax_frame.pack(pady=5)

    entry_h_frame = tk.Frame(ecuaciones_frame, bg="light cyan")
    lb_insert_x0 = tk.Label(entry_h_frame, text='Ingrese el h: ', font=('Arial', 12), bg='light cyan')
    lb_insert_x0.pack(side=tk.LEFT, padx=(0, 5))

    entry_h = tk.Entry(entry_h_frame, font=('Arial', 12), width=30)
    entry_h.pack(side=tk.LEFT)

    entry_h_frame.pack(pady=5)

    entry_y0_frame = tk.Frame(ecuaciones_frame, bg="light cyan")
    lb_insert_x0 = tk.Label(entry_y0_frame, text='Ingrese el punto inicial y: ', font=('Arial', 12), bg='light cyan')
    lb_insert_x0.pack(side=tk.LEFT, padx=(0, 5))

    entry_y0 = tk.Entry(entry_y0_frame, font=('Arial', 12), width=30)
    entry_y0.pack(side=tk.LEFT)

    entry_y0_frame.pack(pady=5)

    entry_x0_frame = tk.Frame(ecuaciones_frame, bg="light cyan")
    lb_insert_tol = tk.Label(entry_x0_frame, text='Ingrese el punto inicial x: ', font=('Arial', 12), bg='light cyan')
    lb_insert_tol.pack(side=tk.LEFT, padx=(0, 5))

    entry_x0 = tk.Entry(entry_x0_frame, font=('Arial', 12), width=30)
    entry_x0.pack(side=tk.LEFT)

    entry_x0_frame.pack(pady=5)

    entry_x1_frame = tk.Frame(ecuaciones_frame, bg="light cyan")
    lb_insert_tol = tk.Label(entry_x1_frame, text='Ingrese el punto final x: ', font=('Arial', 12), bg='light cyan')
    lb_insert_tol.pack(side=tk.LEFT, padx=(0, 5))

    entry_x1 = tk.Entry(entry_x1_frame, font=('Arial', 12), width=30)
    entry_x1.pack(side=tk.LEFT)

    entry_x1_frame.pack(pady=5)

    grafica_btn = tk.Button(ecuaciones_frame, text="Ejecutar", font=('Bold', 15), fg='red', bd=5, bg='#c3c3c3',command=lambda: indicate_grafica_ecuaciones(ecuaciones_indicate,grafica_ecuaciones_page,entry_ecuacion.get(),entry_h.get(),entry_y0.get(),entry_x0.get(),entry_x1.get()))
    grafica_btn.pack(pady=10)


    ecuaciones_frame.pack(pady=20)


def hide_indicators():
    home_indicate.config(bg="#c3c3c3")
    taylor_indicate.config(bg="#c3c3c3")
    ceros_indicate.config(bg="#c3c3c3")
    interpolacion_indicate.config(bg="#c3c3c3")
    ecuaciones_indicate.config(bg = "#c3c3c3")

def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()
    
def indicate(lb,page):
    hide_indicators()
    lb.config(bg='blue4')
    delete_pages()
    page()

def indicate_grafica_taylor(lb,page,funcion):
    hide_indicators()
    lb.config(bg='blue4')
    delete_pages()
    page(funcion)

def indicate_grafica_ceros(lb,page,funcion,punto_i,punto_f,raiz):
    hide_indicators()
    lb.config(bg='blue4')
    delete_pages()
    page(funcion,punto_i,punto_f,raiz)

def indicate_grafica_interpolacion(lb,page,xd,yd):
    hide_indicators()
    lb.config(bg='blue4')
    delete_pages()
    page(xd,yd)

def indicate_grafica_ecuaciones(lb,page,funcion,h,y0,x0,x1):
    hide_indicators()
    lb.config(bg='blue4')
    delete_pages()
    page(funcion,h,y0,x0,x1)


options_frame = tk.Frame(root, bg = '#c3c3c3',)

home_btn = tk.Button(options_frame, text= 'Home', font=('Bold',20),
                     fg = 'blue4', bd=5, bg='light cyan',command=lambda: indicate(home_indicate,home_page))
home_btn.place(x=60, y=120)
home_indicate = tk.Label(options_frame, text = '', bg ='#c3c3c3')
home_indicate.place(x=3, y=120,width=5, height=60)

taylor_btn = tk.Button(options_frame, text= 'Series de Taylor', font=('Bold',15),
                     fg = 'blue4', bd=5, bg='light cyan',command=lambda: indicate(taylor_indicate,taylor_page))
taylor_btn.place(x=35, y=240)
taylor_indicate = tk.Label(options_frame, text = '', bg ='#c3c3c3')
taylor_indicate.place(x=3, y=240,width=5, height=60)

ceros_btn = tk.Button(options_frame, text= 'Ceros', font=('Bold',15),
                     fg = 'blue4', bd=5, bg='light cyan',command=lambda: indicate(ceros_indicate,ceros_page))
ceros_btn.place(x=70, y=340)
ceros_indicate = tk.Label(options_frame, text = '', bg ='#c3c3c3')
ceros_indicate.place(x=3, y=340,width=5, height=60)

interpolacion_btn = tk.Button(options_frame, text= 'Interpolación', font=('Bold',15),
                     fg = 'blue4', bd=5, bg='light cyan',command=lambda: indicate(interpolacion_indicate,interpolacion_page))
interpolacion_btn.place(x=40, y=440)
interpolacion_indicate = tk.Label(options_frame, text = '', bg ='#c3c3c3')
interpolacion_indicate.place(x=3, y=440,width=5, height=60)


ecuaciones_btn = tk.Button(options_frame, text= 'Ecuaciones Diferenciales', font=('Bold',15),
                     fg = 'blue4', bd=5, bg='light cyan',command=lambda: indicate(ecuaciones_indicate,ecuaciones_page))
ecuaciones_btn.place(x=0, y=540)
ecuaciones_indicate = tk.Label(options_frame, text = '', bg ='#c3c3c3')
ecuaciones_indicate.place(x=3, y=540,width=5, height=50)


options_frame.pack(side = tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=230, height=1000)

main_frame = tk.Frame(root,bg='light cyan',highlightbackground='black', highlightthickness=2)

main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height = 1000, width=1200)

root.mainloop()