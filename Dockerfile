# Use the official PostgreSQL image as the base image
FROM postgres:latest

# Set the environment variables for PostgreSQL
ENV POSTGRES_USER admin
ENV POSTGRES_PASSWORD admin
ENV POSTGRES_DB SIT_PFM

# Expose the PostgreSQL port
EXPOSE 5432

# # Copy custom initialization scripts to the image
# COPY init.sql /docker-entrypoint-initdb.d/

# # Install netcat (nc) for health checks
# RUN apt-get update && apt-get install -y netcat

# # Health check script
# HEALTHCHECK CMD ["nc", "-z", "localhost", "5432"]

# Run the PostgreSQL server
CMD ["postgres"]
