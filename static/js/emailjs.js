$(document).ready(function () {
var contactform = $('form#contactform');
contactform.submit(function(event){
	event.preventDefault();

  //   ServiceID
  var service_id = 'gmail';
  var template_id = 'data_dashboard_ala';

  
  contactform.find('button').text('Sending...');
  emailjs.sendForm(service_id,template_id,contactform[0])
  	.then(function(){ 
    	alert('Sent!');
       contactform.find('button').text('Send');
    }, function(err) {
       alert('Send email failed!\r\n Response:\n ' + JSON.stringify(err));
       contactform.find('button').text('Send');
    });
  return false;
});
});