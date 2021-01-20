# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '\ui\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from copy import deepcopy
import osmnx as ox
import pylab

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from matplotlib import patches

from Geocoder import GeocodingException
from NavigationSystem import NavigationSystem
from OwnerState import OwnerStateException


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(866, 521)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.add_owner_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_owner_button.setGeometry(QtCore.QRect(30, 270, 61, 23))
        self.add_owner_button.setObjectName("add_owner_button")
        self.remove_owner_button = QtWidgets.QPushButton(self.centralwidget)
        self.remove_owner_button.setGeometry(QtCore.QRect(30, 310, 61, 23))
        self.remove_owner_button.setObjectName("remove_owner_button")
        self.free_owners_list_widget = QtWidgets.QListWidget(self.centralwidget)
        self.free_owners_list_widget.setGeometry(QtCore.QRect(30, 70, 149, 171))
        self.free_owners_list_widget.setObjectName("free_owners_list_widget")
        self.busy_owners_list_widget = QtWidgets.QListWidget(self.centralwidget)
        self.busy_owners_list_widget.setGeometry(QtCore.QRect(200, 70, 149, 171))
        self.busy_owners_list_widget.setObjectName("busy_owners_list_widget")
        self.free_owners_label = QtWidgets.QLabel(self.centralwidget)
        self.free_owners_label.setGeometry(QtCore.QRect(30, 30, 131, 16))
        self.free_owners_label.setObjectName("free_owners_label")
        self.busy_owners_label = QtWidgets.QLabel(self.centralwidget)
        self.busy_owners_label.setGeometry(QtCore.QRect(200, 30, 131, 16))
        self.busy_owners_label.setObjectName("busy_owners_label")
        self.owner_info_label = QtWidgets.QLabel(self.centralwidget)
        self.owner_info_label.setGeometry(QtCore.QRect(440, 30, 61, 16))
        self.owner_info_label.setObjectName("owner_info_label")
        self.owner_type_label = QtWidgets.QLabel(self.centralwidget)
        self.owner_type_label.setGeometry(QtCore.QRect(440, 70, 47, 13))
        self.owner_type_label.setObjectName("owner_type_label")
        self.owner_location_label = QtWidgets.QLabel(self.centralwidget)
        self.owner_location_label.setGeometry(QtCore.QRect(440, 100, 101, 16))
        self.owner_location_label.setObjectName("owner_location_label")
        self.set_destination_button = QtWidgets.QPushButton(self.centralwidget)
        self.set_destination_button.setGeometry(QtCore.QRect(690, 420, 161, 23))
        self.set_destination_button.setObjectName("set_destination_button")
        self.next_target_label = QtWidgets.QLabel(self.centralwidget)
        self.next_target_label.setGeometry(QtCore.QRect(440, 160, 191, 16))
        self.next_target_label.setObjectName("next_target_label")
        self.nav_tip_label = QtWidgets.QLabel(self.centralwidget)
        self.nav_tip_label.setGeometry(QtCore.QRect(440, 220, 131, 16))
        self.nav_tip_label.setObjectName("nav_tip_label")
        self.destination_address_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.destination_address_line_edit.setGeometry(QtCore.QRect(440, 380, 411, 20))
        self.destination_address_line_edit.setObjectName("destination_address_line_edit")
        self.destination_address_label = QtWidgets.QLabel(self.centralwidget)
        self.destination_address_label.setGeometry(QtCore.QRect(440, 350, 47, 13))
        self.destination_address_label.setObjectName("destination_address_label")
        self.owner_type_output = QtWidgets.QLabel(self.centralwidget)
        self.owner_type_output.setGeometry(QtCore.QRect(480, 70, 341, 16))
        self.owner_type_output.setText("")
        self.owner_type_output.setObjectName("owner_type_output")
        self.owner_location_output = QtWidgets.QLabel(self.centralwidget)
        self.owner_location_output.setGeometry(QtCore.QRect(440, 130, 381, 16))
        self.owner_location_output.setText("")
        self.owner_location_output.setObjectName("owner_location_output")
        self.owner_location_output.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.owner_nav_tip_output = QtWidgets.QLabel(self.centralwidget)
        self.owner_nav_tip_output.setGeometry(QtCore.QRect(440, 240, 381, 16))
        self.owner_nav_tip_output.setText("")
        self.owner_nav_tip_output.setObjectName("owner_nav_tip_output")
        self.owner_next_target_output = QtWidgets.QLabel(self.centralwidget)
        self.owner_next_target_output.setGeometry(QtCore.QRect(440, 190, 381, 16))
        self.owner_next_target_output.setText("")
        self.owner_next_target_output.setObjectName("owner_next_target_output")
        self.owner_next_target_output.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.draw_map_button = QtWidgets.QPushButton(self.centralwidget)
        self.draw_map_button.setGeometry(QtCore.QRect(440, 270, 121, 23))
        self.draw_map_button.setObjectName("draw_map_button")
        self.geocoding_label = QtWidgets.QLabel(self.centralwidget)
        self.geocoding_label.setGeometry(QtCore.QRect(30, 350, 101, 16))
        self.geocoding_label.setObjectName("geocoding_label")
        self.geocoding_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.geocoding_line_edit.setGeometry(QtCore.QRect(30, 380, 381, 20))
        self.geocoding_line_edit.setObjectName("geocoding_line_edit")
        self.find_coordinates_button = QtWidgets.QPushButton(self.centralwidget)
        self.find_coordinates_button.setGeometry(QtCore.QRect(30, 420, 115, 23))
        self.find_coordinates_button.setObjectName("find_coordinates_button")
        self.find_address_button = QtWidgets.QPushButton(self.centralwidget)
        self.find_address_button.setGeometry(QtCore.QRect(160, 420, 75, 23))
        self.find_address_button.setObjectName("find_address_button")
        self.result_label = QtWidgets.QLabel(self.centralwidget)
        self.result_label.setGeometry(QtCore.QRect(30, 460, 71, 16))
        self.result_label.setObjectName("result_label")
        self.geocoding_output = QtWidgets.QLabel(self.centralwidget)
        self.geocoding_output.setGeometry(QtCore.QRect(30, 480, 811, 16))
        self.geocoding_output.setText("")
        self.geocoding_output.setObjectName("geocoding_output")
        self.geocoding_output.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.owner_types_box = QtWidgets.QGroupBox(self.centralwidget)
        self.owner_types_box.setGeometry(QtCore.QRect(110, 270, 251, 21))
        self.owner_types_box.setTitle("")
        self.owner_types_box.setObjectName("owner_types_box")
        self.biker_radio_button = QtWidgets.QRadioButton(self.owner_types_box)
        self.biker_radio_button.setGeometry(QtCore.QRect(0, 0, 101, 17))
        self.biker_radio_button.setChecked(True)
        self.biker_radio_button.setObjectName("biker_radio_button")
        self.pedestrian_radio_button = QtWidgets.QRadioButton(self.owner_types_box)
        self.pedestrian_radio_button.setGeometry(QtCore.QRect(100, 0, 101, 17))
        self.pedestrian_radio_button.setObjectName("pedestrian_radio_button")
        self.driver_radio_button = QtWidgets.QRadioButton(self.owner_types_box)
        self.driver_radio_button.setGeometry(QtCore.QRect(180, 0, 101, 17))
        self.driver_radio_button.setObjectName("driver_radio_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Attributes
        self.__system = NavigationSystem()
        self.__current_owner = None

        # Connections
        # ДобавлениеЮ удаление владельцев
        self.add_owner_button.clicked.connect(self.add_owner)
        self.remove_owner_button.clicked.connect(self.delete_owner)

        # Выбор владельца из списка
        self.free_owners_list_widget.itemSelectionChanged.connect(self.free_owners_selection)
        self.busy_owners_list_widget.itemSelectionChanged.connect(self.busy_owners_selection)

        #  Геокодирование
        self.find_coordinates_button.clicked.connect(self.find_coordinates)
        self.find_address_button.clicked.connect(self.find_address)

        # Задание точки
        self.set_destination_button.clicked.connect(self.set_destination)

        # Движение
        self.timer = QTimer()
        self.timer.timeout.connect(self.perform_move)
        one_move_time = 1000
        self.timer.start(one_move_time)

        # Отображение карты с маршрутом и положением
        self.draw_map_button.clicked.connect(self.show_on_map)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NavigationSystem"))
        self.add_owner_button.setText(_translate("MainWindow", "Добавить"))
        self.remove_owner_button.setText(_translate("MainWindow", "Удалить"))
        self.free_owners_label.setText(_translate("MainWindow", "Свободные владельцы:"))
        self.busy_owners_label.setText(_translate("MainWindow", "Занятые владельцы:"))
        self.owner_info_label.setText(_translate("MainWindow", "Владелец:"))
        self.owner_type_label.setText(_translate("MainWindow", "Тип:"))
        self.owner_location_label.setText(_translate("MainWindow", "Местоположение:"))
        self.set_destination_button.setText(_translate("MainWindow", "Задать точку назначения"))
        self.next_target_label.setText(_translate("MainWindow", "Следующая промежуточная точка:"))
        self.nav_tip_label.setText(_translate("MainWindow", "Подсказка навигатора:"))
        self.destination_address_label.setText(_translate("MainWindow", "Адрес:"))
        self.draw_map_button.setText(_translate("MainWindow", "Показать на карте"))
        self.geocoding_label.setText(_translate("MainWindow", "Геокодирование:"))
        self.find_coordinates_button.setText(_translate("MainWindow", "Найти координаты"))
        self.find_address_button.setText(_translate("MainWindow", "Найти адрес"))
        self.result_label.setText(_translate("MainWindow", "Результат:"))
        self.biker_radio_button.setText(_translate("MainWindow", "Велосипедист"))
        self.pedestrian_radio_button.setText(_translate("MainWindow", "Пешеход"))
        self.driver_radio_button.setText(_translate("MainWindow", "Водитель"))

    # Нажатие на кнопку Добавить
    def add_owner(self):
        # Получаем выбранный тип
        if self.biker_radio_button.isChecked():
            owner_type = "biker"
        elif self.pedestrian_radio_button.isChecked():
            owner_type = "pedestrian"
        else:
            owner_type = "driver"

        # Добавляем в систему
        self.__system.add_owner(owner_type)
        # Обновляем спсики
        self.update_free_owners_list()
        self.update_busy_owners_list()

    # Обновление спсика свободных владельцев
    def update_free_owners_list(self):
        self.free_owners_list_widget.clear()

        free_owners = self.__system.get_free_owners()

        for owner in free_owners:
            item = QtWidgets.QListWidgetItem()
            item.setText(str(owner))
            self.free_owners_list_widget.addItem(item)

    # Обновление спсика занятых владельцев
    def update_busy_owners_list(self):
        self.busy_owners_list_widget.clear()

        busy_owners = self.__system.get_busy_owners()

        for owner in busy_owners:
            item = QtWidgets.QListWidgetItem()
            item.setText(str(owner))
            self.busy_owners_list_widget.addItem(item)

    # Выбор из списка свободных владельцев
    def free_owners_selection(self):
        # Убираем выбранный элемент из списка занятых
        self.busy_owners_list_widget.clearSelection()

        # Получаемый выбранного владельца
        index = self.free_owners_list_widget.currentRow()
        owners = self.__system.get_free_owners()

        if owners and index < len(owners):
            self.__current_owner = owners[index]

        # Обновляем поля с информацией
        self.update_owner_info()

    # Выбор из списка занятых владельцев
    def busy_owners_selection(self):
        # Убираем выбранный элемент из списка свободных
        self.free_owners_list_widget.clearSelection()

        # Получаемый выбранного владельца
        index = self.busy_owners_list_widget.currentRow()
        owners = self.__system.get_busy_owners()

        if owners and index < len(owners):
            self.__current_owner = owners[index]

        # Обновляем поля с информацией
        self.update_owner_info()

    # Заполнение лейблов с информацией о владельце
    def update_owner_info(self):
        # Если выбран владелец
        if self.__current_owner:
            owner_type = type(self.__current_owner).__name__
            location = self.__system.get_location(self.__current_owner)
            next_target = self.__system.get_current_target_point(self.__current_owner)
            navigation_tip = self.__system.get_current_tip(self.__current_owner)

            self.owner_type_output.setText(owner_type)
            self.owner_location_output.setText(f"{location[1]} {location[0]}")

            if next_target is not None:
                self.owner_next_target_output.setText(f"{next_target[1]} {next_target[0]}")
            else:
                self.owner_next_target_output.setText("Не задано")

            self.owner_nav_tip_output.setText(navigation_tip)
        else:
            self.owner_type_output.setText("-")
            self.owner_location_output.setText("-")
            self.owner_next_target_output.setText("-")
            self.owner_nav_tip_output.setText("-")

    # Удаление выбранного владельца
    def delete_owner(self):
        self.__system.remove_owner(self.__current_owner)
        self.__current_owner = None

        self.update_free_owners_list()
        self.update_busy_owners_list()
        self.update_owner_info()

    # Поиск координат по адресу
    def find_coordinates(self):
        address = self.geocoding_line_edit.text()

        try:
            coordinates = self.__system.find_coordinates(address)
            self.geocoding_output.setText(f"{coordinates[1]} {coordinates[0]}")
        except GeocodingException as ex:
            QtWidgets.QMessageBox.warning(MainWindow, "Неверный адрес",
                                          "Адрес должен содержать 'Барнаул, Россия'.")

    # Поиск адреса по координатам
    def find_address(self):
        try:
            coordinates = self.geocoding_line_edit.text().split()
            latitude = float(coordinates[0])
            longitude = float(coordinates[1])

            address = self.__system.find_address(longitude, latitude)
            self.geocoding_output.setText(address)
        except GeocodingException as ex:
            QtWidgets.QMessageBox.warning(MainWindow, "Неверный запрос",
                                          "Объект должен находиться в городе Барнауле.")
        except IndexError as ex:
            QtWidgets.QMessageBox.warning(MainWindow, "Неверный запрос",
                                          "Неверно заданы координаты.")

    # Задание точки назначения
    def set_destination(self):
        # Проверяем выбран ли владелец
        if self.__current_owner is None:
            QtWidgets.QMessageBox.warning(MainWindow, "Не выбран владелец",
                                          "Сначала выберите владельца, которому хотите назначить точку.")
            return

        address = self.destination_address_line_edit.text()

        # Задаем точку
        try:
            self.__system.give_order(self.__current_owner, address)
        except GeocodingException:
            QtWidgets.QMessageBox.warning(MainWindow, "Неверный адрес",
                                          "Адрес должен содержать 'Барнаул, Россия'.")
        except OwnerStateException:
            QtWidgets.QMessageBox.warning(MainWindow, "Нельзя задать точку",
                                          "Выбранный владелец уже движется.")

        self.update_free_owners_list()
        self.update_busy_owners_list()

    # Совершить движение всех владельцев
    def perform_move(self):
        # Движение
        self.__system.perform_move()

        # Обновление списков и информации о владельце
        self.update_owner_info()
        self.update_free_owners_list()
        self.update_busy_owners_list()

    # Показать на карте текущее положение и оставщийся маршрут
    def show_on_map(self):
        # Проверяем выбран ли владелец
        if self.__current_owner is None:
            QtWidgets.QMessageBox.warning(MainWindow, "Не выбран владелец",
                                          "Сначала выберите владельца, которого хотите увидеть на карте.")
            return

        # Получаем оставщийся путь
        path = self.__system.get_path(self.__current_owner)

        # Проверяем задан ли путь
        if path is None:
            QtWidgets.QMessageBox.warning(MainWindow, "Нет пути",
                                          "Сначала задайте точку назначения.")
            return

        path = deepcopy(path)
        path.pop()
        path = [node['id'] for node in path]

        # Получаем граф дорог
        graph = self.__system.get_graph(self.__current_owner)

        # Наносим на рисунок граф дорог и путь
        fig, ax = ox.plot_graph_route(graph, path, node_size=1, route_color="cyan")
        path_patch = patches.Patch(color="cyan", label="Маршрут движения")

        # Наносим текущий промежуток пути
        location = self.__system.get_location(self.__current_owner)
        target_point = self.__system.get_current_target_point(self.__current_owner)

        x = [location[0], target_point[0]]
        y = [location[1], target_point[1]]
        ax.plot(x, y, color="cyan", linestyle="dashed")

        # Наносим текущее положение
        ax.scatter(*location, color="red", label="Текущее положение")

        # Наносим точку назначения
        destination = self.__system.get_destination_point(self.__current_owner)
        ax.scatter(*destination, color="green", label="Точка назначения")

        # Добавляем легенду с обозначениями
        handles, labels = ax.get_legend_handles_labels()
        handles.append(path_patch)
        ax.legend(handles=handles)

        # Показываем мзображение
        fig.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())