from socket import *
import time
#import pymysql
import mysql.connector as mariadb
#exec(open(".//Desktop/Python/Comunica_arduino.py").read())

def quebraValoresDict(parti):
    return {"C1": float(parti.partition('|')[0]),
            "C2": float(parti.partition('|')[2].partition('|')[0]),
            "C3": float(parti.partition('|')[2].partition('|')[2].partition('|')[0])
            }


#mariadb -u 'RASPI'@'localhost' -p 's7oi4nov'
#pip3 list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U
sql = '''select concat(cast(horario as date), ' ', lpad(hour(horario), 2, 0), ':', lpad(minute(horario), 2, 0), ':00') horario, 
    avg(temp1) temp1, 
    avg(temp2) temp2, 
    avg(temp3) temp3 
    from Temperaturas 
    group by hour(horario), MINUTE(horario) 
    order by hour(horario) asc, 
        minute(horario) asc'''


conta = 1
mariadb_connection  = mariadb.connect(user = 'RASPI',password = 's7oi4nov', database = 'CHUVEIRO' )

address= ( '192.168.0.88', 5000) #define server IP and port
client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
client_socket.settimeout(2) #Only wait 1 second for a response

if conta == 1:
#while(1):
    data = "Temperature" #Set data request to Temperature

    #client_socket.sendto( data, address) #Send the data request

    try:
        client_socket.sendto( data.encode('utf-8'), address) #Send the data request
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        #rec_data, addr = client_socket.recvmsg(2048)
        
        #temp = float(rec_data) #Convert string rec_data to float temp
        #print "The Measured Temperature is ", temp, " degrees c." # Print the result

    except:
        pass

    time.sleep(2) #delay before sending next command
    print("CONTAGEM: {}".format(conta))
    #print(conta)
    print('\n')
    conta+=1
    
#grava = rec_data.decode('utf-8')
#grava.partition('|')
   
#def quebraValores(parti):
#    return [parti.partition('|')[0],  
#            parti.partition('|')[2].partition('|')[0], 
#            parti.partition('|')[2].partition('|')[2].partition('|')[0] 
#            ]
            

    valores = quebraValoresDict(rec_data.decode('utf-8'))
    
    cursor  = mariadb_connection.cursor()

#cursor.execute("select * from Temperaturas")

#for row in cursor:
 #   print(row)
 #"Insert into Temperaturas (horario, temperatura, unidade) values (NOW(), {}, {}, {} 'C')".format(*list(valores.values()))
    #"Insert into Temperaturas (horario, temperatura, unidade) values (NOW(), {}, {}, {} 'C')".format(*list(valores.values()))
    cursor.execute("Insert into Temperaturas (horario, temp1, temp2, temp3, unidade) values (NOW(), {}, {}, {}, 'C')".format(*list(valores.values())))
    mariadb_connection.commit()
    time.sleep(2) #delay before sending next command

#read = pandas.read_sql(sql, mariadb_connection)


#mariadb_connection.close()



