describe('Successfully Account Creation test_account', function() {
    it ('Tests the account creation method... account is used in following tests', function() {
        cy.visit('http://localhost:5000/login')
        cy.get('[type="text"]').type('test@company.com')
        cy.get('[type="password"]').type('12345678')
        cy.get('button').click()
        cy.wait(1000)
        cy.get('#add_button').click()
        cy.get('#name').type('Test_Account')
        cy.get('#submit').click()
        cy.visit('http://localhost:5000/Accounts/Dashboard/Test_Account')
    });
}
);
