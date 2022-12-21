Proyecto: Administracion de turnos de consultorio Medico

Autor: Damian Safdie
version 2.0
------------
Descripcion:
------------
El programa permitira a los pacientes acceder a la pagina web del consultorio reservar el turno para el medico y tambien consultar  los turnos ya solicitados.
Esta primera version solo estara trabajando para 1 (un) medico.
El mecanismo seria el siguiente:
el medico se encargara de realizar un archivo excel que luego lo exportara a csv con los dias y horarios que desea que se den sus turnos con el siguiente formato:
fecha, hora, paciente, doctor
este archivo debe recibir el nombre de turnos.csv

Luego tendremos que ejecutar turnos.py y alli se generara la base de datos que luego consultara y acualizara desde la aplicacion principal app.py.

En app.py encontraremos el acceso local en 127.0.0.1:5000 donde se podran ver los turnos disponibles y registrar el que deseamos reservar.









