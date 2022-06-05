from datetime import date, time, datetime, timedelta, timezone

def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%A %d %B %Y')
    print(data_atual) #resposta = 2022-06-04
    print(data_atual.strftime('%d/%m/%y')) #resposta = 04/06/22
    print(data_atual.strftime('%d/%m/%Y')) #resposta = 04/06/2022
    print(data_atual.strftime('%d.%m.%Y')) #resposta = 04.06.2022
    print(data_atual.strftime('%A %d %B %Y')) #resposta = Saturday 04 June 2022
    print(type(data_atual)) #resposta = <class 'datetime.date'>
    print(data_atual_str) #resposta = Saturday 04 June 2022
    print(type(data_atual_str)) #resposta = <class 'str'>

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario) #resposta = 15:18:30
    print(type(horario))  # resposta = <class 'datetime.time'>
    print(horario.strftime('%H:%M:%S')) # resposta = 15:18:30
    horario_str = horario.strftime('%H:%M:%S')
    print(type(horario_str))  # resposta = <class 'str'>

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)  # resposta = 2022-06-04 17:18:26.234581
    print(data_atual.strftime('%d/%m/%y %H:%M:%S'))  # resposta = 04/06/22 17:18:40
    print(data_atual.strftime('%c'))  # resposta = Sat Jun  4 17:20:49 2022
    print(data_atual.date())  # resposta = 2022-06-04
    print(data_atual.day)  # resposta = 4
    print(data_atual.month)  # resposta = 6
    print(data_atual.year)  # resposta = 2022
    print(data_atual.weekday())  # resposta = 5
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[data_atual.weekday()])  # resposta = Sábado
    data_info = datetime(1976, 11, 16, 12, 30, 10)
    print(data_info)  # resposta = 1976-11-16 12:30:10
    print(data_info.strftime('%c'))  # resposta = Tue Nov 16 12:30:10 1976
    data_string = '01/01/2019'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
    print(data_convertida)  # resposta = 2019-01-01 00:00:00
    print(type(data_convertida))  # resposta = <class 'datetime.datetime'>
    print(data_convertida.day)  # resposta = 1
    print(data_convertida.month)  # resposta = 1
    print(data_convertida.year)  # resposta = 2019
    print(data_convertida.time())  # resposta = 00:00:00
    print(data_convertida.weekday())  # resposta = 1
    print(tupla[data_convertida.weekday()])  # resposta = Terça
    data_string2 = '11/07/1975 12:30:00'
    data_convertida = datetime.strptime(data_string2, '%d/%m/%Y %H:%M:%S')
    print(data_convertida.strftime('%c'))  # resposta = Fri Jul 11 12:30:00 1975
    print(data_convertida)  # resposta = 1975-07-11 12:30:00
    #nova_dt = data_convertida - timedelta(days=365) e o print gera resposta = 1974-07-11 12:30:00
    nova_dt = data_convertida - timedelta(days=365, hours=6)
    print(nova_dt)  # resposta = 1974-07-11 06:30:00



def trabalhando_com_timedelta():
    pass

def trabalhando_com_timezone():
    pass





if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()
