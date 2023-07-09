# Usa la imagen de Go oficial como base
FROM golang:latest

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo server.go al directorio de trabajo del contenedor
COPY . .

# Compila la aplicación Go
RUN go build -o app/server.go

# Exponer el puerto en el que se ejecuta la API
EXPOSE 8080

# Comando para iniciar la aplicación cuando se inicie el contenedor
CMD ["./server"]
