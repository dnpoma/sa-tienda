package entity

import "time"

type Shipping struct {
	ID int64 `json:"id"`
	Address    string `json:"address"`
	City       string `json:"city"`
	PostalCode string `json:"postalCode"`
	Country    string `json:"country"`
}

type Payment struct {
	ID int64 `json:"id"`
	PaymentMethod string `json:"paymentMethod"`
}

type OrderItem struct {
	ID int64 `json:"id"`
	Name     string `json:"name"`
	Qty      int    `json:"qty"`
	Image    string `json:"image"`
	Price    string `json:"price"`
	Product  string `json:"product"`
}

type Order struct {
	ID int64 `json:"id"`
	User          string      `json:"user"`
	OrderItems    []OrderItem `json:"orderItems"`
	Shipping      Shipping    `json:"shipping"`
	Payment       Payment     `json:"payment"`
	ItemsPrice    int         `json:"itemsPrice"`
	TaxPrice      int         `json:"taxPrice"`
	ShippingPrice int         `json:"shippingPrice"`
	TotalPrice    int         `json:"totalPrice"`
	IsPaid        bool        `json:"isPaid"`
	PaidAt        time.Time   `json:"paidAt"`
	IsDelivered   bool        `json:"isDelivered"`
	DeliveredAt   time.Time   `json:"deliveredAt"`
	Timestamps    time.Time   `json:"timestamps"`
}

// No se necesita exportar el modelo en Go ya que no se usará para conectarse directamente con Firebase.
