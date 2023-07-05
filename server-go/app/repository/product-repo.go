package repository

import (
	"context"
	"log"
	"time"
)

type ReviewRepository interface {
	Save(*entity.Review) (*entity.Review, error)
	FindAll() ([]entity.Review, error)
}

type ProductRepository interface {
	Save(*entity.Product) (*entity.Product, error)
	FindAll() ([]entity.Product, error)
}

type repoProduct struct{}

const (
	CollectionProducts  string = "products"
)

// NewReviewRepository crea una nueva instancia del repositorio de reseñas.
func NewReviewRepository() ReviewRepository {
	return &repoProduct{}
}

func (*repoProduct) Save(review *entity.Review) (*entity.Review, error) {
	ctx := context.Background()
	client, err := firestore.NewClient(ctx, projectId)
	if err != nil {
		log.Fatalf("Failed to create a Firestore client: %v", err)
		return nil, err
	}
	defer client.Close()
	_, _, err = client.Collection(reviewsCollectionProducts).Add(ctx, map[string]interface{}{
		"Id":      review.ID,
		"Name":    review.Name,
		"Rating":  review.Rating,
		"Comment": review.Comment,
	})
	if err != nil {
		log.Fatalf("Failed to add a new review: %v", err)
		return nil, err
	}

	return review, nil
}

func (*repoProduct) FindAll() ([]entity.Review, error) {
	ctx := context.Background()
	client, err := firestore.NewClient(ctx, projectId)
	if err != nil {
		log.Fatalf("Failed to create a Firestore client: %v", err)
		return nil, err
	}
	defer client.Close()
	var reviews []entity.Review

	itr := client.Collection(reviewsCollectionProducts).Documents(ctx)
	for {
		doc, err := itr.Next()
		if err == iterator.Done {
			break
		}
		if err != nil {
			log.Fatalf("Failed to iterate the list of reviews: %v", err)
			return nil, err
		}

		review := entity.Review{
			ID:      doc.Data()["id"].(int64),
			Name:    doc.Data()["name"].(string),
			Rating:  doc.Data()["rating"].(int),
			Comment: doc.Data()["comment"].(string),
		}
		reviews = append(reviews, review)
	}

	return reviews, nil
}

// NewProductRepository crea una nueva instancia del repositorio de productos.
func NewProductRepository() ProductRepository {
	return &repoProduct{}
}

func (*repoProduct) Save(product *entity.Product) (*entity.Product, error) {
	ctx := context.Background()
	client, err := firestore.NewClient(ctx, projectId)
	if err != nil {
		log.Fatalf("Failed to create a Firestore client: %v", err)
		return nil, err
	}
	defer client.Close()
	_, _, err = client.Collection(productsCollectionProducts).Add(ctx, map[string]interface{}{
		"Id":           product.ID,
		"Name":         product.Name,
		"Image":        product.Image,
		"Brand":        product.Brand,
		"Price":        product.Price,
		"Category":     product.Category,
		"CountInStock": product.CountInStock,
		"Description":  product.Description,
		"Rating":       product.Rating,
		"NumReviews":   product.NumReviews,
		"Reviews":      product.Reviews,
		"Timestamps":   product.Timestamps,
	})
	if err != nil {
		log.Fatalf("Failed to add a new product: %v", err)
		return nil, err
	}

	return product, nil
}

func (*repoProduct) FindAll() ([]entity.Product, error) {
	ctx := context.Background()
	client, err := firestore.NewClient(ctx, projectId)
	if err != nil {
		log.Fatalf("Failed to create a Firestore client: %v", err)
		return nil, err
	}
	defer client.Close()
	var products []entity.Product

	itr := client.Collection(productsCollectionProducts).Documents(ctx)
	for {
		doc, err := itr.Next()
		if err == iterator.Done {
			break
		}
		if err != nil {
			log.Fatalf("Failed to iterate the list of products: %v", err)
			return nil, err
		}

		product := entity.Product{
			ID:           doc.Data()["Id"].(int64),
			Name:         doc.Data()["Name"].(string),
			Image:        doc.Data()["Image"].(string),
			Brand:        doc.Data()["Brand"].(string),
			Price:        doc.Data()["Price"].(int),
			Category:     doc.Data()["Category"].(string),
			CountInStock: doc.Data()["CountInStock"].(int),
			Description:  doc.Data()["Description"].(string),
			Rating:       doc.Data()["Rating"].(int),
			NumReviews:   doc.Data()["NumReviews"].(int),
			Reviews:      doc.Data()["Reviews"].([]entity.Review),
			Timestamps:   doc.Data()["Timestamps"].(time.Time),
		}
		products = append(products, product)
	}

	return products, nil
}
