describe('Successfully Show Stock Prices for a Microservice', function() {
    it ('Tests api call for the /get-last route', function() {
        cy.visit('http://localhost:5000/login')
        cy.get('[type="text"]').type('test@company.com')
        cy.get('[type="password"]').type('12345678')
        cy.get('button').click()
        cy.wait(1000)
        cy.visit('http://localhost:5000/Accounts/Dashboard/Test_Account')
        cy.get('[action="/Microservices/Google/Buy"] > button').click()
        cy.get('#Microservices').click()
        cy.get('#get-last').click()
        cy.get('tr').eq(0).should('contain', 'Alphabet Inc')
    });
}
);
