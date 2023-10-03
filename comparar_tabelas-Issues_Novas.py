import csv
#Colunas de comparação no csv
SYSTEM_IP = 1
SYSTEM_PORT = 6
SYSTEM_SERVICE = 7
SYSTEM_ISSUE_TITLE = 10

#Abertura dos arquivos usados para comparação e gravação dos dados
with open('old.csv','r',encoding="utf8") as t1, open('new.csv','r',encoding="utf8") as t2, open ('Issues_Novas.csv','w',newline='',encoding="utf8") as t3:
    old = csv.reader(t1,delimiter=',')    
    new = csv.reader(t2,delimiter=',')
    update = csv.writer(t3,delimiter=',')        
#Varre cada linha do arquivo 1 comparando com o arquivo 2
    for row_new in new:             
        for row_old in old:
            if (row_new[SYSTEM_IP] == row_old[SYSTEM_IP]) and (row_new[SYSTEM_PORT] == row_old[SYSTEM_PORT]) and (row_new[SYSTEM_ISSUE_TITLE] == row_old[SYSTEM_ISSUE_TITLE]):         
                comparador = 1
                break
            else:
                comparador = 0
        if comparador == 0:       
            update.writerow(row_new)
            t1.seek(0)
        else:                
            t1.seek(0)

