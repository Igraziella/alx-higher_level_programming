$.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {
	$('data.result').each(function() {
		$("UL#list_movies").append('<li>' + this.title + '</li>');
	});
});
