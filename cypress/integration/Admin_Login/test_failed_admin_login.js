describe('Failed Admin login', function(){
    it('Tests the admin login page for a failed login', function(){
        cy.visit("http://localhost:5000/login")
        cy.get('[type="text"]').type('admin@admin.com')
        cy.get('[type="password"]').type('12345678')
        cy.get('button').click()
        cy.get('h2').contains('Log in failed')
    });
});