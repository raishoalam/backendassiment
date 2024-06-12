# backendassiment

1. Basic Setup and Simple Feature:

Set up the development environment and run the application.
Add a new field to the Conversation model.
Implement functionality to automatically generate and store conversation summaries.
Update the Django admin page to display the new field.
Database Migration and Data Management:

2. Migrate the database from SQLite to PostgreSQL.
Implement a management command to clean up old conversations.
Schedule the cleanup command to run periodically using Django’s crontab or Celery.
API Development and Integration:

3. Develop a new API endpoint to retrieve conversation summaries, supporting pagination and filtering.
Develop a file upload endpoint, implementing file duplication check to prevent multiple uploads of the same file.
Create an endpoint to list uploaded files with metadata.
Implement file deletion functionality.
