import React from 'react';
import { Link } from 'react-router-dom';

import './styles/Footer.css';

import footerLogo from '../images/footer_logo.png';
import icoDiscord from '../images/discord_icono.svg';
import icoTelegram from '../images/telegram_icono.svg';
import icoTwitter from '../images/twiter_icono.svg';
import icoInstagram from '../images/instagram_icono.svg';
import icoFacebook from '../images/facebook_icono.svg';


class Footer extends React.Component{
    render(){
        return(
        <div className="container--footer">
            <div className="container--footer-row container">
                <div >
                    <Link to="#">
                        <img className="footer-logo" src={footerLogo} alt="Logo MyTems"/>
                    </Link>
                </div>
                <div>
                    <h4>Acerca de</h4>
                    <ul>
                        <li>
                            <Link to="/">Home</Link>
                        </li>
                        <li>
                            <Link to="/store">Tienda</Link>
                        </li>
                        <li>
                            <Link to="/aboutas">Nosotros</Link>
                        </li>
                    </ul>
                </div>
                <div>
                    <div>
                        <h4>Contacto</h4>
                        <ul>
                            <li>
                                support@mytems.com
                            </li>
                        </ul>
                    </div>
                    <div className="footer-icons">
                        <h4>Siguenos</h4>
                        <Link to="#" target="_blank">
                            <img src={icoDiscord} alt="Discord icono"/>
                        </Link>
                        <Link to="#" target="_blank">
                            <img src={icoTelegram} alt="Telegram icono"/>
                        </Link>
                        <Link to="#" target="_blank">
                            <img src={icoTwitter} alt="Twitter icono"/>
                        </Link>
                        <Link to="#" target="_blank">
                            <img src={icoInstagram} alt="Instagram icono"/>
                        </Link>
                        <Link to="#" target="_blank">
                            <img src={icoFacebook} alt="Facebook icono"/>
                        </Link>
                    </div>
                </div>
            </div>
        </div>
        );
    }

}

export default Footer;