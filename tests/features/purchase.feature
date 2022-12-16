Feature: Purchase an item
    Purchase an item

    Background: The user is logged with the correct credentials
        Given the user is in the home page
        When the user logins as "standard user"

    Scenario: Complete the purchase
        When the user selects an item
        And the user clicks in the cart button
        And the user clicks in the checkout button
        And the "standard user" completes the shipping information
        And the user clicks in the continue button
        And the user clicks in the finish button
        Then validate the text order is completed succesfully

    Scenario: Validate that the name of the selected item is persistent in the cart and checkout page
        When the user selects an item
        And the user clicks in the cart button
        Then the user sees the item in the cart matches the one selected
        When the user clicks in the checkout button
        And the "standard user" completes the shipping information
        And the user clicks in the continue button
        Then the user sees the item in the checkout matches the one selected