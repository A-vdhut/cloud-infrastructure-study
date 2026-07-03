# cloud-infrastructure-study
# Cloud Study App

## Dockerfile

```dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./

RUN npm ci --only=production

COPY . .

EXPOSE 3000

CMD ["node", "index.js"]
```

## Test Locally with Docker

### Build the Docker image

```bash
docker build -t cloud-study-app app/
```

### Run the container

```bash
docker run -p 3000:3000 cloud-study-app
```

### Test the health endpoint

```bash
curl http://localhost:3000/health
```

### Expected Output

```json
{
  "status": "OK"
}
```
