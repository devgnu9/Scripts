#! /bin/bash

ano=`date +%Y`
mes=`date +%m`
dia=`date +%d`
hora=`date +%H`

if [[ -d /.NombreDeCarpeta/ ]]; then
  echo "Carpeta contenedora existente"
else
  mkdir /.NombreDeCarpeta/
fi

function respaldar
{
  mysqldump -uUSUARIO -pCONTRASENA NOMBRE_DB > /.NombreDeCarpeta/Respaldo$mes$ano.sql
  
  git init
  git remote add origin https://gitlab.com/XXXX/YYYYY.git
  git add Respaldo$mes$ano.sql
  git commit -m "Respaldo de la fecha $dia$mes$ano"
  git push -u origin master

}

if [[ -d /.NombreDeCarpeta/ ]]; then
  cd /.NombreDeCarpeta/
  respaldar
fi
