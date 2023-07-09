package main

import (
	"log"
	"net/http"

	"github.com/gorilla/mux"
)

func handleRequest() {
	const port string = ":8000"

	router := mux.NewRouter()

	router.HandleFunc("/api/user", GetUser).Methods("GET")
	router.HandleFunc("/api/user", GetProduct).Methods("GET")

	router.HandleFunc("/api/product", AddUser).Methods("POST")

	log.Println("Server Listening on Port", port)
	log.Fatalln(http.ListenAndServe(port, router))
}

func main() {
	handleRequest()
}
