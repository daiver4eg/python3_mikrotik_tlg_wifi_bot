def clear_wifi_key(list,str):
 #Функция возвращает текст из строки по парам срезов
 #счетчик для циклов
 counter = 0
 #переменная для прохода по индексам
 i = 0
 #data
 clr_data = ""
 while len(list) > counter:
    #print("индекс ", list[i])
    #print(list[i+1])
    #print("типапароль ", str[list[i]-1:(list[i+1]-2)])

    clr_data += "Пароль wifi " + str[list[i]+1:(list[i+1])] + "\n"

    i += 2
    counter += 2
 return clr_data