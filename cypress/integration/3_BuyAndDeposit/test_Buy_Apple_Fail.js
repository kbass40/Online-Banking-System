describe('Successful API endpoint call', function() {
    it ('Tests API call for JSON object return', function() {
        cy.visit('http://localhost:5000/login')
        cy.get('[type="text"]').type('test@company.com')
        cy.get('[type="password"]').type('12345678')
        cy.get('button').click()
        cy.get('button[id="Test Account"]').click()
        cy.get('button[id="buy_apple_stock"]').click()
        cy.get('#buy_apple > .modal-content > .container > #amount').type("3")
        cy.get('#buy_apple > .modal-content > .container > #submit').click()
        cy.get('#message').contains("Not enough funds")
        
    });
}
);
