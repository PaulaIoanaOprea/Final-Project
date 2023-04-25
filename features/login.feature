Feature: Test the functionality of the Login Page

  #Scenariu_Curs fara parametru
  Scenario: Check that "No customer account found" message is displayed when the user tries to log in with an unregistered email
    Given I am on the Login Page
    When I insert an unregistered email in the email input
    When I insert a password in the password input
    When I click on the login button
    Then The main error message is displayed
    Then The error text contains "No customer account found" message

  #Scenariu_Curs cu parametru
  Scenario: Check that "No customer account found" message is displayed when the user tries to log in with an unregistered email
    Given I am on the Login Page
    When I insert "wrong_email@host.com" in the email input
    When I insert "parolaoarecare" in the password input
    When I click on the login button
    Then The main error message is displayed
    Then The error text contains "No customer account found"

   #Scenariu1_Tema
    Scenario: Check that “Please enter your email” message is displayed when the user enters empty email address:
      Given I am on the Login Page
      When I insert " " in the email input
      When I click on the login button
      Then The email error message is displayed
      Then The error text contains "Please enter your email"

      #Scenariu2_Tema
      Scenario: Check that “Wrong email” message is displayed when the user enters an email address with an invalid format
        Given I am on the Login Page
        When I insert "emailinvalid" in the email input
        When I click on the login button
        Then The email error message is displayed
        Then The email error message text contains "Wrong email"

       #Scenariu3_Tema
      Scenario: Check that the URL is correct
        Given I am on the Login Page
        Then The actual URL is "https://demo.nopcommerce.com/login"



