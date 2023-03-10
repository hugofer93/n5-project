# n5-project

This is a REST API with [Django](https://docs.djangoproject.com/en/3.2/), [Django REST Framework](https://www.django-rest-framework.org/) and [PostgreSQL](https://www.postgresql.org/)


## Overview: N5 Project

[Problem Statement](PROBLEM-STATEMENT.md) proposed by [N5 Now](https://n5now.com/es/)


## Table of Contents

* [Overview](#n5-project)
* [Main Dependencies](#Main-Dependencies)
* [Project Configuration](#Project-Configuration)
* [Architecture Proposal](PROPOSAL.md#aws-deployment)


# Main Dependencies

    Python              ~3.8
    Django              ~3.2
    djangorestframework ~3.13
    PostgreSQL          ~12.7

For more details, see the [pyproject.toml file](pyproject.toml).


# Docker Configuration

- [Install Docker](https://docs.docker.com/engine/install/)

- [Install Docker Compose](https://docs.docker.com/compose/install/#install-compose)


## Project Configuration

- Clone this [repository](https://github.com/hugofer93/n5-project):

        git clone git@github.com:hugofer93/n5-project.git

- Create `.env` file based on `.env.sample`:

        cp .env.sample .env

    **Production or Staging Environment**:

    - Set `DEBUG=false`

    **Develop Environment**:

    - Set `DEBUG=true`

- Up Services with docker-compose:

    **Production or Staging Environment**:

        docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d

    **Develop Environment**:

        docker compose up -d

- Execute commands in container (e.g.):

        docker compose exec project poetry run python manage.py shell

- Create an Admin User for the project:

        docker compose exec project poetry run python manage.py createsuperuser

- Show containers logs:

    For Django Project:

        docker compose logs -f project
