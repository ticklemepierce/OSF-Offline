# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Preferences(object):
    def setupUi(self, Preferences):
        Preferences.setObjectName("Preferences")
        Preferences.resize(590, 320)
        self.verticalLayoutWidget = QtWidgets.QWidget(Preferences)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 591, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.verticalLayoutWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 551, 80))
        self.groupBox.setObjectName("groupBox")
        self.desktopNotifications = QtWidgets.QCheckBox(self.groupBox)
        self.desktopNotifications.setGeometry(QtCore.QRect(10, 20, 541, 22))
        self.desktopNotifications.setChecked(True)
        self.desktopNotifications.setObjectName("desktopNotifications")
        self.startOnStartup = QtWidgets.QCheckBox(self.groupBox)
        self.startOnStartup.setGeometry(QtCore.QRect(10, 40, 541, 22))
        self.startOnStartup.setChecked(True)
        self.startOnStartup.setObjectName("startOnStartup")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 110, 561, 61))
        self.groupBox_6.setObjectName("groupBox_6")
        self.changeFolderButton = QtWidgets.QPushButton(self.groupBox_6)
        self.changeFolderButton.setGeometry(QtCore.QRect(440, 20, 99, 31))
        self.changeFolderButton.setObjectName("changeFolderButton")
        self.containingFolderTextEdit = QtWidgets.QTextEdit(self.groupBox_6)
        self.containingFolderTextEdit.setGeometry(QtCore.QRect(20, 20, 331, 31))
        self.containingFolderTextEdit.setObjectName("containingFolderTextEdit")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 581, 51))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(280, 50, 561, 51))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(30, 16, 411, 31))
        self.label.setObjectName("label")
        self.accountLogOutButton = QtWidgets.QPushButton(self.groupBox_2)
        self.accountLogOutButton.setGeometry(QtCore.QRect(460, 10, 99, 31))
        self.accountLogOutButton.setObjectName("accountLogOutButton")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 70, 561, 211))
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 30, 541, 81))
        self.groupBox_5.setObjectName("groupBox_5")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton.setGeometry(QtCore.QRect(30, 20, 117, 22))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_2.setGeometry(QtCore.QRect(30, 40, 117, 22))
        self.radioButton_2.setObjectName("radioButton_2")
        self.changeFolderButton_2 = QtWidgets.QPushButton(self.groupBox_5)
        self.changeFolderButton_2.setGeometry(QtCore.QRect(440, 20, 99, 31))
        self.changeFolderButton_2.setObjectName("changeFolderButton_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_7.setGeometry(QtCore.QRect(50, 40, 441, 181))
        self.groupBox_7.setObjectName("groupBox_7")
        self.logInButton = QtWidgets.QPushButton(self.groupBox_7)
        self.logInButton.setGeometry(QtCore.QRect(330, 150, 99, 27))
        self.logInButton.setObjectName("logInButton")
        self.emailEdit = QtWidgets.QLineEdit(self.groupBox_7)
        self.emailEdit.setGeometry(QtCore.QRect(160, 30, 261, 27))
        self.emailEdit.setObjectName("emailEdit")
        self.passwordEdit = QtWidgets.QLineEdit(self.groupBox_7)
        self.passwordEdit.setGeometry(QtCore.QRect(160, 70, 261, 27))
        self.passwordEdit.setObjectName("passwordEdit")
        self.label_3 = QtWidgets.QLabel(self.groupBox_7)
        self.label_3.setGeometry(QtCore.QRect(70, 26, 61, 31))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_7)
        self.label_5.setGeometry(QtCore.QRect(70, 70, 81, 31))
        self.label_5.setObjectName("label_5")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.treeWidget = QtWidgets.QTreeWidget(self.tab_4)
        self.treeWidget.setGeometry(QtCore.QRect(10, 40, 561, 221))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setMouseTracking(False)
        self.treeWidget.setAcceptDrops(False)
        self.treeWidget.setAnimated(False)
        self.treeWidget.setWordWrap(True)
        self.treeWidget.setHeaderHidden(False)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setTextAlignment(0, QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.treeWidget.headerItem().setTextAlignment(1, QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.treeWidget.header().setCascadingSectionResizes(True)
        self.treeWidget.header().setDefaultSectionSize(200)
        self.treeWidget.header().setHighlightSections(True)
        self.label_2 = QtWidgets.QLabel(self.tab_4)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 561, 17))
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_5)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 20, 551, 251))
        self.textEdit_2.setObjectName("textEdit_2")
        self.tabWidget.addTab(self.tab_5, "")
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Preferences)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Preferences)

    def retranslateUi(self, Preferences):
        _translate = QtCore.QCoreApplication.translate
        Preferences.setWindowTitle(_translate("Preferences", "Preferences"))
        self.groupBox.setTitle(_translate("Preferences", "System"))
        self.desktopNotifications.setText(_translate("Preferences", "Show Desktop Notifications"))
        self.startOnStartup.setText(_translate("Preferences", "Start OSF Offline on Computer Startup"))
        self.groupBox_6.setTitle(_translate("Preferences", "Choose Folder to Place Project in "))
        self.changeFolderButton.setText(_translate("Preferences", "Change"))
        self.containingFolderTextEdit.setHtml(_translate("Preferences", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">/home/himanshu/somefolder/My Project</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Preferences", "General"))
        self.groupBox_2.setTitle(_translate("Preferences", "Account"))
        self.groupBox_3.setTitle(_translate("Preferences", "Account"))
        self.label.setText(_translate("Preferences", "User name"))
        self.accountLogOutButton.setText(_translate("Preferences", "Log Out"))
        self.groupBox_4.setTitle(_translate("Preferences", "Project"))
        self.groupBox_5.setTitle(_translate("Preferences", "Choose Project to Sync With"))
        self.radioButton.setText(_translate("Preferences", "Project A"))
        self.radioButton_2.setText(_translate("Preferences", "Project B"))
        self.changeFolderButton_2.setText(_translate("Preferences", "Change"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Preferences", "OSF (logged in)"))
        self.groupBox_7.setTitle(_translate("Preferences", "Log in"))
        self.logInButton.setText(_translate("Preferences", "Log In"))
        self.label_3.setText(_translate("Preferences", "Email"))
        self.label_5.setText(_translate("Preferences", "Password"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Preferences", "OSF (logged out)"))
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.headerItem().setText(0, _translate("Preferences", "Component, Folder, or File"))
        self.treeWidget.headerItem().setText(1, _translate("Preferences", "Priority"))
        self.label_2.setText(_translate("Preferences", "Priority Items will be given priority when syncing"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Preferences", "Priority Syncing"))
        self.textEdit_2.setHtml(_translate("Preferences", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. This is copyright info. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">© Center for Open Science</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Preferences", "About"))

