import os
import psycopg2

def showallMenu():
    DATABASE_URL = os.environ['DATABASE_URL']
    connection_db = psycopg2.connect(DATABASE_URL,sslmode='require')
    cursor = connection_db.cursor()
    SQL_cmd = f"""SELECT * FROM menu ORDER by menu_id;"""
    cursor.execute(SQL_cmd)
    connection_db.commit()
    raws = cursor.fetchall()
    data = []
    for raw in raws:
        data.append(raw)
    
    cursor.close()
    connection_db.close()
    return data

def queryItem(keyword):
    DATABASE_URL = os.environ['DATABASE_URL']
    connection_db = psycopg2.connect(DATABASE_URL,sslmode='require')
    cursor = connection_db.cursor()
    SQL_cmd = f"""SELECT * FROM menu WHERE menuname = %s;"""
    cursor.execute(SQL_cmd,[keyword])
    connection_db.commit()
    raws = cursor.fetchall()
    data = []
    for raw in raws:
        data.append(raw)
    
    cursor.close()
    connection_db.close()
    return data

def addMenu(text):
    DATABASE_URL = os.environ['DATABASE_URL']
    connection_db = psycopg2.connect(DATABASE_URL,sslmode='require')
    cursor = connection_db.cursor()
    data = text.split(',')
    table_columns = '(menuname,menuprize)'
    SQL_cmd = f"""INSERT INTO menu { table_columns } VALUES(%s,%s);"""
    cursor.execute(SQL_cmd,(str(data[0]),int(data[1])))
    connection_db.commit()
    cursor.close()
    connection_db.close()
    return text

def updateMenu(text):
    DATABASE_URL = os.environ['DATABASE_URL']
    connection_db = psycopg2.connect(DATABASE_URL,sslmode='require')
    cursor = connection_db.cursor()
    data = text.split(',')
    SQL_cmd = f"""UPDATE menu SET menuprize = %s WHERE menuname = %s;"""
    cursor.execute(SQL_cmd,(int(data[1]),str(data[0])))
    connection_db.commit()
    cursor.close()
    connection_db.close()
    return text

def deleteMenu(text):
    DATABASE_URL = os.environ['DATABASE_URL']
    connection_db = psycopg2.connect(DATABASE_URL,sslmode='require')
    cursor = connection_db.cursor()
    data = text.split(',')
    SQL_cmd = f"""DELETE FROM menu WHERE menuname = %s;"""
    print(str(data[0]))
    cursor.execute(SQL_cmd,[str(data[0])])
    connection_db.commit()
    cursor.close()
    connection_db.close()
    return text

def showAds():
    DATABASE_URL = os.environ['DATABASE_URL']
    connection_db = psycopg2.connect(DATABASE_URL,sslmode='require')
    cursor = connection_db.cursor()
    SQL_cmd = f"""SELECT * FROM ads ORDER by ads_id DESC limit 5;"""
    cursor.execute(SQL_cmd)
    connection_db.commit()
    raws = cursor.fetchall()
    data = []
    for raw in raws:
        data.append(raw)
    
    cursor.close()
    connection_db.close()
    return data

def deleteAds(text):
    DATABASE_URL = os.environ['DATABASE_URL']
    connection_db = psycopg2.connect(DATABASE_URL,sslmode='require')
    cursor = connection_db.cursor()
    data = text.split(',')
    SQL_cmd = f"""DELETE FROM ads WHERE ads_id = %s;"""
    print(int(data[0]))
    cursor.execute(SQL_cmd,[int(data[0])])
    connection_db.commit()
    cursor.close()
    connection_db.close()
    return text

def addads(text):
    DATABASE_URL = os.environ['DATABASE_URL']
    connection_db = psycopg2.connect(DATABASE_URL,sslmode='require')
    cursor = connection_db.cursor()
    data = text.split(',')
    table_columns = '(adsname,adscontent,adspicname)'
    SQL_cmd = f"""INSERT INTO menu { table_columns } VALUES(%s,%s,%s);"""
    cursor.execute(SQL_cmd,(str(data[0]),str(data[1]),str(data[2])))
    connection_db.commit()
    cursor.close()
    connection_db.close()
    return text

def addOrders(text):
    DATABASE_URL = os.environ['DATABASE_URL']
    connection_db = psycopg2.connect(DATABASE_URL,sslmode='require')
    cursor = connection_db.cursor()
    data = text.split(',')
    table_columns = '(nos,cusphone,nodes)'
    SQL_cmd = f"""INSERT INTO ordermenu { table_columns } VALUES(%s,%s,%s);"""
    cursor.execute(SQL_cmd,(int(data[0]),str(data[1]),str(data[2])))
    connection_db.commit()
    cursor.close()
    connection_db.close()
    return text

def showOrders():
    DATABASE_URL = os.environ['DATABASE_URL']
    connection_db = psycopg2.connect(DATABASE_URL,sslmode='require')
    cursor = connection_db.cursor()
    SQL_cmd = f"""SELECT * FROM ordermenu ORDER by order_id DESC limit 10;"""
    cursor.execute(SQL_cmd)
    connection_db.commit()
    raws = cursor.fetchall()
    data = []
    for raw in raws:
        data.append(raw)
    
    cursor.close()
    connection_db.close()
    return data
