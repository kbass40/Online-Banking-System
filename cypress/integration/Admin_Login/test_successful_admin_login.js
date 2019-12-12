describe('Successful Admin login', function(){
    it('Tests the admin login page for a successful login', function(){
        cy.visit("http://localhost:5555/admin")
        cy.get('[type="text"]').type('admin@admin.com')
        cy.get('[type="password"]').type('admin1')
        cy.get('button').click()
        cy.get('h1').contains('Admin Dashboard')
    });
});