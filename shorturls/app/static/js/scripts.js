base_url = "http://localhost:8000/"
jQuery(document).ready(function() {

	$('.url-submit form').submit(function(e) {
		e.preventDefault();
    console.log('Entered submit')
    var data = $("#url_form").serialize();
    $.ajax({
      url : base_url.concat("new_link/"), 
      type : "POST", 
      data: data,
      success : function(response) {
        console.log(response.valid)
        if (response.valid === 'False'){
          console.log('Entered invalid')
          $("#error_msg").show();
        }else{
          console.log('Entered valid')
          $('body').html(response.html);
        }
      }
    });
  });
});
