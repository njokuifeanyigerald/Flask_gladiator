import gladiator as gl

valid_test_data = {
    'email': 'realbopgeek@gmail.com',
    'pw': 'pd123',
    'name': 'TopBoy',
    'birth_year': 1999
}
# assigning validations
registration_form_validator = (
    ('email', gl.required, gl.format_email),
    ('pw', gl.required, gl.length_min(5)),
    ('name', gl.required, gl.type_(str)),
    ('birth_year', gl.required, gl.type_(int))
)
  
# checking data using validate()
print("Validating data : ")


result = gl.validate(registration_form_validator, valid_test_data)
print("Is data valid ? : " + str(bool(result)))
