describe('Admin Dashboard Loaded', function(){
    it('Tests the admin dashboard to make sure it has the required elements', function(){
        cy.visit("http://localhost:5555/admin")
        cy.get('[type="text"]').type('admin@admin.com')
        cy.get('[type="password"]').type('admin1')
        cy.get('button').click()
        cy.get('h1').contains('Admin Dashboard')
        cy.get('a').should('have', 'target', 'blank')
        cy.get('div[class="apple_stock"]')
        cy.get('div[class="fcb_stock"]')
        cy.get('div[class="google_stock"]')
        cy.get('div[class="oracle_stock"]')
        cy.get('div[class="ubi_stock"]')
    });
});