Feature: Test the functionality of the Register Page

  Background: I am on the Register Page
  Given I am on the Register Page

  @simple
  Scenario: Check that trying to register without completing any field displays error fields
    When I click on the Register button
    Then First name error is displayed
    Then Last name error is displayed
    Then Email error is displayed
    Then Confirm password error is displayed

    @parameterized
    Scenario: Check that the register success with completing all the required fields
      When I select Female Gender
      When I enter "Paula Ioana" in the First name
      When I enter "Oprea" in the Last name
      When I select Day "9" in the Date of birth
      When I select Month "April" in the Date of birth
      When I select Year "1991" in the Date of birth
      When I enter "not_in_use_email@sf.com" in the Email
      When I enter "OZN" in the Company
      When I uncheck the Newsletter
      When I insert "Extraterestru66" in the Password
      When I insert "Extraterestru66" in the Confirm password
      When I click on the Register button
      Then The register success message is displayed
      Then The Continue button is displayed
      Then The register success message contains "Your registration completed"


