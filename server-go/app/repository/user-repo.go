package repository

import (
	"context"
	"log"
	"github.com/dnpoma/sa-tienda/server-go/app/entity"
)

type UserRepository interface {
	Save(*entity.User) (*entity.User, error)
	FindAll() ([]entity.User, error)
}

type repoUser struct{}

const (
	collectionUser string = "users"
)

// NewUserRepository crea una nueva instancia del repositorio de usuarios.
func NewUserRepository() UserRepository {
	return &repoUser{}
}

func (*repoUser) Save(user *entity.User) (*entity.User, error) {
	ctx := context.Background()
	client, err := firestore.NewClient(ctx, projectId)
	if err != nil {
		log.Fatalf("Failed to create a Firestore client: %v", err)
		return nil, err
	}
	defer client.Close()
	_, _, err = client.Collection(collectionUser).Add(ctx, map[string]interface{}{
		"ID":       user.ID,
		"Name":     user.Name,
		"Email":    user.Email,
		"Password": user.Password,
		"IsAdmin":  user.IsAdmin,
	})
	if err != nil {
		log.Fatalf("Failed to add a new user: %v", err)
		return nil, err
	}

	return user, nil
}

func (*repoUser) FindAll() ([]entity.User, error) {
	ctx := context.Background()
	client, err := firestore.NewClient(ctx, projectId)
	if err != nil {
		log.Fatalf("Failed to create a Firestore client: %v", err)
		return nil, err
	}
	defer client.Close()
	var users []entity.User

	itr := client.Collection(collectionUser).Documents(ctx)
	for {
		doc, err := itr.Next()
		if err == iterator.Done {
			break
		}
		if err != nil {
			log.Fatalf("Failed to iterate the list of users: %v", err)
			return nil, err
		}

		user := entity.User{
			ID:       doc.Data()["Id"].(int64),
			Name:     doc.Data()["Name"].(string),
			Email:    doc.Data()["Email"].(string),
			Password: doc.Data()["Password"].(string),
			IsAdmin:  doc.Data()["IsAdmin"].(bool),
		}
		users = append(users, user)
	}

	return users, nil
}
