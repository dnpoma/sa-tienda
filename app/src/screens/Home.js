import React, {Component} from 'react';
import { Link } from 'react-router-dom';

import './styles/Home.css';


import start from '../images/start.svg';
import rifle_icono from './images/rifle_icono.png';
import cuchillo_icono from './images/cuchillo_icono.png';
import sniper_icono from './images/sniper_icono.png';
import pistola_icono from './images/pistola_icono.png';
import vinoculares_icono from './images/vinoculares_icono.png';
import Niña_pequeña_tienda from './images/Niña_pequeña_tienda.png';
import Akaly_informacion from './images/Akaly_informacion.png';
import bolitas from './images/bolitas.png';

export default class Home extends Component {
    render(){
        return(
    <React.Fragment>
            {/* <main> */}
                <section  className="main-hero">
                <div className="main-hero--information"> 
                    <div className="hero--information">
                        <h2 className="hero--box--title">
                            Bienvenido a un universo de juegos cruzados
                                para adquirir artículos virtuales. Compra, vende e intercambia los
                            artículos de tus juegos preferidos ahora.
                        </h2>
                    </div>
                </div>
                <section>
                    <div className="items--container">
                        <p>Más de 12 895 artículos</p>
                        <div className="items--container-row">
                            <div className="items-element">
                                <img src={rifle_icono} alt="Founder's Mark"/>
                                <p>Founder's Mark</p>
                                <b>$39.99</b>
                            </div>
                            <div className="items-element">
                                <img src={cuchillo_icono} alt="Doppler Ruby"/>
                                <p>Doppler Ruby</p>
                                <b>$40.99</b>
                            </div>
                            <div className="items-element">
                                <img src={sniper_icono} alt="Gungnir"/>
                                <p>Gungnir</p>
                                <b>$20.00</b>
                            </div>
                            <div className="items-element">
                                <img src={pistola_icono} alt="Instantly Withdrawable"/>
                                <p>Instantly Withdrawable</p>
                                <b>$27.00</b>
                            </div>
                            <div className="items-element">
                                <img src={vinoculares_icono} alt="Desert Eagle"/>
                                <p>Desert Eagle</p>
                                <b>$50.30</b>
                            </div>
                            <div className="items-element">
                                <img src={rifle_icono} alt="Founder's Mark"/>
                                <p>Founder's Mark</p>
                                <b>$39.99</b>
                            </div>
            
                        </div>
                    </div>
                </section>
         </section>
       
         {/* </main> */}
    
        <section className="information--container ">
            <div className="information--container-row container">
                <div className="information--item">
                    <h2>10%</h2>
                    <div className="information--line"></div>
                    <p>de descuento por tu primera compra</p>
                </div>
                <div className="information--item">
                    <h2>12 895</h2>
                    <div className="information--line"></div>
                    <p>objetos de CS:GO Dota 2 en nuestro sitio</p>
                </div>
                <div className="information--item">
                    <h2>24/7</h2>
                    <div className="information--line"></div>
                    <p>soporte técnico en línea</p>
                </div>
                <div className="information--item">
                    <h2>30 seg.</h2>
                    <div className="information--line"></div>
                    <p>el tiempo de espera para confirmas tu pago</p>
                </div>
            </div>
        </section>

        <section className="store--container">
            <div className="store--container-elements content">
                <div>
                    <h2>Tienda</h2>
                    <ul>
                        <li>
                            <img src={start} alt="Estrella"/>
                            Compra, vende e intercambia artículos

                        </li>
                        <li>
                            <img src={start} alt="Estrella"/>
                            Realiza transacciones desde cualquier tipo de juego
                        </li>
                        <li>
                            <img src={start} alt="Estrella"/>
                            Retira tu ganancias
                        </li>
                        <li>
                            <img src={start} alt="Estrella"/>
                            Verifica tus transacciones
                        </li>
                        <li>
                            <img src={start} alt="Estrella"/>
                            Solventamos tus pagos desdes cualquier servicio bancario del Ecuador
                        </li>
                    </ul>
                </div>
                <div>
                    <img src={Niña_pequeña_tienda} alt="Paimon feliz"/>
                </div>
            </div>
        </section>

        <section className="about--container" id="nosotros">
            <div className="about--container-elements container">
                <div>
                    <img src={Akaly_informacion} alt="Assassin lista para luchar"/>
                </div>
                <div className="about--element">
                    <img src={bolitas} alt="Decoracion"/>
                    <h1>SOBRE NOSOTROS</h1>
                    <p>
                        MyTems s un mercado para comerciar con artículos virtuales y tecnología con el fin de crear metatarsos. 
                        ed sollicitudin iaculis augue quis dapibus. Nulla lectus elit, congue eget ipsum eu, lobortis sagittis
                        lorem. Maecenas ac ante ullamcorper, interdum nibh sed, tristique augue. Maecenas aliquam tortor mauris,
                        quis rhoncus lacus bibendum euismod. Fusce quis aliquam sem. Nunc egestas porta eros non ullamcorper.
                        Mauris faucibus eleifend pulvinar. Fusce sed sollicitudin metus, nec ultricies dui. Pellentesque at 
                        ligula urna. Vestibulum tincidunt nisl non nisi rutrum, in luctus enim aliquet. Nullam risus mi, 
                        iaculis vel tempus eu, aliquet quis dui. Integer in enim est. Ut a quam quis nisi iaculis lobortis.
                        Pellentesque habitant morbi tristique senectus et netus et ma.
                        <Link to='/aboutas'>Ver más.</Link>
                    </p>
                </div>
            </div>
        </section>
    </React.Fragment>
        );
    }
}
