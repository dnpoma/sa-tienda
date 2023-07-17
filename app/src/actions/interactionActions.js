import Axios from "axios";
import Cookie from "js-cookie";
import {
  CART_ADD_INTERACTION,
  CART_ADD_INTERACTION_PRODUCT,
} from "../constants/interactionConstants";

const validateUser = async (user) => {
  try {
    const userRequest = await Axios.get(`/interaction/user/${user}`);
    if (userRequest.status === 200) {
      // El usuario existe
      return true;
    } else {
      return false;
    }
  } catch (error) {
    console.error(error);
    return false;
  }
};

const createInteraction = async (user, products, ip) => {
  try {
    let response;
    const userRequest = await Axios.get(`/interaction/user/${user}`);
    const interactionId = userRequest.data._id.$oid; //
    response = await Axios.post(`/products_interaction/${interactionId}`, {
      products: products,
    });

    const data = response.data;
    // Manejar la respuesta según sea necesario
    console.log(data);
  } catch (error) {
    // Manejar el error según sea necesario
    console.error(error);
  }
};

const createInteractionUser = async (user, products, ip) => {
  let response;
  try {
    response = await Axios.post("/interaction_user/", {
      user: user,
      products: products,
      ip: ip,
    });
  } catch (error) {
    console.error(error);
  }
};

const createInteractionNoneUser = async (products, ip) => {
  let response;
  try {
    const ipRequest = await Axios.get(`/interaction/ip/${ip}`);
    if (ipRequest.data) {
      const interactionId = ipRequest.data._id.$oid;
      response = await Axios.post(`/products_interaction/${interactionId}`, {
        products: products,
      });
    } else {
      response = await Axios.post("/interaction/", {
        user: null,
        products: products,
        ip: ip,
      });
    }
    const data = response.data;
    // Manejar la respuesta según sea necesario
    console.log(data);
  } catch (error) {
    console.error(error);
  }
};

const addProductsToInteraction = async (interactionId, products) => {
  try {
    const response = await Axios.post(`/products/${interactionId}`, {
      products: products,
    });
    const data = response.data;
    // Manejar la respuesta según sea necesario
    console.log(data);
  } catch (error) {
    // Manejar el error según sea necesario
    console.error(error);
  }
};

const getIPAddress = async () => {
  try {
    const response = await fetch("https://api.ipify.org?format=json");
    const data = await response.json();
    const ipAddress = data.ip;
    return ipAddress;
  } catch (error) {
    console.error(error);
    // Maneja el error según sea necesario
    return null; // Otra opción es devolver un valor predeterminado en caso de error
  }
};

export {
  createInteraction,
  addProductsToInteraction,
  createInteractionUser,
  createInteractionNoneUser,
  getIPAddress,
  validateUser,
};
