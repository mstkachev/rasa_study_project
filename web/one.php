 <?php
$host="";
$user="postgres";
$pass="rasa";
$db="rasa";
//Соединяемся с сервером
/* проверка соединения */
$dbconn = pg_connect("host=$host port=5432 dbname=$db user=$user password=$pass");

//Формируем текст запроса
$query="SELECT * FROM public.math ORDER BY public.math.Number";
 
//Выполняем запрос с сохранением идентификатора результата
$result=pg_query($query);
$rows = pg_num_rows($result);// количество полученных строк
 
print("<table border=1 align=center width=100% cellpadding=5><tr bgcolor=#ffffcc><th width=35%>Name</th><th>Number</th></tr>");

while($row = pg_fetch_array($result)){   //Creates a loop to loop through results
print("<tr><td align=center>" . $row[0] . "</td><td align=center>" . $row[1] . "</td></tr>");  //$row['index'] the index here is a field name
}

print("</table>"); //Close the table in HTML
 
//Закрываем соединение
pg_close();
?>