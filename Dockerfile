# Backend service
FROM python:3.8 AS backend
WORKDIR /app/backend
COPY backend/requirements.txt .
RUN pip install -r requirements.txt
COPY backend/ .
EXPOSE 5000
CMD ["python", "app.py"]

# Frontend service
FROM node:14 AS frontend
WORKDIR /app/frontend
COPY frontend/package.json frontend/package-lock.json ./
RUN npm install
COPY frontend/ .
EXPOSE 3000
CMD ["npm", "start"]

# Final container to run both
FROM backend AS final
WORKDIR /app
COPY --from=frontend /app/frontend /app/frontend
