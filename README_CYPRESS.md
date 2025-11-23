Cypress E2E tests

Quick steps to run the new Cypress tests added to the project.

Prerequisites
- Node.js + npm installed
- Your Django dev server running on `http://localhost:8000` (default)
- The application database seeded with books and genres used by the tests (the tests assume at least one book exists; adjust or seed as needed)

Install Cypress (project root):

```powershell
npm install
```

Run Django dev server (in a separate terminal):

```powershell
python manage.py runserver
```

Open Cypress interactive runner:

```powershell
npm run cypress:open
```

Run Cypress headless:

```powershell
npm run cypress:run
```

Notes
- The tests were converted from Selenium-based tests and assume the UI routes/labels (Portuguese) exist (for example `Entrar`, `Sair`, `Biblioteca`, `Adicionar`, `Remover`).
- If the Django site uses different text or the database is empty, seed the DB or update the tests accordingly.
