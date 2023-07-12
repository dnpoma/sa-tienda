import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import { listOrders, deleteOrder } from "../actions/orderActions";

function OrdersScreen(props) {
  const orderList = useSelector((state) => state.orderList);
  const { loading, orders, error } = orderList;

  const orderDelete = useSelector((state) => state.orderDelete);
  const {
    loading: loadingDelete,
    success: successDelete,
    error: errorDelete,
  } = orderDelete;

  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(listOrders());
    return () => {
      //
    };
  }, [successDelete]);

  const deleteHandler = (order) => {
    dispatch(deleteOrder(order.id));
  };
  return loading ? (
    <div>Loading...</div>
  ) : (
    <div className="content content-margined">
      <div className="order-header">
        <h3>Pedidos</h3>
      </div>
      <div className="order-list">
        <table className="table">
          <thead>
            <tr>
              <th>ID</th>
              <th>FECHA</th>
              <th>TOTAL</th>
              <th>USUARIO</th>
              <th>PAGO</th>
              <th>PAGADO EN</th>
              <th>ENVIADO</th>
              <th>ENTREGADO</th>
              <th>OBSERVACIÓN</th>
            </tr>
          </thead>
          <tbody>
            {orders.map((order) => (
              <tr key={order.id}>
                <td>{order.id}</td>
                <td>{order.created_at}</td>
                <td>{order.total_price}</td>
                <td>{order.user.name}</td>
                <td>{order.is_paid.toString()}</td>
                <td>{order.paid_at}</td>
                <td>{order.is_delivered.toString()}</td>
                <td>{order.delivered_at}</td>
                <td>
                  <Link to={"/order/" + order.id} className="button secondary">
                    Detalle
                  </Link>{" "}
                  <button
                    type="button"
                    onClick={() => deleteHandler(order)}
                    className="button secondary"
                  >
                    Eliminar
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
export default OrdersScreen;
