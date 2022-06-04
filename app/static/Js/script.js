let form_fields = document.getElementsByTagName('input')
form_fields[2].placeholder='provide an Email';
form_fields[3].placeholder='Provide a username';
form_fields[4].placeholder='Enter password';
form_fields[5].placeholder='Verify your Password';


for (var field in form_fields){	
    form_fields[field].className += ' form-control'
}