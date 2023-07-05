package entity

import "time"

type Review struct {
	ID int64 `json:"id"`
	Name    string    `json:"name"`
	Rating  int       `json:"rating"`
	Comment string    `json:"comment"`
}

type Product struct {
	ID int64 `json:"id"`
	Name         string    `json:"name"`
	Image        string    `json:"image"`
	Brand        string    `json:"brand"`
	Price        int       `json:"price"`
	Category     string    `json:"category"`
	CountInStock int       `json:"countInStock"`
	Description  string    `json:"description"`
	Rating       int       `json:"rating"`
	NumReviews   int       `json:"numReviews"`
	Reviews      []Review  `json:"reviews"`
	Timestamps   time.Time `json:"timestamps"`
}
