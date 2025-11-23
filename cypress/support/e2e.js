// Cypress support file: loaded before test files
// If you need custom global setup, put it here.

// Load custom commands
require('./commands')

// Example: set default command timeout for stable tests
Cypress.config('defaultCommandTimeout', 8000)
