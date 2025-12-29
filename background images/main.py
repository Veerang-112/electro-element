import sys
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QMessageBox, QFrame
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
from matplotlib.patheffects import withStroke
import numpy as np
from PyQt5.QtGui import QMovie


class Custom_Title_UI(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("gui.ui", self)

        self.movie = QMovie("electron_2.gif")
        self.electron.setMovie(self.movie)
        self.movie.start()
        self.movie = QMovie("0001-0129.gif")
        self.heading.setMovie(self.movie)
        self.movie.start()
        
        # remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        # Get a reference to the button (assuming its objectName is "{Element symbol}")
        self.button_H = self.findChild(QtWidgets.QPushButton, 'H')
        self.button_He = self.findChild(QtWidgets.QPushButton, 'He')
        self.button_Li = self.findChild(QtWidgets.QPushButton, 'Li')
        self.button_Be = self.findChild(QtWidgets.QPushButton, 'Be')
        self.button_B = self.findChild(QtWidgets.QPushButton, 'B')
        self.button_C = self.findChild(QtWidgets.QPushButton, 'C')
        self.button_N = self.findChild(QtWidgets.QPushButton, 'N')
        self.button_O = self.findChild(QtWidgets.QPushButton, 'O')
        self.button_F = self.findChild(QtWidgets.QPushButton, 'F')
        self.button_Ne = self.findChild(QtWidgets.QPushButton, 'Ne')
        self.button_Na = self.findChild(QtWidgets.QPushButton, 'Na')
        self.button_Mg = self.findChild(QtWidgets.QPushButton, 'Mg')
        self.button_Al = self.findChild(QtWidgets.QPushButton, 'Al')
        self.button_Si = self.findChild(QtWidgets.QPushButton, 'Si')
        self.button_P = self.findChild(QtWidgets.QPushButton, 'P')
        self.button_S = self.findChild(QtWidgets.QPushButton, 'S')
        self.button_Cl = self.findChild(QtWidgets.QPushButton, 'Cl')
        self.button_Ar = self.findChild(QtWidgets.QPushButton, 'Ar')
        self.button_K = self.findChild(QtWidgets.QPushButton, 'K')
        self.button_Ca = self.findChild(QtWidgets.QPushButton, 'Ca')
        self.button_Sc = self.findChild(QtWidgets.QPushButton, 'Sc')
        self.button_Ti = self.findChild(QtWidgets.QPushButton, 'Ti')
        self.button_V = self.findChild(QtWidgets.QPushButton, 'V')
        self.button_Cr = self.findChild(QtWidgets.QPushButton, 'Cr')
        self.button_Mn = self.findChild(QtWidgets.QPushButton, 'Mn')
        self.button_Fe = self.findChild(QtWidgets.QPushButton, 'Fe')
        self.button_Co = self.findChild(QtWidgets.QPushButton, 'Co')
        self.button_Ni = self.findChild(QtWidgets.QPushButton, 'Ni')
        self.button_Cu = self.findChild(QtWidgets.QPushButton, 'Cu')
        self.button_Zn = self.findChild(QtWidgets.QPushButton, 'Zn')
        self.button_Ga = self.findChild(QtWidgets.QPushButton, 'Ga')
        self.button_Ge = self.findChild(QtWidgets.QPushButton, 'Ge')
        self.button_As = self.findChild(QtWidgets.QPushButton, 'As')
        self.button_Se = self.findChild(QtWidgets.QPushButton, 'Se')
        self.button_Br = self.findChild(QtWidgets.QPushButton, 'Br')
        self.button_Kr = self.findChild(QtWidgets.QPushButton, 'Kr')
        self.button_Rb = self.findChild(QtWidgets.QPushButton, 'Rb')
        self.button_Sr = self.findChild(QtWidgets.QPushButton, 'Sr')
        self.button_Y = self.findChild(QtWidgets.QPushButton, 'Y')
        self.button_Zr = self.findChild(QtWidgets.QPushButton, 'Zr')
        self.button_Nb = self.findChild(QtWidgets.QPushButton, 'Nb')
        self.button_Mo = self.findChild(QtWidgets.QPushButton, 'Mo')
        self.button_Tc = self.findChild(QtWidgets.QPushButton, 'Tc')
        self.button_Ru = self.findChild(QtWidgets.QPushButton, 'Ru')
        self.button_Rh = self.findChild(QtWidgets.QPushButton, 'Rh')
        self.button_Pd = self.findChild(QtWidgets.QPushButton, 'Pd')
        self.button_Ag = self.findChild(QtWidgets.QPushButton, 'Ag')
        self.button_Cd = self.findChild(QtWidgets.QPushButton, 'Cd')
        self.button_In = self.findChild(QtWidgets.QPushButton, 'In')
        self.button_Sn = self.findChild(QtWidgets.QPushButton, 'Sn')
        self.button_Sb = self.findChild(QtWidgets.QPushButton, 'Sb')
        self.button_Te = self.findChild(QtWidgets.QPushButton, 'Te')
        self.button_I = self.findChild(QtWidgets.QPushButton, 'I')
        self.button_Xe = self.findChild(QtWidgets.QPushButton, 'Xe')
        self.button_Cs = self.findChild(QtWidgets.QPushButton, 'Cs')
        self.button_Ba = self.findChild(QtWidgets.QPushButton, 'Ba')
        self.button_La = self.findChild(QtWidgets.QPushButton, 'La')
        self.button_Ce = self.findChild(QtWidgets.QPushButton, 'Ce')
        self.button_Pr = self.findChild(QtWidgets.QPushButton, 'Pr')
        self.button_Nd = self.findChild(QtWidgets.QPushButton, 'Nd')
        self.button_Pm = self.findChild(QtWidgets.QPushButton, 'Pm')
        self.button_Sm = self.findChild(QtWidgets.QPushButton, 'Sm')
        self.button_Eu = self.findChild(QtWidgets.QPushButton, 'Eu')
        self.button_Gd = self.findChild(QtWidgets.QPushButton, 'Gd')
        self.button_Tb = self.findChild(QtWidgets.QPushButton, 'Tb')
        self.button_Dy = self.findChild(QtWidgets.QPushButton, 'Dy')
        self.button_Ho = self.findChild(QtWidgets.QPushButton, 'Ho')
        self.button_Er = self.findChild(QtWidgets.QPushButton, 'Er')
        self.button_Tm = self.findChild(QtWidgets.QPushButton, 'Tm')
        self.button_Yb = self.findChild(QtWidgets.QPushButton, 'Yb')
        self.button_Lu = self.findChild(QtWidgets.QPushButton, 'Lu')
        self.button_Hf = self.findChild(QtWidgets.QPushButton, 'Hf')
        self.button_Ta = self.findChild(QtWidgets.QPushButton, 'Ta')
        self.button_W = self.findChild(QtWidgets.QPushButton, 'W')
        self.button_Re = self.findChild(QtWidgets.QPushButton, 'Re')
        self.button_Os = self.findChild(QtWidgets.QPushButton, 'Os')
        self.button_Ir = self.findChild(QtWidgets.QPushButton, 'Ir')
        self.button_Pt = self.findChild(QtWidgets.QPushButton, 'Pt')
        self.button_Au = self.findChild(QtWidgets.QPushButton, 'Au')
        self.button_Hg = self.findChild(QtWidgets.QPushButton, 'Hg')
        self.button_Tl = self.findChild(QtWidgets.QPushButton, 'Tl')
        self.button_Pb = self.findChild(QtWidgets.QPushButton, 'Pb')
        self.button_Bi = self.findChild(QtWidgets.QPushButton, 'Bi')
        self.button_Po = self.findChild(QtWidgets.QPushButton, 'Po')
        self.button_At = self.findChild(QtWidgets.QPushButton, 'At')
        self.button_Rn = self.findChild(QtWidgets.QPushButton, 'Rn')
        self.button_Fr = self.findChild(QtWidgets.QPushButton, 'Fr')
        self.button_Ra = self.findChild(QtWidgets.QPushButton, 'Ra')
        self.button_Ac = self.findChild(QtWidgets.QPushButton, 'Ac')
        self.button_Th = self.findChild(QtWidgets.QPushButton, 'Th')
        self.button_Pa = self.findChild(QtWidgets.QPushButton, 'Pa')
        self.button_U = self.findChild(QtWidgets.QPushButton, 'U')
        self.button_Np = self.findChild(QtWidgets.QPushButton, 'Np')
        self.button_Pu = self.findChild(QtWidgets.QPushButton, 'Pu')
        self.button_Am = self.findChild(QtWidgets.QPushButton, 'Am')
        self.button_Cm = self.findChild(QtWidgets.QPushButton, 'Cm')
        self.button_Bk = self.findChild(QtWidgets.QPushButton, 'Bk')
        self.button_Cf = self.findChild(QtWidgets.QPushButton, 'Cf')
        self.button_Es = self.findChild(QtWidgets.QPushButton, 'Es')
        self.button_Fm = self.findChild(QtWidgets.QPushButton, 'Fm')
        self.button_Md = self.findChild(QtWidgets.QPushButton, 'Md')
        self.button_No = self.findChild(QtWidgets.QPushButton, 'No')
        self.button_Lr = self.findChild(QtWidgets.QPushButton, 'Lr')
        self.button_Rf = self.findChild(QtWidgets.QPushButton, 'Rf')
        self.button_Db = self.findChild(QtWidgets.QPushButton, 'Db')
        self.button_Sg = self.findChild(QtWidgets.QPushButton, 'Sg')
        self.button_Bh = self.findChild(QtWidgets.QPushButton, 'Bh')
        self.button_Hs = self.findChild(QtWidgets.QPushButton, 'Hs')
        self.button_Mt = self.findChild(QtWidgets.QPushButton, 'Mt')
        self.button_Ds = self.findChild(QtWidgets.QPushButton, 'Ds')
        self.button_Rg = self.findChild(QtWidgets.QPushButton, 'Rg')
        self.button_Cn = self.findChild(QtWidgets.QPushButton, 'Cn')
        self.button_Nh = self.findChild(QtWidgets.QPushButton, 'Nh')
        self.button_Fl = self.findChild(QtWidgets.QPushButton, 'Fl')
        self.button_Mc = self.findChild(QtWidgets.QPushButton, 'Mc')
        self.button_Lv = self.findChild(QtWidgets.QPushButton, 'Lv')
        self.button_Ts = self.findChild(QtWidgets.QPushButton, 'Ts')
        self.button_Og = self.findChild(QtWidgets.QPushButton, 'Og')

        # Connect the button click event to the clicked method
        self.button_H.clicked.connect(self.Hydrogen)
        self.button_He.clicked.connect(self.Helium)
        self.button_Li.clicked.connect(self.Lithium)
        self.button_Be.clicked.connect(self.Beryllium)
        self.button_B.clicked.connect(self.Boron)
        self.button_C.clicked.connect(self.Carbon)
        self.button_N.clicked.connect(self.Nitrogen)
        self.button_O.clicked.connect(self.Oxygen)
        self.button_F.clicked.connect(self.Fluorine)
        self.button_Ne.clicked.connect(self.Neon)
        self.button_Na.clicked.connect(self.Sodium)
        self.button_Mg.clicked.connect(self.Magnesium)
        self.button_Al.clicked.connect(self.Aluminum)
        self.button_Si.clicked.connect(self.Silicon)
        self.button_P.clicked.connect(self.Phosphorus)
        self.button_S.clicked.connect(self.Sulfur)
        self.button_Cl.clicked.connect(self.Chlorine)
        self.button_Ar.clicked.connect(self.Argon)
        self.button_K.clicked.connect(self.Potassium)
        self.button_Ca.clicked.connect(self.Calcium)
        self.button_Sc.clicked.connect(self.Scandium)
        self.button_Ti.clicked.connect(self.Titanium)
        self.button_V.clicked.connect(self.Vanadium)
        self.button_Cr.clicked.connect(self.Chromium)
        self.button_Mn.clicked.connect(self.Manganese)
        self.button_Fe.clicked.connect(self.Iron)
        self.button_Co.clicked.connect(self.Cobalt)
        self.button_Ni.clicked.connect(self.Nickel)
        self.button_Cu.clicked.connect(self.Copper)
        self.button_Zn.clicked.connect(self.Zinc)
        self.button_Ga.clicked.connect(self.Gallium)
        self.button_Ge.clicked.connect(self.Germanium)
        self.button_As.clicked.connect(self.Arsenic)
        self.button_Se.clicked.connect(self.Selenium)
        self.button_Br.clicked.connect(self.Bromine)
        self.button_Kr.clicked.connect(self.Krypton)
        self.button_Rb.clicked.connect(self.Rubidium)
        self.button_Sr.clicked.connect(self.Strontium)
        self.button_Y.clicked.connect(self.Yttrium)
        self.button_Zr.clicked.connect(self.Zirconium)
        self.button_Nb.clicked.connect(self.Niobium)
        self.button_Mo.clicked.connect(self.Molybdenum)
        self.button_Tc.clicked.connect(self.Technetium)
        self.button_Ru.clicked.connect(self.Ruthenium)
        self.button_Rh.clicked.connect(self.Rhodium)
        self.button_Pd.clicked.connect(self.Palladium)
        self.button_Ag.clicked.connect(self.Silver)
        self.button_Cd.clicked.connect(self.Cadmium)
        self.button_In.clicked.connect(self.Indium)
        self.button_Sn.clicked.connect(self.Tin)
        self.button_Sb.clicked.connect(self.Antimony)
        self.button_Te.clicked.connect(self.Tellurium)
        self.button_I.clicked.connect(self.Iodine)
        self.button_Xe.clicked.connect(self.Xenon)
        self.button_Cs.clicked.connect(self.Cesium)
        self.button_Ba.clicked.connect(self.Barium)
        self.button_La.clicked.connect(self.Lanthanum)
        self.button_Ce.clicked.connect(self.Cerium)
        self.button_Pr.clicked.connect(self.Praseodymium)
        self.button_Nd.clicked.connect(self.Neodymium)
        self.button_Pm.clicked.connect(self.Promethium)
        self.button_Sm.clicked.connect(self.Samarium)
        self.button_Eu.clicked.connect(self.Europium)
        self.button_Gd.clicked.connect(self.Gadolinium)
        self.button_Tb.clicked.connect(self.Terbium)
        self.button_Dy.clicked.connect(self.Dysprosium)
        self.button_Ho.clicked.connect(self.Holmium)
        self.button_Er.clicked.connect(self.Erbium)
        self.button_Tm.clicked.connect(self.Thulium)
        self.button_Yb.clicked.connect(self.Ytterbium)
        self.button_Lu.clicked.connect(self.Lutetium)
        self.button_Hf.clicked.connect(self.Hafnium)
        self.button_Ta.clicked.connect(self.Tantalum)
        self.button_W.clicked.connect(self.Tungsten)
        self.button_Re.clicked.connect(self.Rhenium)
        self.button_Os.clicked.connect(self.Osmium)
        self.button_Ir.clicked.connect(self.Iridium)
        self.button_Pt.clicked.connect(self.Platinum)
        self.button_Au.clicked.connect(self.Gold)
        self.button_Hg.clicked.connect(self.Mercury)
        self.button_Tl.clicked.connect(self.Thallium)
        self.button_Pb.clicked.connect(self.Lead)
        #self.button_Bi.clicked.connect(self.Bismuth)
        self.button_Po.clicked.connect(self.Polonium)
        self.button_At.clicked.connect(self.Astatine)
        self.button_Rn.clicked.connect(self.Radon)
        self.button_Fr.clicked.connect(self.Francium)
        self.button_Ra.clicked.connect(self.Radium)
        self.button_Ac.clicked.connect(self.Actinium)
        self.button_Th.clicked.connect(self.Thorium)
        self.button_Pa.clicked.connect(self.Protactinium)
        self.button_U.clicked.connect(self.Uranium)
        self.button_Np.clicked.connect(self.Neptunium)
        self.button_Pu.clicked.connect(self.Plutonium)
        self.button_Am.clicked.connect(self.Americium)
        self.button_Cm.clicked.connect(self.Curium)
        self.button_Bk.clicked.connect(self.Berkelium)
        self.button_Cf.clicked.connect(self.Californium)
        self.button_Es.clicked.connect(self.Einsteinium)
        self.button_Fm.clicked.connect(self.Fermium)
        self.button_Md.clicked.connect(self.Mendelevium)
        self.button_No.clicked.connect(self.Nobelium)
        self.button_Lr.clicked.connect(self.Lawrencium)
        self.button_Rf.clicked.connect(self.Rutherfordium)
        self.button_Db.clicked.connect(self.Dubnium)
        self.button_Sg.clicked.connect(self.Seaborgium)
        self.button_Bh.clicked.connect(self.Bohrium)
        self.button_Hs.clicked.connect(self.Hassium)
        self.button_Mt.clicked.connect(self.Meitnerium)
        self.button_Ds.clicked.connect(self.Darmstadtium)
        self.button_Rg.clicked.connect(self.Roentgenium)
        self.button_Cn.clicked.connect(self.Copernicium)
        self.button_Nh.clicked.connect(self.Nihonium)
        self.button_Fl.clicked.connect(self.Flerovium)
        self.button_Mc.clicked.connect(self.Moscovium)
        self.button_Lv.clicked.connect(self.Livermorium)
        self.button_Ts.clicked.connect(self.Tennessine)
        self.button_Og.clicked.connect(self.Oganesson)
        self.animation = None

    def keyPressEvent(self, event):
        modifiers = QtWidgets.QApplication.keyboardModifiers()
        if event.key() == QtCore.Qt.Key_Escape and modifiers == QtCore.Qt.ShiftModifier:
            self.show_close_dialog()

    def show_close_dialog(self):
        reply = QMessageBox.question(self, 'Close Program', 'Do you really want to close the program?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.close()

    def setup_animation(self, num_electrons, Element,atomic_no,atomic_mass):
        n = int(np.ceil(np.sqrt(num_electrons / 2)))
        shells = n

        # Create a new window for the Matplotlib figure
        self.graph_window = QtWidgets.QMainWindow()
        self.graph_window.setWindowTitle("Graph Window")
        self.graph_window.setGeometry(200, 100, 800, 600)

        # Remove title bar from the graph window
        self.graph_window.setWindowFlag(Qt.FramelessWindowHint)

        # Create a QFrame as the central widget for the graph window
        central_frame = QFrame(self.graph_window)
        central_frame.setStyleSheet("border: 2px solid white;")  # Add a 2-pixel solid white border
        self.graph_window.setCentralWidget(central_frame)

        # Create a Matplotlib figure and axis
        self.fig = Figure(figsize=(20, 20), facecolor='black')
        ax = self.fig.add_subplot(111, projection='3d', facecolor='black')

        # Create a Matplotlib canvas widget to embed the figure in the PyQt5 application
        canvas = FigureCanvas(self.fig)
        central_layout = QVBoxLayout(central_frame)
        central_layout.addWidget(canvas)

        # Connect the close event to the close method
        self.graph_window.keyPressEvent = self.on_key

        # Initialize the animation
        self.animation = FuncAnimation(self.fig, self.update_animation,
                                       fargs=(ax, num_electrons, shells, Element,atomic_no,atomic_mass),
                                       interval=50, blit=False,cache_frame_data=False)

        # Show the graph window
        self.graph_window.show()

    def on_key(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.graph_window.close()

    def update_animation(self, frame, ax, num_electrons, shells, Element,atomic_no,atomic_mass):
        ax.cla()

        # Set the background color both inside and outside the plot to black
        ax.set_facecolor('black')
        ax.figure.set_facecolor('black')

        # Hide the axes and grid lines
        ax.set_axis_off()
        ax.grid(False)

        # Plotting nucleus at the origin
        ax.scatter(0, 0, 0, c='red', marker='o', s=200, label='Nucleus')

        # Plotting electron orbits as circles
        for shell in range(1, shells + 1):
            num_points = 100
            theta = np.linspace(0, 2 * np.pi, num_points)
            x = shell * np.cos(theta)
            y = shell * np.sin(theta)
            z = np.zeros_like(theta)
            ax.plot(x, y, z, label=f'Orbit {shell}')

            # Calculate new angles for animation
            electrons_theta = np.linspace(0, 2 * np.pi, min(num_electrons, shell * shell * 2), endpoint=False)
            electrons_theta += np.radians(frame * 5)  # Adjust the speed of rotation
            electrons_x = shell * np.cos(electrons_theta)
            electrons_y = shell * np.sin(electrons_theta)
            electrons_z = np.zeros_like(electrons_theta)

            # Plotting electrons with glow effect
            ax.scatter(electrons_x, electrons_y, electrons_z, s=40, label=f'Electrons - Orbit {shell}')
            ax.scatter(electrons_x, electrons_y, electrons_z, s=80, alpha=0.3, label='', color='white')

            num_electrons -= min(num_electrons, shell * shell * 2)

        # Move the legend outside of the plot to the right
        ax.legend(loc='center left', bbox_to_anchor=(0.9, 0.6), framealpha=0.5)

        # Add text annotation outside the plot in 3D space
        ax.text2D(-.39, 0.95, "# Press 'esc' to close the window", color='white', ha='left', va='center', fontsize=12, transform=ax.transAxes)
        atom_no=atomic_no
        ax.text2D(-.39, 0.1, f'Atomic no & no of electrons: {atomic_no}', color='white', ha='left', va='center', fontsize=12, transform=ax.transAxes)
        atom_mass=atomic_mass
        ax.text2D(-.39, 0.01, f'Atomic mass: {atomic_mass}', color='white', ha='left', va='center', fontsize=12, transform=ax.transAxes)
        text = Element
        ax.text2D(0.2, 1.03, text, color='white', fontsize=28, ha='left', va='center', transform=ax.transAxes,
                  path_effects=[withStroke(linewidth=5, foreground='pink')])

        # Ensure the plot is updated and displayed inside the embedded Matplotlib figure
        self.fig.canvas.draw()

    def Hydrogen(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(1, 'Hydrogen', '1', '1.008')
        print('clicked')

    def Helium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(2, 'Helium', '2', '4.0026')
        print('clicked')

    def Lithium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(3, 'Lithium', '3', '6.941')
        print('clicked')

    def Beryllium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(4, 'Beryllium', '4', '9.012')
        print('clicked')

    def Boron(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(5, 'Boron', '5', '10.81')
        print('clicked')

    def Carbon(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(6, 'Carbon', '6', '12.011')
        print('clicked')

    def Nitrogen(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(7, 'Nitrogen', '7', '14.007')
        print('clicked')

    def Oxygen(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(8, 'Oxygen', '8', '15.999')
        print('clicked')

    def Fluorine(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(9, 'Fluorine', '9', '18.998')
        print('clicked')

    def Neon(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(10, 'Neon', '10', '20.180')
        print('clicked')

    def Sodium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(11, 'Sodium', '11', '22.990')
        print('clicked')

    def Magnesium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(12, 'Magnesium', '12', '24.305')
        print('clicked')

    def Aluminum(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(13, 'Aluminum', '13', '26.982')
        print('clicked')

    def Silicon(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(14, 'Silicon', '14', '28.085')
        print('clicked')

    def Phosphorus(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(15, 'Phosphorus', '15', '30.974')
        print('clicked')

    def Sulfur(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(16, 'Sulfur', '16', '32.06')
        print('clicked')

    def Chlorine(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(17, 'Chlorine', '17', '35.45')
        print('clicked')

    def Argon(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(18, 'Argon', '18', '39.948')
        print('clicked')

    def Potassium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(19, 'Potassium', '19', '39.098')
        print('clicked')

    def Calcium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(20, 'Calcium', '20', '40.078')
        print('clicked')

    def Scandium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(21, 'Scandium', '21', '44.956')
        print('clicked')

    def Titanium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(22, 'Titanium', '22', '47.867')
        print('clicked')

    def Vanadium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(23, 'Vanadium', '23', '50.942')
        print('clicked')

    def Chromium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(24, 'Chromium', '24', '51.996')
        print('clicked')

    def Manganese(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(25, 'Manganese', '25', '54.938')
        print('clicked')

    def Iron(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(26, 'Iron', '26', '55.845')
        print('clicked')

    def Cobalt(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(27, 'Cobalt', '27', '58.933')
        print('clicked')

    def Nickel(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(28, 'Nickel', '28', '58.693')
        print('clicked')

    def Copper(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(29, 'Copper', '29', '63.546')
        print('clicked')

    def Zinc(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(30, 'Zinc', '30', '65.38')
        print('clicked')

    def Gallium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(31, 'Gallium', '31', '69.723')
        print('clicked')

    def Germanium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(32, 'Germanium', '32', '72.630')
        print('clicked')

    def Arsenic(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(33, 'Arsenic', '33', '74.922')
        print('clicked')

    def Selenium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(34, 'Selenium', '34', '78.971')
        print('clicked')

    def Bromine(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(35, 'Bromine', '35', '79.904')
        print('clicked')

    def Krypton(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(36, 'Krypton', '36', '83.798')
        print('clicked')

    def Rubidium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(37, 'Rubidium', '37', '85.468')
        print('clicked')

    def Strontium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(38, 'Strontium', '38', '87.62')
        print('clicked')

    def Yttrium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(39, 'Yttrium', '39', '88.906')
        print('clicked')

    def Zirconium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(40, 'Zirconium', '40', '91.224')
        print('clicked')

    def Niobium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(41, 'Niobium', '41', '92.906')
        print('clicked')

    def Molybdenum(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(42, 'Molybdenum', '42', '95.95')
        print('clicked')

    def Technetium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(43, 'Technetium', '43', '(98)')
        print('clicked')

    def Ruthenium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(44, 'Ruthenium', '44', '101.07')
        print('clicked')

    def Rhodium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(45, 'Rhodium', '45', '102.91')
        print('clicked')

    def Palladium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(46, 'Palladium', '46', '106.42')
        print('clicked')

    def Silver(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(47, 'Silver', '47', '107.87')
        print('clicked')

    def Cadmium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(48, 'Cadmium', '48', '112.41')
        print('clicked')

    def Indium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(49, 'Indium', '49', '114.82')
        print('clicked')

    def Tin(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(50, 'Tin', '50', '118.71')
        print('clicked')

    def Antimony(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(51, 'Antimony', '51', '121.76')
        print('clicked')

    def Tellurium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(52, 'Tellurium', '52', '127.60')
        print('clicked')

    def Iodine(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(53, 'Iodine', '53', '126.90')
        print('clicked')

    def Xenon(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(54, 'Xenon', '54', '131.29')
        print('clicked')

    def Cesium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(55, 'Cesium', '55', '132.91')
        print('clicked')

    def Barium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(56, 'Barium', '56', '137.33')
        print('clicked')

    def Lanthanum(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(57, 'Lanthanum', '57', '138.91')
        print('clicked')

    def Cerium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(58, 'Cerium', '58', '140.12')
        print('clicked')

    def Praseodymium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(59, 'Praseodymium', '59', '140.91')
        print('clicked')

    def Neodymium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(60, 'Neodymium', '60', '144.24')
        print('clicked')

    def Promethium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(61, 'Promethium', '61', '(145)')
        print('clicked')

    def Samarium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(62, 'Samarium', '62', '150.36')
        print('clicked')

    def Europium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(63, 'Europium', '63', '151.96')
        print('clicked')

    def Gadolinium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(64, 'Gadolinium', '64', '157.25')
        print('clicked')

    def Terbium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(65, 'Terbium', '65', '158.93')
        print('clicked')

    def Dysprosium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(66, 'Dysprosium', '66', '162.50')
        print('clicked')

    def Holmium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(67, 'Holmium', '67', '164.93')
        print('clicked')

    def Erbium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(68, 'Erbium', '68', '167.26')
        print('clicked')

    def Thulium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(69, 'Thulium', '69', '168.93')
        print('clicked')

    def Ytterbium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(70, 'Ytterbium', '70', '173.04')
        print('clicked')

    def Lutetium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(71, 'Lutetium', '71', '174.97')
        print('clicked')

    def Hafnium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(72, 'Hafnium', '72', '178.49')
        print('clicked')

    def Tantalum(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(73, 'Tantalum', '73', '180.95')
        print('clicked')

    def Tungsten(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(74, 'Tungsten', '74', '183.84')
        print('clicked')

    def Rhenium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(75, 'Rhenium', '75', '186.21')
        print('clicked')

    def Osmium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(76, 'Osmium', '76', '190.23')
        print('clicked')

    def Iridium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(77, 'Iridium', '77', '192.22')
        print('clicked')

    def Platinum(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(78, 'Platinum', '78', '195.08')
        print('clicked')

    def Gold(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(79, 'Gold', '79', '196.97')
        print('clicked')

    def Mercury(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(80, 'Mercury', '80', '200.59')
        print('clicked')

    def Thallium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(81, 'Thallium', '81', '204.38')
        print('clicked')

    def Lead(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(82, 'Lead', '82', '207.2')
        print('clicked')

    def Bismuth(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(83, 'Bismuth', '83', '208.98')
        print('clicked')

    def Polonium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(84, 'Polonium', '84', '(209)')
        print('clicked')

    def Astatine(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(85, 'Astatine', '85', '(210)')
        print('clicked')

    def Radon(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(86, 'Radon', '86', '(222)')
        print('clicked')

    def Francium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(87, 'Francium', '87', '(223)')
        print('clicked')

    def Radium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(88, 'Radium', '88', '(226)')
        print('clicked')

    def Actinium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(89, 'Actinium', '89', '(227)')
        print('clicked')

    def Thorium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(90, 'Thorium', '90', '232.04')
        print('clicked')

    def Protactinium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(91, 'Protactinium', '91', '231.04')
        print('clicked')

    def Uranium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(92, 'Uranium', '92', '238.03')
        print('clicked')

    def Neptunium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(93, 'Neptunium', '93', '(237)')
        print('clicked')

    def Plutonium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(94, 'Plutonium', '94', '(244)')
        print('clicked')

    def Americium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(95, 'Americium', '95', '(243)')
        print('clicked')

    def Curium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(96, 'Curium', '96', '(247)')
        print('clicked')

    def Berkelium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(97, 'Berkelium', '97', '(247)')
        print('clicked')

    def Californium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(98,'Californium','98','251.08')

    def Einsteinium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(99, 'Einsteinium', 'Es', '252')
        print('clicked')

    def Fermium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(100, 'Fermium', 'Fm', '257')
        print('clicked')

    def Mendelevium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(101, 'Mendelevium', 'Md', '258')
        print('clicked')

    def Nobelium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(102, 'Nobelium', 'No', '259')
        print('clicked')

    def Lawrencium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(103, 'Lawrencium', 'Lr', '266')
        print('clicked')

    def Rutherfordium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(104, 'Rutherfordium', 'Rf', '267')
        print('clicked')

    def Dubnium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(105, 'Dubnium', 'Db', '268')
        print('clicked')

    def Seaborgium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(106, 'Seaborgium', 'Sg', '269')
        print('clicked')

    def Bohrium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(107, 'Bohrium', 'Bh', '270')
        print('clicked')

    def Hassium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(108, 'Hassium', 'Hs', '277')
        print('clicked')

    def Meitnerium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(109, 'Meitnerium', 'Mt', '276')
        print('clicked')

    def Darmstadtium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(110, 'Darmstadtium', 'Ds', '281')
        print('clicked')

    def Roentgenium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(111, 'Roentgenium', 'Rg', '280')
        print('clicked')

    def Copernicium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(112, 'Copernicium', 'Cn', '285')
        print('clicked')

    def Nihonium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(113, 'Nihonium', 'Nh', '284')
        print('clicked')

    def Flerovium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(114, 'Flerovium', 'Fl', '289')
        print('clicked')

    def Moscovium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(115, 'Moscovium', 'Mc', '288')
        print('clicked')

    def Livermorium(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(116, 'Livermorium', 'Lv', '293')
        print('clicked')

    def Tennessine(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(117, 'Tennessine', 'Ts', '294')
        print('clicked')

    def Oganesson(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.setup_animation(118, 'Oganesson', 'Og', '294')
        print('clicked')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Custom_Title_UI()
    window.show()
    sys.exit(app.exec_())
