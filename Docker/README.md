# Docker Guide: Build Your Own Container & Pull Images from Docker Hub

A complete reference for creating your own Docker image from scratch and pulling any existing image from Docker Hub.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Key Concepts](#key-concepts)
3. [Part A: Pulling Images from Docker Hub](#part-a-pulling-images-from-docker-hub)
4. [Part B: Building Your Own Docker Image](#part-b-building-your-own-docker-image)
5. [Part C: Pushing Your Image to Docker Hub](#part-c-pushing-your-image-to-docker-hub)
6. [Common Commands Cheat Sheet](#common-commands-cheat-sheet)
7. [Troubleshooting](#troubleshooting)
8. [Next Steps](#next-steps)

## Prerequisites

- Docker installed → [get.docker.com](https://get.docker.com)
- A free [Docker Hub](https://hub.docker.com) account

Verify Docker is installed and working:

```bash
docker --version
docker run hello-world
```

If you see `Hello from Docker!`, you're ready to go.

## Key Concepts

| Term           | Meaning                                                              |
| -------------- | -------------------------------------------------------------------- |
| **Dockerfile** | A text file with instructions to build an image                      |
| **Image**      | A packaged, read-only template of your app (e.g. `myapp:v1`)         |
| **Container**  | A running instance of an image                                       |
| **Repository** | A collection of related images on a registry (e.g. `username/myapp`) |
| **Tag**        | A version label for an image (e.g. `latest`, `v1`, `18-alpine`)      |
| **Registry**   | The server storing images (`docker.io` = Docker Hub is the default)  |

Flow at a glance:

```
Dockerfile → docker build → Image → docker run → Container

Image → docker tag → docker push → Registry
                                        │
                                   docker pull (elsewhere)
                                        │
                                        ▼
                                     Image → docker run → Container
```

## Part A: Pulling Images from Docker Hub

### 1. Search for an image (optional)

```bash
docker search nginx
```

### 2. Pull the image

```bash
docker pull nginx
```

Pull a specific version/tag instead of `latest`:

```bash
docker pull nginx:1.25
```

Pull someone else's image from their namespace:

```bash
docker pull username/image-name:tag
```

### 3. Verify the image downloaded

```bash
docker images
```

### 4. Run it as a container

```bash
docker run -d --name my-nginx -p 8080:80 nginx
```

- `-d` → run in background (detached)
- `--name` → give the container a friendly name
- `-p 8080:80` → map host port 8080 → container port 80

### 5. Confirm it's running

```bash
docker ps
curl http://localhost:8080
```

## Part B: Building Your Own Docker Image

We'll build a simple Node.js app as the example — the same steps apply to Python, Java, Go, etc.

### 1. Create your project

```bash
mkdir docker-demo && cd docker-demo
```

**app.js**

```javascript
const http = require("http");

const server = http.createServer((req, res) => {
  res.writeHead(200, { "Content-Type": "text/plain" });
  res.end("Hello from Docker!");
});

server.listen(3000, () => {
  console.log("Server running on port 3000");
});
```

**package.json**

```json
{
  "name": "docker-demo",
  "version": "1.0.0",
  "main": "app.js"
}
```

### 2. Write the Dockerfile

Create a file named exactly `Dockerfile` (no extension):

```dockerfile
FROM node:22-alpine

WORKDIR /app

COPY package.json .
COPY app.js .

EXPOSE 3000

CMD ["node", "app.js"]
```

**What each line does:**

- `FROM` → base image to build on top of
- `WORKDIR` → sets the working directory inside the container
- `COPY` → copies files from your machine into the image
- `EXPOSE` → documents which port the app uses
- `CMD` → the command that runs when the container starts

### 3. Build the image

```bash
docker build -t docker-demo .
```

- `-t docker-demo` → names/tags the image
- `.` → build context is the current directory

Verify:

```bash
docker images
```

### 4. Run your container

```bash
docker run -d --name docker-demo-container -p 3000:3000 docker-demo
```

### 5. Test it

```bash
docker ps
curl http://localhost:3000
```

Expected output: `Hello from Docker!`

### 6. View logs

```bash
docker logs docker-demo-container
docker logs -f docker-demo-container   # follow live
```

### 7. Stop / start / remove

```bash
docker stop docker-demo-container
docker start docker-demo-container
docker rm docker-demo-container        # container must be stopped first
```

## Part C: Pushing Your Image to Docker Hub

### 1. Create a repository on Docker Hub

Go to **hub.docker.com → My Hub → Repositories → Create repository**, e.g. `docker-demo`.

### 2. Log in from your terminal

```bash
docker login
```

### 3. Tag your image with your username

Docker Hub requires the format `USERNAME/REPOSITORY:TAG`:

```bash
docker tag docker-demo:latest yourusername/docker-demo:latest
```

Check it worked:

```bash
docker images
```

### 4. Push it

```bash
docker push yourusername/docker-demo:latest
```

### 5. Verify

Visit `hub.docker.com/r/yourusername/docker-demo` — your image should be listed.

### 6. Pull it back down (from any machine)

```bash
docker pull yourusername/docker-demo:latest
docker run -d --name docker-demo-container -p 3000:3000 yourusername/docker-demo:latest
```

## Common Commands Cheat Sheet

| Action                   | Command                                                     |
| ------------------------ | ----------------------------------------------------------- |
| Pull an image            | `docker pull <image>`                                       |
| Search Docker Hub        | `docker search <term>`                                      |
| Build an image           | `docker build -t <name>:<tag> .`                            |
| List local images        | `docker images`                                             |
| Run a container          | `docker run -d --name <name> -p <host>:<container> <image>` |
| List running containers  | `docker ps`                                                 |
| List all containers      | `docker ps -a`                                              |
| View logs                | `docker logs <container>`                                   |
| Stop a container         | `docker stop <container>`                                   |
| Start a container        | `docker start <container>`                                  |
| Remove a container       | `docker rm <container>`                                     |
| Remove an image          | `docker image rm <image>`                                   |
| Log in to Docker Hub     | `docker login`                                              |
| Tag an image             | `docker tag <image>:<tag> <username>/<image>:<tag>`         |
| Push to Docker Hub       | `docker push <username>/<image>:<tag>`                      |
| Add persistent storage   | `-v volumename:/path/in/container`                          |
| Set environment variable | `-e KEY=value`                                              |

## Troubleshooting

**`denied: requested access to the resource is denied`**
→ You didn't tag the image with your Docker Hub username, or you're not logged in. Run `docker login` and re-tag correctly.

**`unauthorized: authentication required`**
→ Your login session expired. Run `docker login` again.

**`port is already allocated`**
→ Another container/process is using that host port. Change the host-side port: `-p 3001:3000`.

**Container exits immediately**
→ Check logs: `docker logs <container>`. Often means the app crashed or the Dockerfile's `CMD` is wrong.

**Image size too large**
→ Use `-alpine` or `-slim` base images, and consider a multi-stage build for production.

## Next Steps

Once comfortable with this, the natural progression is:

- **Docker Compose** — define multi-container apps (e.g. app + database) in one YAML file instead of long `docker run` commands
- **Docker volumes** — for persisting data (databases, uploads) across container restarts
- **Multi-stage builds** — for smaller, production-ready images
