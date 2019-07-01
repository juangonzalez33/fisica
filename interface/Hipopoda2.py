
import tkinter as tk
import matplotlib.animation as ani
import mpl_toolkits.mplot3d.axes3d as p3
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)


def sys_exit():
    tk.close()


def toggle(event):
    global tog
    if tog == True:
        t_btn.config(image=off)
        tog = False
    else:
        t_btn.config(image=on)
        tog = True

def posicion_ejemplo(root):
    fig = plt.figure()
    frame = tk.Frame(root, width=300, height=800)
    frame.place(x=240, y=240, height=546, width=642)
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().pack(side='top', fill='both')
    ax = p3.Axes3D(fig)

    def gen():
        for theta in np.linspace(0, 4 * np.pi, 99):
            yield np.array([20 + (50 - 20) * np.cos(theta), (50 - 20) * np.sin(theta),
                            2 * (5 * (50 - 20)) ** (1 / 2) * np.sin(theta / 2)])

    def update(num, data, line):
        line.set_data(data[:2, :num])
        line.set_3d_properties(data[2, :num])

    N = 100
    plt.rcParams['legend.fontsize'] = 12
    data = np.array(list(gen())).T
    line, = ax.plot(data[0, 0:1], data[1, 0:1], data[2, 0:1], label='Hipopede de Eudoxo')

    ax.set_xlim3d([-50.0, 50.0])
    ax.set_xlabel('X')

    ax.set_ylim3d([-50.0, 50.0])
    ax.set_ylabel('Y')

    ax.set_zlim3d([-50.0, 50.0])
    ax.set_zlabel('Z')
    anim = ani.FuncAnimation(fig, update, N, fargs=(data, line), interval=1700 / N, repeat=False)
    ax.legend()
    canvas._tkcanvas.pack(side='top', fill='both', expand=1)
    tk.mainloop()


def posicion(root,a,b):
    if len(a.get()) == 0:
        pass
    else:
        if tog==True:
            fig = plt.figure()
            frame = tk.Frame(root, width=300, height=800)
            frame.place(x=240, y=240, height=546, width=642)
            canvas = FigureCanvasTkAgg(fig, master=frame)
            canvas.get_tk_widget().pack(side='top', fill='both')
            ax = p3.Axes3D(fig)

            def gen():
                for theta in np.linspace(0, 4 * np.pi, 99):
                    yield np.array([int(a.get()) + (int(b.get()) - int(a.get())) * np.cos(theta), (int(b.get()) - int(a.get())) * np.sin(theta),
                                    2 * (int(a.get()) * (int(b.get()) - int(a.get()))) ** (1 / 2) * np.sin(theta / 2)])

            def update(num, data, line):
                line.set_data(data[:2, :num])
                line.set_3d_properties(data[2, :num])

            N = 100
            plt.rcParams['legend.fontsize'] = 12
            data = np.array(list(gen())).T
            line, = ax.plot(data[0, 0:1], data[1, 0:1], data[2, 0:1], label='Hipopede de Eudoxo')
            ax.set_xlim3d([-(float(b.get()) + 5.0), float(b.get()) + 5.0])
            ax.set_xlabel('X')

            ax.set_ylim3d([-(float(b.get()) + 5.0), float(b.get()) + 5.0])
            ax.set_ylabel('Y')

            ax.set_zlim3d([-(float(b.get()) + 5.0), float(b.get()) + 5.0])
            ax.set_zlabel('Z')
            anim = ani.FuncAnimation(fig, update, N, fargs=(data, line), interval=1700 / N, repeat=False)
            ax.legend()
            canvas._tkcanvas.pack(side='top', fill='both', expand=1)
            tk.mainloop()
        else:
            fig = plt.figure()
            frame = tk.Frame(root, width=300, height=800)
            frame.place(x=240, y=240, height=546, width=642)
            canvas = FigureCanvasTkAgg(fig, master=frame)
            canvas.get_tk_widget().pack(side='top', fill='both')
            ax = p3.Axes3D(fig)
            plt.rcParams['legend.fontsize'] = 12
            ax = fig.gca(projection='3d')
            # Prepare arrays x, y, z
            ax.set_xlim3d([-(float(b.get()) + 5.0), float(b.get()) + 5.0])
            ax.set_xlabel('X')

            ax.set_ylim3d([-(float(b.get()) + 5.0), float(b.get()) + 5.0])
            ax.set_ylabel('Y')

            ax.set_zlim3d([-(float(b.get()) + 5.0), float(b.get()) + 5.0])
            ax.set_zlabel('Z')
            theta = np.linspace(-4 * np.pi, 4 * np.pi, 99)
            a_p = int(a.get())
            r_p = int(b.get())
            x = a_p + (r_p - a_p) * np.cos(theta)
            y = (r_p - a_p) * np.sin(theta)
            z = 2 * (a_p * (r_p - a_p)) ** (1 / 2) * np.sin(theta / 2)
            ax.plot(x, y, z, label='Hipopede de Eudoxo')

            ax.legend()
            canvas._tkcanvas.pack(side='top', fill='both', expand=1)
            #plt.show()
            tk.mainloop()
def spd():
    hipopoda_button1.config(relief="raised")
    hipopoda_button2.config(relief="sunken")
    hipopoda_button3.config(relief="raised")
    hipopoda_button4.config(relief="raised")
    hipopoda_button5.config(relief="raised")
    hipopoda_button6.config(relief="raised")
    hipopoda_button7.config(relief="raised")
    hipopoda_button8.config(relief="raised")
    hipopoda_button9.config(relief="raised")
    hipopoda_button10.config(relief="raised")
    entry.config(state='disabled')
    entry1.config(state='disabled')
    entry2.config(state='normal')
    entry3.config(state='disabled')
    label3.config(text="t")
    button_calcp.config(command=velocidad)


def velocidad():
    if (len(a.get()) != 0 and len(b.get()) != 0 and len(c.get()) != 0):
        ventana_spd = tk.Tk()
        ventana_spd.wm_title("Velocidad")
        ventana_spd.geometry("376x131")
        button = tk.Button(master=ventana_spd, text="Atrás", command=ventana_spd.destroy)
        x = -(int(a.get()) + int(b.get())) * np.sin(int(c.get()))
        y = (-int(a.get()) + int(b.get())) * np.cos(int(c.get()))
        z = np.sqrt(int(a.get()) * (-int(a.get()) + int(b.get()))) * np.cos(int(c.get()) / 2)
        solucion = ("La velocidad es " + " x: " + str('%.3f'%(x)) + " y: " + str('%.3f'%(y)) + " z: " + str('%.3f'%(z)))
        entry_respuesta = tk.Label(master=ventana_spd, text=solucion)
        entry_respuesta.pack()
        ventana_spd.resizable(0, 0)
        ventana_spd.mainloop()


def aceleracion():
    if (len(a.get()) != 0 and len(b.get()) != 0 and len(c.get()) != 0):
        ventana_acc = tk.Tk()
        ventana_acc.wm_title("Aceleracion")
        ventana_acc.geometry("376x131")
        button = tk.Button(master=ventana_acc, text="Atrás", command=ventana_acc.destroy)
        x = -(int(a.get()) + int(b.get())) * np.cos(int(c.get()))
        y = (int(a.get()) - int(b.get())) * np.sin(int(c.get()))
        z = np.sqrt(int(a.get()) * (-int(a.get()) + int(b.get()))) * np.sin(int(c.get()) / 2)*(-1/2)
        solucion = ("La aceleración es " + " x: " + str('%.3f' % (x)) + " y: " + str('%.3f' % (y)) + " z: " + str(
            '%.3f' % (z)))
        entry_respuesta = tk.Label(master=ventana_acc, text=solucion)
        entry_respuesta.pack()
        ventana_acc.resizable(0, 0)
        ventana_acc.mainloop()
def aceleracionmedia():
    ventana_acc = tk.Tk()
    ventana_acc.wm_title("Aceleracion Media")
    ventana_acc.geometry("376x131")
    x = -(int(a.get()) + int(b.get())) * np.sin(int(c.get()))
    y = (-int(a.get()) + int(b.get())) * np.cos(int(c.get()))
    z = np.sqrt(int(a.get()) * (-int(a.get()) + int(b.get()))) * np.cos(int(c.get()) / 2)
    x2 = -(int(a.get()) + int(b.get())) * np.sin(int(d.get()))
    y2 = (-int(a.get()) + int(b.get())) * np.cos(int(d.get()))
    z2 = np.sqrt(int(a.get()) * (-int(a.get()) + int(b.get()))) * np.cos(int(d.get()) / 2)
    xa = (x2-x)/(int(d.get())-int(c.get()))
    ya = (y2-y)/(int(d.get())-int(c.get()))
    za = (z2-z)/(int(d.get())-int(c.get()))
    solucion = "la aceleracion media es " + "x: " + str('%.3f' % (xa)) + " y: " + str('%.3f' % (ya)) + " z: " + str('%.3f' % (za))
    entry_respuesta = tk.Label(master=ventana_acc, text=solucion)
    entry_respuesta.pack()
def velocidadmedia():
    ventana_acc = tk.Tk()
    ventana_acc.wm_title("Velocidad Media")
    ventana_acc.geometry("376x131")
    a_p = int(a.get())
    r_p = int(b.get())
    t = int(c.get())
    x = a_p + (r_p - a_p) * np.cos(t)
    y = (r_p - a_p) * np.sin(t)
    z = 2 * (a_p * (r_p - a_p)) ** (1 / 2) * np.sin(t / 2)
    t2 = int(d.get())
    x2 = a_p + (r_p - a_p) * np.cos(t2)
    y2 = (r_p - a_p) * np.sin(t2)
    z2 = 2 * (a_p * (r_p - a_p)) ** (1 / 2) * np.sin(t2 / 2)
    xv = (x2-x)/(t2-t)
    yv = (y2-y)/(t2-t)
    zv = (z2-z)/(t2-t)
    solucion ="la velocidad media es "+"x: "+str('%.3f' % (xv))+" y: "+str('%.3f' % (yv)) + " z: "+str('%.3f' % (zv))
    entry_respuesta = tk.Label(master=ventana_acc, text=solucion)
    entry_respuesta.pack()
    ventana_acc.resizable(0, 0)
    ventana_acc.mainloop()
def spdm():
    hipopoda_button1.config(relief="raised")
    hipopoda_button3.config(relief="sunken")
    hipopoda_button2.config(relief="raised")
    hipopoda_button4.config(relief="raised")
    hipopoda_button5.config(relief="raised")
    hipopoda_button6.config(relief="raised")
    hipopoda_button7.config(relief="raised")
    hipopoda_button8.config(relief="raised")
    hipopoda_button9.config(relief="raised")
    hipopoda_button10.config(relief="raised")
    label3.config(text="ti")
    label4.config(text="tf")
    entry.config(state='disabled')
    entry1.config(state='disabled')
    entry2.config(state='normal')
    entry3.config(state='normal')
    button_calcp.config(command=velocidadmedia)


def pos(root,a,b):
    entry3.config(state='disabled')
    hipopoda_button1.config(relief="sunken")
    hipopoda_button2.config(relief="raised")
    hipopoda_button3.config(relief="raised")
    hipopoda_button4.config(relief="raised")
    hipopoda_button5.config(relief="raised")
    hipopoda_button6.config(relief="raised")
    hipopoda_button7.config(relief="raised")
    hipopoda_button8.config(relief="raised")
    hipopoda_button9.config(relief="raised")
    hipopoda_button10.config(relief="raised")
    entry.config(state='normal')
    entry1.config(state='normal')
    entry2.config(state='disabled')
    entry3.config(state='disabled')
    button_calcp.config(command=lambda:posicion(root, a, b))


def acc():
    hipopoda_button1.config(relief="raised")
    hipopoda_button2.config(relief="raised")
    hipopoda_button3.config(relief="raised")
    hipopoda_button4.config(relief="sunken")
    hipopoda_button5.config(relief="raised")
    hipopoda_button6.config(relief="raised")
    hipopoda_button7.config(relief="raised")
    hipopoda_button8.config(relief="raised")
    hipopoda_button9.config(relief="raised")
    hipopoda_button10.config(relief="raised")
    button_calcp.config(command=aceleracion)
    label3.config(text="t")
    entry.config(state='disabled')
    entry1.config(state='disabled')
    entry2.config(state='normal')
    entry3.config(state='disabled')
def accm():
    hipopoda_button1.config(relief="raised")
    hipopoda_button2.config(relief="raised")
    hipopoda_button3.config(relief="raised")
    hipopoda_button4.config(relief="raised")
    hipopoda_button5.config(relief="sunken")
    hipopoda_button6.config(relief="raised")
    hipopoda_button7.config(relief="raised")
    hipopoda_button8.config(relief="raised")
    hipopoda_button9.config(relief="raised")
    hipopoda_button10.config(relief="raised")
    button_calcp.config(command=aceleracionmedia)
    label3.config(text="ti")
    label4.config(text="tf")
    entry.config(state='disabled')
    entry1.config(state='disabled')
    entry2.config(state='normal')
    entry3.config(state='normal')


def curv():
    hipopoda_button1.config(relief="raised")
    hipopoda_button2.config(relief="raised")
    hipopoda_button3.config(relief="raised")
    hipopoda_button4.config(relief="raised")
    hipopoda_button5.config(relief="raised")
    hipopoda_button6.config(relief="sunken")
    hipopoda_button7.config(relief="raised")
    hipopoda_button8.config(relief="raised")
    hipopoda_button9.config(relief="raised")
    hipopoda_button10.config(relief="raised")


def rcurv():
    hipopoda_button1.config(relief="raised")
    hipopoda_button2.config(relief="raised")
    hipopoda_button3.config(relief="raised")
    hipopoda_button4.config(relief="raised")
    hipopoda_button5.config(relief="raised")
    hipopoda_button6.config(relief="raised")
    hipopoda_button7.config(relief="sunken")
    hipopoda_button8.config(relief="raised")
    hipopoda_button9.config(relief="raised")
    hipopoda_button10.config(relief="raised")


def tors():
    hipopoda_button1.config(relief="raised")
    hipopoda_button2.config(relief="raised")
    hipopoda_button3.config(relief="raised")
    hipopoda_button4.config(relief="raised")
    hipopoda_button5.config(relief="raised")
    hipopoda_button6.config(relief="raised")
    hipopoda_button7.config(relief="raised")
    hipopoda_button8.config(relief="sunken")
    hipopoda_button9.config(relief="raised")
    hipopoda_button10.config(relief="raised")


def rtors():
    hipopoda_button1.config(relief="raised")
    hipopoda_button2.config(relief="raised")
    hipopoda_button3.config(relief="raised")
    hipopoda_button4.config(relief="raised")
    hipopoda_button5.config(relief="raised")
    hipopoda_button6.config(relief="raised")
    hipopoda_button7.config(relief="raised")
    hipopoda_button8.config(relief="raised")
    hipopoda_button9.config(relief="sunken")
    hipopoda_button10.config(relief="raised")


def larc():
    hipopoda_button1.config(relief="raised")
    hipopoda_button2.config(relief="raised")
    hipopoda_button3.config(relief="raised")
    hipopoda_button4.config(relief="raised")
    hipopoda_button5.config(relief="raised")
    hipopoda_button6.config(relief="raised")
    hipopoda_button7.config(relief="raised")
    hipopoda_button8.config(relief="raised")
    hipopoda_button9.config(relief="raised")
    hipopoda_button10.config(relief="sunken")


if __name__ == "__main__":
    tog = True
    root = tk.Tk()
    root.wm_title("Física Interactiva")
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)
    root.geometry("900x900")
    root.resizable(0, 0)
    dato = tk.StringVar()
    a = tk.StringVar()
    b = tk.StringVar()
    c = tk.StringVar()
    d =tk.StringVar()
    hipopoda_button1 = tk.Button(master=root, text="Posición", command=lambda:pos(root,a,b))
    hipopoda_button1.pack()
    hipopoda_button1.config(relief="sunken")
    hipopoda_button1.place(x=20, y=220, height=40, width=200)
    hipopoda_button2 = tk.Button(master=root, text="Velocidad", command=spd)
    hipopoda_button2.pack()
    hipopoda_button2.place(x=20, y=280, height=40, width=200)
    hipopoda_button3 = tk.Button(master=root, text="Velocidad Media", command=spdm)
    hipopoda_button3.pack()
    hipopoda_button3.place(x=20, y=340, height=40, width=200)
    hipopoda_button4 = tk.Button(master=root, text="Aceleración", command=acc)
    hipopoda_button4.pack()
    hipopoda_button4.place(x=20, y=400, height=40, width=200)
    hipopoda_button5 = tk.Button(master=root, text="Aceleración Media", command=accm)
    hipopoda_button5.pack()
    hipopoda_button5.place(x=20, y=460, height=40, width=200)
    hipopoda_button6 = tk.Button(master=root, text="Curvatura", command=curv)
    hipopoda_button6.pack()
    hipopoda_button6.place(x=20, y=520, height=40, width=200)
    hipopoda_button7 = tk.Button(master=root, text="Radio de Curvatura", command=rcurv)
    hipopoda_button7.pack()
    hipopoda_button7.place(x=20, y=580, height=40, width=200)
    hipopoda_button8 = tk.Button(master=root, text="Torsión", command=tors)
    hipopoda_button8.pack()
    hipopoda_button8.place(x=20, y=640, height=40, width=200)
    hipopoda_button9 = tk.Button(master=root, text="Radio de Torsión", command=rtors)
    hipopoda_button9.pack()
    hipopoda_button9.place(x=20, y=700, height=40, width=200)
    hipopoda_button10 = tk.Button(master=root, text="Longitud de Arco", command=larc)
    hipopoda_button10.pack()
    hipopoda_button10.place(x=20, y=760, height=40, width=200)
    hipopoda_button = tk.Button(master=root, text="Atrás", command=root.destroy)
    hipopoda_button.pack()
    hipopoda_button.place(x=20, y=10, height=40, width=200)
    titulo_label = tk.Label(master=root, text="Hipopoda", font=("letter case", 50))
    titulo_label.place(x=290, y=70, height=371, width=111)
    titulo_label.pack()
    label2 = tk.Label(master=root, text="R", font=("letter case", 12))
    label2.place(x=440, y=810, height=21, width=21)
    label3 = tk.Label(master=root, text="t", font=("letter case", 12))
    label3.place(x=560, y=810, height=21, width=21)

    label4 = tk.Label(master=root, text="tf", font=("letter case", 12))
    label4.place(x=680, y=810, height=21, width=21)

    label1 = tk.Label(master=root, text="A", font=("letter case", 12))
    label1.place(x=320, y=810, height=21, width=21)
    entry = tk.Entry(master=root, textvariable=a)
    entry.place(x=340, y=810, height=30, width=75)
    entry1 = tk.Entry(master=root, textvariable=b)
    entry1.place(x=460, y=810, height=30, width=75)
    entry2 = tk.Entry(master=root, textvariable=c)
    entry2.place(x=580, y=810, height=30, width=75)
    entry3 = tk.Entry(master=root, textvariable=d)
    entry3.place(x=700, y=810, height=30, width=75)
    entry2.config(state='disable')
    entry3.config(state='disable')
    button_calcp = tk.Button(master=root, text="Calcular",command=lambda:posicion(root,a,b))
    button_calcp.place(y=850, x=450, height=40, width=200)
    on = tk.PhotoImage(file="on.gif")
    off = tk.PhotoImage(file="off.gif")
    t_btn = tk.Label(width=12, image=on)
    t_btn.bind('<Button-1>', toggle)
    t_btn.place(x=840, y=10, height=15, width=27)
    labelk = tk.Label(master=root, text="Animación")
    labelk.place(x=820, y=30)
    posicion_ejemplo(root)
    root.mainloop()