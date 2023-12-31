import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link } from "react-router-dom";
import { createOrder, detailsOrder, payOrder } from "../actions/orderActions";
import PaypalButton from "../components/PaypalButton";
function OrderScreen(props) {
  const orderPay = useSelector((state) => state.orderPay);
  const {
    loading: loadingPay,
    success: successPay,
    error: errorPay,
  } = orderPay;
  const dispatch = useDispatch();
  useEffect(() => {
    if (successPay) {
      props.history.push("/profile");
    } else {
      dispatch(detailsOrder(props.match.params.id));
    }
    return () => {};
  }, [successPay]);

  const handleSuccessPayment = (paymentResult) => {
    dispatch(payOrder(order, paymentResult));
  };

  const orderDetails = useSelector((state) => state.orderDetails);
  const { loading, order, error } = orderDetails;

  return loading ? (
    <div>Cargando ...</div>
  ) : error ? (
    <div>{error}</div>
  ) : (
    <div>
      <div className="placeorder">
        <div className="placeorder-info">
          <div>
            <h3>Envio</h3>
            <div>
              {order.shipping.address}, {order.shipping.city},
              {order.shipping.postalCode}, {order.shipping.country},
            </div>
            <div>
              {order.is_delivered
                ? "Entrega en " + order.delivered_at
                : "No entregado."}
            </div>
          </div>
          <div>
            <h3>Pago</h3>
            <div>Método de Pago: {order.payment.paymentMethod}</div>
            <div>
              {order.is_paid ? "Pagado en " + order.paid_at : "No Pagado."}
            </div>
          </div>
          <div>
            <ul className="cart-list-container">
              <li>
                <h3>Carrito de Compras</h3>
                <div>Precio</div>
              </li>
              {order.orderItems.length === 0 ? (
                <div>El carrito esta vacio</div>
              ) : (
                order.orderItems.map((item) => (
                  <li key={item.id}>
                    <div className="cart-image">
                      <img src={item.image} alt="product" />
                    </div>
                    <div className="cart-name">
                      <div>
                        <Link to={"/product/" + item.product}>{item.name}</Link>
                      </div>
                      <div>Qty: {item.qty}</div>
                    </div>
                    <div className="cart-price">${item.price}</div>
                  </li>
                ))
              )}
            </ul>
          </div>
        </div>
        <div className="placeorder-action">
          <ul>
            <li className="placeorder-actions-payment">
              {loadingPay && <div>Finalizando Pago...</div>}
              {!order.is_paid && (
                <PaypalButton
                  amount={order.total_price}
                  onSuccess={handleSuccessPayment}
                />
              )}
            </li>
            <li>
              <h3>Resumen del Pedido</h3>
            </li>
            <li>
              <div>Items</div>
              <div>${order.items_price}</div>
            </li>
            <li>
              <div>Envio</div>
              <div>${order.shipping_price}</div>
            </li>
            <li>
              <div>Impuesto</div>
              <div>${order.tax_price}</div>
            </li>
            <li>
              <div>Total</div>
              <div>${order.total_price}</div>
            </li>
          </ul>
        </div>
      </div>
    </div>
  );
}

export default OrderScreen;
