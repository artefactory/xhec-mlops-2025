FROM python:3.11.6-slim
##### Enter your code here #####
# You can find A LOT of resources on the internet (good example: https://docs.docker.com/get-started/docker-concepts/building-images/writing-a-dockerfile/)
# Don't forget to :
# - Install the app dependencies
#   - Install uv on the container: COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
#   - Copy the dependencies into the image: COPY pyproject.toml uv.lock ./
#   - Install dependencies: RUN uv sync --locked
# - Expose the correct port
# - Copy your files in the container
WORKDIR /web_service
# - Initialize the app with uvicorn
