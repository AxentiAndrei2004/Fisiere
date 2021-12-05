with open('C:\Users\_DelL15_\Downloads\Lista Clasei 11A.txt','r') as f:
    elevii=list(f)
    n=media=0
    print('Nume','\tPrenume','Nota','Limba studiata',sep='\t')
grupa1=('C:\Users\_DelL15_\Desktop\Grupa de engleza.txt','w')
grupa2=('C:\Users\_DelL15_\Desktop\Grupa de germana.txt','w')
for a in elevii:
    elev=a.split()
    nota=int(elev[2])
    n,media=n+1,media+nota
    print(elev[0], elev[1],nota,elev[3],sep='\t')
    if elev[3]=='Grupa de engleza':
        grupa1.write(elev[0]+'\t'+elev[1]+'\t'+nota)
    if elev[3]=='Grupa de germana':
        grupa2.write(elev[0]+'\t'+elev[1]+'\t'+nota)
print('Media celor',n,'elevi este',media/float(n))
grupa1.close()
grupa2.close()