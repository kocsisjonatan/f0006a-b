egyik = input('írj egy számot!')
másik = input('írj egy másik számot!')

#int
egyik = int(egyik)
másik = int(másik)

#ha
if egyik < másik:
    eredmény = 'itt ' + str(másik) + ' a nagyobb.'

elif egyik == másik:
    eredmény = 'Egyenlő!'
    
elif egyik > másik:
    eredmény = 'itt ' + str(egyik) + ' a nagyobb.'

#ki írás    
print(eredmény)
    