import sys
from PyQt4 import QtCore, QtGui, uic , Qt
import mysql.connector
import time
qtCreatorFile = "untitled.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.bottun()
        self.databes()
        self.unite()



    def unite(self):
        self.setWindowTitle('hemidi benameur app')
    def databes(self):
        self.dbe = mysql.connector.connect(host='localhost' , user='root', password='12345' ,db='mydb')
        self.cur = self.dbe.cursor()

        ######
        sql = ''' SELECT * FROM table_1 '''
        m = self.comboBox.currentText()
        f = [str(m)]

        self.cur.execute(sql)
        data = self.cur.fetchall()
        for e in  data :
            l = e[28]
            self.comboBox.addItem(str(l))






    def bottun(self):
        self.pushButton.clicked.connect(self.add)
        self.pushButton_3.clicked.connect(self.add_l)
        self.pushButton_4.clicked.connect(self.demare)
        self.pushButton_2.clicked.connect(self.tte)
        self.pushButton_5.clicked.connect(self.ubdite)




    def tte(self):
        self.line1.setText(str("{:,}".format(int(self.line1.text()))))
        self.line22.setText(str("{:,}".format(int(self.line22.text()))))
        self.line23.setText(str("{:,}".format(int(self.line23.text()))))
        self.line24.setText(str("{:,}".format(int(self.line24.text()))))
        self.line25.setText(str("{:,}".format(int(self.line25.text()))))
        self.line26.setText(str("{:,}".format(int(self.line26.text()))))
        self.line27.setText(str("{:,}".format(int(self.line27.text()))))
        self.line29.setText(str("{:,}".format(int(self.line29.text()))))
        self.line19.setText(str("{:,}".format(int(self.line19.text()))))
        self.line18.setText(str("{:,}".format(int(self.line18.text()))))
        self.line20.setText(str("{:,}".format(int(self.line20.text()))))
        self.line21.setText(str("{:,}".format(int(self.line21.text()))))



    def add(self):
        line1 = self.line1.text()
        line2 = self.line2.text()
        line3 = self.line3.text()
        line4 = self.line4.text()
        line5 = self.line5.text()
        line6 = self.line6.text()
        line7 = self.line7.text()
        line8 = self.line8.text()
        line9 = self.line9.text()
        line10 = self.line10.text()
        line11 = self.line11.text()
        line12 = self.line12.text()
        line13 = self.line13.text()
        line14 = self.line14.text()
        line15 = self.line15.text()
        line16 = self.line16.text()
        line17 = self.line17.text()
        line18 = self.line18.text()
        line19 = self.line19.text()
        line20 = self.line20.text()
        line21 = self.line21.text()
        line22 = self.line22.text()
        line23 = self.line23.text()
        line24 = self.line24.text()
        line25 = self.line25.text()
        line26 = self.line26.text()
        line27 = self.line27.text()
        line29 = self.line29.text()
        line30 = self.line30.text()
        line31 = self.line31.text()
        #self.cur.execute('''INSERT INTO table(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18,line19,line20,line21,line22,line23,line24,line25,line26,line27,line29,line30) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')''' % (line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18,line19,line20,line21,line22,line23,line24,line25,line26,line27,line29,line30))
        self.cur.execute('''INSERT INTO 
                                  table_1(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18,line19,line20,line21,line22,line23,line24,line25,line26,line27,line29,line30,line31)
                                  VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')''' % (line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18,line19,line20,line21,line22,line23,line24,line25,line26,line27,line29,line30,line31))
        if line1 == '' or  line2 == ''  or  line3 == '' or line4 == '' or line5 or  line6 == '' or line7 == '' or\
                line8 == '' or line9 == '' or line10 == '' or line11 == '' or line12 == '' or line13 == '' or line14 == '' or\
                line15 =='' or line16 == '' or line17 == '' or line18 == '' or line17 == '' or line18 ==  "" or line19 == '' or\
                line20 == '' or line21 == '' or line22 == '' or line23 == '' or line24 == '' or line25 == '' or line26 == '' or\
                line27 == '' or line29 == '' or line30 == '' or line31 == '' or type(line30) != str :



            Qt.QMessageBox.information(self, 'finishd', 'fooo nsit wahda wla nom dola fih fot')
        else  :

            self.dbe.commit()
            m = self.line30.text()
            self.comboBox.addItem(m)
            self.statusbar.showMessage('saved')
            time.sleep(4)
            self.statusbar.showMessage('')

        #####
        ''''
        self.cur.execute(sql)
        data = self.cur.fetchall()
        
        for e in data :
            i = 0
            while i < 30 :
                if e[i] == '' :
                    Qt.QMessageBox.information(self, 'finishd', 'fooo nsit wahda')
                    break

                i = i + 1
        '''





    def ubdite(self):
        line1 = self.line1.text()
        line2 = self.line2.text()
        line3 = self.line3.text()
        line4 = self.line4.text()
        line5 = self.line5.text()
        line6 = self.line6.text()
        line7 = self.line7.text()
        line8 = self.line8.text()
        line9 = self.line9.text()
        line10 = self.line10.text()
        line11 = self.line11.text()
        line12 = self.line12.text()
        line13 = self.line13.text()
        line14 = self.line14.text()
        line15 = self.line15.text()
        line16 = self.line16.text()
        line17 = self.line17.text()
        line18 = self.line18.text()
        line19 = self.line19.text()
        line20 = self.line20.text()
        line21 = self.line21.text()
        line22 = self.line22.text()
        line23 = self.line23.text()
        line24 = self.line24.text()
        line25 = self.line25.text()
        line26 = self.line26.text()
        line27 = self.line27.text()
        line29 = self.line29.text()
        line30 = self.line30.text()
        line31 = self.line31.text()
        # self.cur.execute('''INSERT INTO table(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18,line19,line20,line21,line22,line23,line24,line25,line26,line27,line29,line30) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')''' % (line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18,line19,line20,line21,line22,line23,line24,line25,line26,line27,line29,line30))
        self.cur.execute(''' UPDATE  table_1 
                             SET 
                             line1 = %s,line2 = %s,line3 = %s,line4 = %s,line5 = %s,line6 = %s,line7 = %s,line8 = %s,line9 = %s,line10 = %s,line11 = %s,line12 = %s,line13 = %s,line14 = %s,line15 = %s,line16 = %s,line17 = %s,line18 = %s,line19 = %s,line20 = %s,line21 = %s,line22 = %s,line23 = %s,line24 = %s,line25 = %s,line26 = %s,line27 = %s,line29 = %s,line30 = '%s',line31 = %s 
                             WHERE
                              line30 = '%s' ;
                                           ''' % (line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18,line19,line20,line21,line22,line23,line24,line25,line26,line27,line29,line30,line31,line30) )



        self.dbe.commit()
        self.statusbar.showMessage('saved edite')
        time.sleep(4)
        self.statusbar.showMessage('')

    def add_l(self):



        sql = ''' SELECT * FROM table_1 WHERE line30 = %s '''
        m = self.comboBox.currentText()
        f = [str(m)]

        self.cur.execute(sql, f)
        data = self.cur.fetchall()
        for row in data:
            p =  list(row)

        l = self.lineEdit.text()
        self.lineEdit.setText(l + '+' + str(p[28]))

        self.line1.setText( str(int(p[0]) + int(self.line1.text()) ))
        self.line2.setText( str(int(p[1]) + int(self.line2.text()) ))
        self.line3.setText( str(int(p[2]) + int(self.line3.text()) ))
        self.line4.setText( str(int(p[3]) + int(self.line4.text()) ))
        self.line5.setText( str(int(p[4]) + int(self.line5.text()) ))
        self.line6.setText( str(int(p[5]) + int(self.line6.text()) ))
        self.line7.setText( str(int(p[6]) + int(self.line7.text()) ))
        self.line8.setText( str(int(p[7]) + int(self.line8.text()) ))
        self.line9.setText( str(int(p[8]) + int(self.line9.text()) ))
        self.line10.setText( str(int(p[9]) + int(self.line10.text()) ))
        self.line11.setText( str(int(p[10]) + int(self.line11.text()) ))
        self.line12.setText( str(int(p[11]) + int(self.line12.text()) ))
        self.line13.setText( str(int(p[12]) + int(self.line13.text()) ))
        self.line14.setText( str(int(p[13]) + int(self.line14.text()) ))
        self.line15.setText( str(int(p[14]) + int(self.line15.text()) ))
        self.line16.setText( str(int(p[15]) + int(self.line16.text()) ))
        self.line17.setText( str(int(p[16]) + int(self.line17.text()) ))
        self.line18.setText( str(int(p[17]) + int(self.line18.text()) ))
        self.line19.setText( str(int(p[18]) + int(self.line19.text()) ))
        self.line20.setText( str(int(p[19]) + int(self.line20.text()) ))
        self.line21.setText( str(int(p[20]) + int(self.line21.text()) ))
        self.line22.setText( str(int(p[21]) + int(self.line22.text()) ))
        self.line23.setText( str(int(p[22]) + int(self.line23.text()) ))
        self.line24.setText( str(int(p[23]) + int(self.line24.text()) ))
        self.line25.setText( str(int(p[24]) + int(self.line25.text()) ))
        self.line26.setText( str(int(p[25]) + int(self.line26.text()) ))
        self.line27.setText( str(int(p[26]) + int(self.line27.text()) ))
        self.line29.setText( str(int(p[27]) + int(self.line29.text()) ))
        self.line30.setText(str(p[28]))
        self.line31.setText(str(p[29]))

        m = self.lineEdit.text()
        p = m[2:].split('+')
        self.lcdNumber.display(len(p))














    def demare(self):
        self.line1.setText('0')
        self.line2.setText('0')
        self.line3.setText('0')
        self.line4.setText('0')
        self.line5.setText('0')
        self.line6.setText('0')
        self.line7.setText('0')
        self.line8.setText('0')
        self.line9.setText('0')
        self.line10.setText('0')
        self.line11.setText('0')
        self.line12.setText('0')
        self.line13.setText('0')
        self.line14.setText('0')
        self.line15.setText('0')
        self.line16.setText('0')
        self.line17.setText('0')
        self.line18.setText('0')
        self.line19.setText('0')
        self.line20.setText('0')
        self.line21.setText('0')
        self.line22.setText('0')
        self.line23.setText('0')
        self.line24.setText('0')
        self.line25.setText('0')
        self.line26.setText('0')
        self.line27.setText('0')
        self.line29.setText('0')
        self.lineEdit.setText('')
        self.lcdNumber.display(0)



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())