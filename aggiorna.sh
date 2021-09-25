#!/bin/bash

#Questo script aggiorna la directory di github (~/Documenti/GitHub_projects/ADM-HM1)

#Si sposta nella directory di git
cd ~/Documenti/GitHub_Projects/ADM-HM1

#Controlla che non ci siano aggiornamenti e poi carica le modifiche fatte nello stage		
git pull origin master ; git add * 

#Controlla che non siano stati eliminati dei file dalla directory		 
log=`git commit -m "aggiornato" | awk '/deleted:/{print $2}'`

#se li trova li elimina da git		
for i in $log
	do
		git rm $i; git commit -m "aggiornato"
	
done

#aggiorna la directory 		
git push origin master
