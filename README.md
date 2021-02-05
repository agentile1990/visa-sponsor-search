# visa-sponsor-search

Find Companies Offering Visa Sponsorships

## Development Environment Setup

### Database
1. Start PostgreSQL container: `docker-compose up --build`
1. Create PGPASSFILE `cp ./db_deploy/.pgpass.example ./db_deploy/.pgpass`
1. Set database, hostname, user and password fields in `.pgpass`
1. Run db_deploy: `./db_deploy.sh`

### Parser
- Start the parser container with `./parser/startdev.sh`
- The parser directory also contains a VS Code `.devcontainer` setup for development

