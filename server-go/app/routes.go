package main

import (
	"encoding/json"
	"math/rand"
	"net/http"

	"github.com/dnpoma/sa-tienda/server-go/app/entity"
	"github.com/dnpoma/sa-tienda/server-go/app/repository"
)



var (
	repoUser repository.UserRepository = repository.NewUserRepository() 
	repoOrder repository.OrderRepository = repository.NewOrderRepository()
	repoProduct repository.ProductRepository = repository.NewProductRepository()
)



func GetProduct(response http.ResponseWriter , request *http.Request)  {
	response.Header().Set("Content-Type","application/json")
	product , err := repoProduct.FindAllProduct()
	if err !=nil {
		response.WriteHeader(http.StatusInternalServerError)
		response.Write([]byte(`{"error":"Error Getting the Product"}`))
		return
	}
	response.WriteHeader(http.StatusOK)
	json.NewEncoder(response).Encode(product)
}

func GetUser(response http.ResponseWriter , request *http.Request)  {
	response.Header().Set("Content-Type","application/json")
	users , err := repoUser.FindAll()
	if err !=nil {
		response.WriteHeader(http.StatusInternalServerError)
		response.Write([]byte(`{"error":"Error Getting the Users"}`))
		return
	}
	response.WriteHeader(http.StatusOK)
	json.NewEncoder(response).Encode(users)
}

func AddUser(response http.ResponseWriter , request *http.Request){
	response.Header().Set("Content-Type","application/json")
	var user entity.User
	err:= json.NewDecoder(request.Body).Decode(&user)
	if err != nil{
		response.WriteHeader(http.StatusInternalServerError)
		response.Write([]byte(`{"error":"Error Unmarshalling Data"}`))
		return
	}
	user.ID = rand.Int63()
	repoUser.Save(&user)
	response.WriteHeader(http.StatusOK)
	json.NewEncoder(response).Encode(user)
}