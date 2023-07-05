package main

import (
	"encoding/json"
	"net/http"
	"math/rand"
)



var (
repo repository.UserRepository = repository.NewUserRepository() 
)

const (
	projectId      string = "a-3a604"
)

func getUser(response http.ResponseWriter , request *http.Request)  {
	response.Header().Set("Content-Type","application/json")
	users , err := repo.FindAll()
	if err !=nil {
		response.WriteHeader(http.StatusInternalServerError)
		response.Write([]byte(`{"error":"Error Getting the Users"}`))
		return
	}
	response.WriteHeader(http.StatusOK)
	json.NewEncoder(response).Encode(users)
}

func addUser(response http.ResponseWriter , request *http.Requsest){
	response.Header().Set("Content-Type","application/json")
	var user entity.User
	err:= json.NewDecoder(request.Body).Decode(&user)
	if err != nil{
		response.WriteHeader(http.StatusInternalServerError)
		response.Write([]byte(`{"error":"Error Unmarshalling Data"}`))
		return
	}
	user.ID = rand.Int63()
	repo.Save(&user)
	response.WriteHeader(http.StatusOK)
	json.NewEncoder(response).Encode(user)
}