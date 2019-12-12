describe('Successful account creation', function() {
    it ('Tests creating an account', function() {
        cy.visit('http://localhost:5000/login')
        cy.get('[type="text"]').type('test@company.com')
        cy.get('[type="password"]').type('12345678')
        cy.get('button').click()
        cy.get('button[id="add_account"]').click()
        cy.get('#name').type('Test Account')
        cy.get('#submit').click()
        cy.get('button[id="Test Account"]')
    });
}
);
