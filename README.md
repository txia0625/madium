# news-site

Use Django Framework to implement a Medium like news website.

## Timeline
- 1/8/2024 Implemented Basic Structure, decoupled generated settings and configs.
- 1/8/2024 Set up a simple logger
- 1/9/2024 Setup API, PostgresSQL and mailhog containers
- 1/10/2024 Add database backup/restore scripts and makefile
- 1/11/2024 Add custom user model, setup redoc api.
- 1/11/2024 Setup Nginx, serve staticfiles.
- 1/12/2024 Configure Redis, Celery and flower.
- 1/12/2024 add timestamped, profile
- 1/13/2024 add JWT authentication and some auth routes
- 1/15/2024 feat: add profile, follow and unfollow views


## Tools

### General
- Django REST Framework

### Basic Structure, Utilities
- Docker
- Shell Script
### Async Tasks
- Celery
- Redis(as message broker)
### Reverse Proxy and Load Balancer
- nginx

### Email Development
- Mailhog
- Mailgun

### API Documentation
- Redoc