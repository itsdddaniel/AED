function MyTable()
{
	this.draw = MyTableDrawOptimized;
}

function MyTableDrawOptimized(array=[],border=1)
{
	var html = "";
	html += `<table border=${border}>`;
	for(i=0; i<array.length; i++)
	{
		html += "<tr>";
		html += `<td>${array[i].join("</td><td>")}</td>`;
		html += "</tr>";
	}
	html += "</table>";
	return html;
}
