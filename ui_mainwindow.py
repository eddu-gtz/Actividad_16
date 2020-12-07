# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(799, 551)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionOrdenar_id = QAction(MainWindow)
        self.actionOrdenar_id.setObjectName(u"actionOrdenar_id")
        self.actionOrdenar_distancia = QAction(MainWindow)
        self.actionOrdenar_distancia.setObjectName(u"actionOrdenar_distancia")
        self.actionOrdenar_velocidad = QAction(MainWindow)
        self.actionOrdenar_velocidad.setObjectName(u"actionOrdenar_velocidad")
        self.actionGrafo = QAction(MainWindow)
        self.actionGrafo.setObjectName(u"actionGrafo")
        self.actionRecorrido_en_Profuncidad_Amplitud = QAction(MainWindow)
        self.actionRecorrido_en_Profuncidad_Amplitud.setObjectName(u"actionRecorrido_en_Profuncidad_Amplitud")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.id_spinBox = QSpinBox(self.groupBox)
        self.id_spinBox.setObjectName(u"id_spinBox")
        self.id_spinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.id_spinBox.setProperty("showGroupSeparator", False)
        self.id_spinBox.setMinimum(-5000)
        self.id_spinBox.setMaximum(5000)
        self.id_spinBox.setSingleStep(1)
        self.id_spinBox.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)

        self.gridLayout.addWidget(self.id_spinBox, 0, 1, 1, 2)

        self.agregar_inicio_pushButton = QPushButton(self.groupBox)
        self.agregar_inicio_pushButton.setObjectName(u"agregar_inicio_pushButton")
        self.agregar_inicio_pushButton.setMinimumSize(QSize(200, 0))
        font = QFont()
        font.setPointSize(10)
        self.agregar_inicio_pushButton.setFont(font)
        self.agregar_inicio_pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.agregar_inicio_pushButton, 9, 0, 1, 3)

        self.agregar_final_pushButton = QPushButton(self.groupBox)
        self.agregar_final_pushButton.setObjectName(u"agregar_final_pushButton")
        self.agregar_final_pushButton.setMinimumSize(QSize(200, 0))
        self.agregar_final_pushButton.setFont(font)
        self.agregar_final_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.agregar_final_pushButton.setAutoFillBackground(False)
        self.agregar_final_pushButton.setFlat(False)

        self.gridLayout.addWidget(self.agregar_final_pushButton, 8, 0, 1, 3)

        self.salida = QPlainTextEdit(self.groupBox)
        self.salida.setObjectName(u"salida")
        self.salida.setFont(font)

        self.gridLayout.addWidget(self.salida, 0, 3, 11, 1)

        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_7 = QGridLayout(self.groupBox_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(25, 16777215))
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_4, 0, 0, 1, 1)

        self.destino_y_spinBox = QSpinBox(self.groupBox_3)
        self.destino_y_spinBox.setObjectName(u"destino_y_spinBox")
        self.destino_y_spinBox.setMaximum(500)

        self.gridLayout_7.addWidget(self.destino_y_spinBox, 0, 3, 1, 1)

        self.destino_x_spinBox = QSpinBox(self.groupBox_3)
        self.destino_x_spinBox.setObjectName(u"destino_x_spinBox")
        self.destino_x_spinBox.setMaximum(500)

        self.gridLayout_7.addWidget(self.destino_x_spinBox, 0, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(25, 16777215))
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_5, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.groupBox_3, 2, 0, 2, 3)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(250, 0))
        self.gridLayout_6 = QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(25, 16777215))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_2, 0, 0, 1, 1)

        self.origen_x_spinBox = QSpinBox(self.groupBox_2)
        self.origen_x_spinBox.setObjectName(u"origen_x_spinBox")
        self.origen_x_spinBox.setMaximum(500)

        self.gridLayout_6.addWidget(self.origen_x_spinBox, 0, 1, 1, 1)

        self.origen_y_spinBox = QSpinBox(self.groupBox_2)
        self.origen_y_spinBox.setObjectName(u"origen_y_spinBox")
        self.origen_y_spinBox.setMaximum(500)

        self.gridLayout_6.addWidget(self.origen_y_spinBox, 0, 3, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(25, 16777215))
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_3, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 3)

        self.mostrar_pushButton = QPushButton(self.groupBox)
        self.mostrar_pushButton.setObjectName(u"mostrar_pushButton")
        self.mostrar_pushButton.setMinimumSize(QSize(200, 0))
        self.mostrar_pushButton.setFont(font)
        self.mostrar_pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.mostrar_pushButton, 10, 0, 1, 3)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.line_2 = QFrame(self.groupBox)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 7, 0, 1, 3)

        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_8 = QGridLayout(self.groupBox_4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_8.addWidget(self.label_7, 0, 0, 1, 1)

        self.red_spinBox = QSpinBox(self.groupBox_4)
        self.red_spinBox.setObjectName(u"red_spinBox")
        self.red_spinBox.setMinimumSize(QSize(90, 0))
        self.red_spinBox.setMaximum(255)

        self.gridLayout_8.addWidget(self.red_spinBox, 0, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_8.addWidget(self.label_9, 1, 0, 1, 1)

        self.green_spinBox = QSpinBox(self.groupBox_4)
        self.green_spinBox.setObjectName(u"green_spinBox")
        self.green_spinBox.setMinimumSize(QSize(90, 0))
        self.green_spinBox.setMaximum(255)

        self.gridLayout_8.addWidget(self.green_spinBox, 1, 1, 1, 1)

        self.label_10 = QLabel(self.groupBox_4)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_8.addWidget(self.label_10, 2, 0, 1, 1)

        self.blue_spinBox = QSpinBox(self.groupBox_4)
        self.blue_spinBox.setObjectName(u"blue_spinBox")
        self.blue_spinBox.setMinimumSize(QSize(90, 0))
        self.blue_spinBox.setMaximum(255)

        self.gridLayout_8.addWidget(self.blue_spinBox, 2, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_4, 6, 0, 1, 3)

        self.velocidad_spinBox = QSpinBox(self.groupBox)
        self.velocidad_spinBox.setObjectName(u"velocidad_spinBox")
        self.velocidad_spinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.velocidad_spinBox.setMinimum(-5000)
        self.velocidad_spinBox.setMaximum(5000)

        self.gridLayout.addWidget(self.velocidad_spinBox, 4, 1, 1, 2)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.search_id_lineEdit = QLineEdit(self.tab_2)
        self.search_id_lineEdit.setObjectName(u"search_id_lineEdit")
        self.search_id_lineEdit.setFont(font)

        self.gridLayout_4.addWidget(self.search_id_lineEdit, 1, 0, 1, 1)

        self.search_pushButton = QPushButton(self.tab_2)
        self.search_pushButton.setObjectName(u"search_pushButton")
        self.search_pushButton.setFont(font)

        self.gridLayout_4.addWidget(self.search_pushButton, 1, 1, 1, 1)

        self.show_table_pushButton = QPushButton(self.tab_2)
        self.show_table_pushButton.setObjectName(u"show_table_pushButton")
        self.show_table_pushButton.setFont(font)

        self.gridLayout_4.addWidget(self.show_table_pushButton, 1, 2, 1, 1)

        self.table = QTableWidget(self.tab_2)
        self.table.setObjectName(u"table")
        self.table.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.table.setAutoFillBackground(False)

        self.gridLayout_4.addWidget(self.table, 0, 0, 1, 3)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_5 = QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.graphicsView = QGraphicsView(self.tab_3)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_5.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.draw_pushButton = QPushButton(self.tab_3)
        self.draw_pushButton.setObjectName(u"draw_pushButton")
        self.draw_pushButton.setFont(font)

        self.gridLayout_5.addWidget(self.draw_pushButton, 1, 0, 1, 1)

        self.clean_drawing_pushButton = QPushButton(self.tab_3)
        self.clean_drawing_pushButton.setObjectName(u"clean_drawing_pushButton")
        self.clean_drawing_pushButton.setFont(font)

        self.gridLayout_5.addWidget(self.clean_drawing_pushButton, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 799, 21))
        self.menuAbrir = QMenu(self.menubar)
        self.menuAbrir.setObjectName(u"menuAbrir")
        self.menuOrdenar = QMenu(self.menubar)
        self.menuOrdenar.setObjectName(u"menuOrdenar")
        self.menuGrafo = QMenu(self.menubar)
        self.menuGrafo.setObjectName(u"menuGrafo")
        self.menuAlgoritmos = QMenu(self.menubar)
        self.menuAlgoritmos.setObjectName(u"menuAlgoritmos")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAbrir.menuAction())
        self.menubar.addAction(self.menuOrdenar.menuAction())
        self.menubar.addAction(self.menuGrafo.menuAction())
        self.menubar.addAction(self.menuAlgoritmos.menuAction())
        self.menuAbrir.addAction(self.actionAbrir)
        self.menuAbrir.addAction(self.actionGuardar)
        self.menuOrdenar.addAction(self.actionOrdenar_id)
        self.menuOrdenar.addAction(self.actionOrdenar_distancia)
        self.menuOrdenar.addAction(self.actionOrdenar_velocidad)
        self.menuGrafo.addAction(self.actionGrafo)
        self.menuAlgoritmos.addAction(self.actionRecorrido_en_Profuncidad_Amplitud)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.agregar_final_pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Registro Particulas", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionOrdenar_id.setText(QCoreApplication.translate("MainWindow", u"Por id - ascendente", None))
        self.actionOrdenar_distancia.setText(QCoreApplication.translate("MainWindow", u"Por distancia - descendente", None))
        self.actionOrdenar_velocidad.setText(QCoreApplication.translate("MainWindow", u"Por velocidad - ascendente", None))
        self.actionGrafo.setText(QCoreApplication.translate("MainWindow", u"Grafo", None))
#if QT_CONFIG(shortcut)
        self.actionGrafo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+G", None))
#endif // QT_CONFIG(shortcut)
        self.actionRecorrido_en_Profuncidad_Amplitud.setText(QCoreApplication.translate("MainWindow", u"Recorrido en Profuncidad/Amplitud", None))
#if QT_CONFIG(shortcut)
        self.actionRecorrido_en_Profuncidad_Amplitud.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Particula", None))
        self.agregar_inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al inicio", None))
        self.agregar_final_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al final", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Destino", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Origen", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Id", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Color (RGB):", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.search_id_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar por ID de la particula", None))
        self.search_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.show_table_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.draw_pushButton.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.clean_drawing_pushButton.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Dibujo", None))
        self.menuAbrir.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuOrdenar.setTitle(QCoreApplication.translate("MainWindow", u"Ordenar", None))
        self.menuGrafo.setTitle(QCoreApplication.translate("MainWindow", u"Ver", None))
        self.menuAlgoritmos.setTitle(QCoreApplication.translate("MainWindow", u"Algoritmos", None))
    # retranslateUi

