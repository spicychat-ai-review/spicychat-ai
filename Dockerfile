# Start with Python base (hello-world doesn't have Python runtime)
FROM python:3.11-slim

# Reference to the hello-world image for documentation
LABEL base_reference="docker.io/library/hello-world:latest"
LABEL version="v1"
LABEL description="SpicyChat AI stub model - first version"
LABEL org.opencontainers.image.source="https://github.com/spicychat-ai-review/spicychat-ai"
LABEL org.opencontainers.image.url="https://github.com/spicychat-ai-review/spicychat-ai"
LABEL org.opencontainers.image.documentation="https://github.com/spicychat-ai-review/spicychat-ai#readme"

# Install cog
RUN pip install cog

# Copy predict script
COPY predict.py /predict.py
COPY README.md /README.md

# Make predict script executable
RUN chmod +x /predict.py

# Default command
CMD ["python", "/predict.py"] 