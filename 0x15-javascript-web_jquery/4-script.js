$('#toggle_header').click(() => {
	if($('header').hasClass('red')) {
		$('header').addClass('green')
	} else {
		$('header').addClass('red')
	}
});
