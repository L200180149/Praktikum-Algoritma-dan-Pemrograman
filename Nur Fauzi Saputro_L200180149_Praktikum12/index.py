import cgi

print "Content-type:text/html\r\n\r\n"
print "<!DOCTYPE html>"
print ""
print "<head><title>Data Diri di Web</title></head>"
print """
<body>
<table>
	<tr>
		<td rowspan='6'><img src='potpot.jpg'></td>
		<td><b><font size='5'>Data Diri</font><b></td>
	</tr>
	<tr>
		<td>Nama </td>
		<td>:</td>
		<td>Nur Fauzi Saputro</td>
	</tr>
	<tr>
		<td>Alamat tinggal </td>
		<td>:</td>
		<td>Klaten</td>
	</tr>
	<tr>
		<td>Tempat, tanggal lahir </td>
		<td>:</td>
		<td>Klaten, 25 Oktober 1999</td>
	</tr>
	<tr>
		<td>Buku favorit </td>
		<td>:</td>
		<td>Garis Waktu</td>
	</tr>
	<tr>
		<td>Motto </td>
		<td>:</td>
		<td>Hiduplah seperti naik sepeda</td>
	</tr>
</table>
</body>
</html>"""