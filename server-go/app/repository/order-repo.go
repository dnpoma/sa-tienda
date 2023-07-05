package repository

import (
	"context"
	"log"
	"time"
)

type OrderRepository interface {
	Save(*entity.Order) (*entity.Order, error)
	FindAll() ([]entity.Order, error)
}

type repoOrder struct{}

const (
	collectionOrders string = "orders"
)

// NewOrderRepository crea una nueva instancia del repositorio de órdenes.
func NewOrderRepository() OrderRepository {
	return &repoOrder{}
}

func (*repoOrder) Save(order *entity.Order) (*entity.Order, error) {
	ctx := context.Background()
	client, err := firestore.NewClient(ctx, projectId)
	if err != nil {
		log.Fatalf("Failed to create a Firestore client: %v", err)
		return nil, err
	}
	defer client.Close()
	_, _, err = client.Collection(collectionOrders).Add(ctx, map[string]interface{}{
		"id":            order.ID,
		"user":          order.User,
		"orderItems":    order.OrderItems,
		"shipping":      order.Shipping,
		"payment":       order.Payment,
		"itemsPrice":    order.ItemsPrice,
		"taxPrice":      order.TaxPrice,
		"shippingPrice": order.ShippingPrice,
		"totalPrice":    order.TotalPrice,
		"isPaid":        order.IsPaid,
		"paidAt":        order.PaidAt,
		"isDelivered":   order.IsDelivered,
		"deliveredAt":   order.DeliveredAt,
		"timestamps":    order.Timestamps,
	})
	if err != nil {
		log.Fatalf("Failed to add a new order: %v", err)
		return nil, err
	}

	return order, nil
}

func (*repoOrder) FindAll() ([]entity.Order, error) {
	ctx := context.Background()
	client, err := firestore.NewClient(ctx, projectId)
	if err != nil {
		log.Fatalf("Failed to create a Firestore client: %v", err)
		return nil, err
	}
	defer client.Close()
	var orders []entity.Order

	itr := client.Collection(collectionOrders).Documents(ctx)
	for {
		doc, err := itr.Next()
		if err == iterator.Done {
			break
		}
		if err != nil {
			log.Fatalf("Failed to iterate the list of orders: %v", err)
			return nil, err
		}

		order := entity.Order{
			ID:            doc.Data()["id"].(int64),
			User:          doc.Data()["user"].(string),
			OrderItems:    doc.Data()["orderItems"].([]entity.OrderItem),
			Shipping:      doc.Data()["shipping"].(entity.Shipping),
			Payment:       doc.Data()["payment"].(entity.Payment),
			ItemsPrice:    doc.Data()["itemsPrice"].(int),
			TaxPrice:      doc.Data()["taxPrice"].(int),
			ShippingPrice: doc.Data()["shippingPrice"].(int),
			TotalPrice:    doc.Data()["totalPrice"].(int),
			IsPaid:        doc.Data()["isPaid"].(bool),
			PaidAt:        doc.Data()["paidAt"].(time.Time),
			IsDelivered:   doc.Data()["isDelivered"].(bool),
			DeliveredAt:   doc.Data()["deliveredAt"].(time.Time),
			Timestamps:    doc.Data()["timestamps"].(time.Time),
		}
			orders = append(orders, order)
	}

	return orders, nil
}
