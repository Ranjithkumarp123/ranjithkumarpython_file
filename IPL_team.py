l=[[20,'11001'],[18,'10011'],[16,'10100'],[14,'11010'],[14,'01100'],[12,'01101'],[12,'01010'],
   [12,'10000'],[8,'00101'],[6,'01011']]
ll=['GT','LSG','RR','DC','RCB','KKR','PBKS','SRH','CSK','MI']
pp=[]
p=[]
c=0
total_points =0 
for i in l:
    a=i[1]
    for j in range(len(i[1])-1):
        if(a[j]=='0' and a[j+1]=='0'):
            p.append(i)
            pp.append(ll[c])
            total_points += i[0]
            c+=1
            break

print(total_points/len(pp))



                
                
            
            
    
