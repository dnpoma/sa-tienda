import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import { savePayment } from "../actions/cartActions";
import CheckoutSteps from "../components/CheckoutSteps";

function PaymentScreen(props) {
  const [payment_method, setpayment_method] = useState("");

  const dispatch = useDispatch();

  const submitHandler = (e) => {
    e.preventDefault();
    dispatch(savePayment({ payment_method }));
    props.history.push("placeorder");
  };
  return (
    <div>
      <CheckoutSteps step1 step2 step3></CheckoutSteps>
      <div className="form">
        <form onSubmit={submitHandler}>
          <ul className="form-container">
            <li>
              <h3>Pago</h3>
            </li>

            <li>
              <div>
                <input
                  type="radio"
                  name="payment_method"
                  id="payment_method"
                  value="paypal"
                  onChange={(e) => setpayment_method(e.target.value)}
                ></input>
                <label for="payment_method">Paypal</label>
              </div>
            </li>

            <li>
              <button type="submit" className="button primary">
                Siguiente
              </button>
            </li>
          </ul>
        </form>
      </div>
    </div>
  );
}
export default PaymentScreen;
