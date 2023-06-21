import React, {Component} from 'react';  

import './styles/AboutAs.css';

import logo from './images/about_as.png';
import first from './images/valor_juego.png'
import second from './images/innovacion.png'
import third from './images/apliarse.png'
import opinion from './images/opinion.png'
import unete from './images/unete.png'

export default class AboutAs extends Component {
    render(){
        return(
    <React.Fragment>
    <section className='aboutas--container-bg'>
        <div className='container aboutas--container'>
            <div className='aboutas--container-information'>
                <h1>
                    Quienes somos
                </h1>
                <p>
                Somos más que un estudio, somos una familia de desarrolladores talentosos que están comprometidos a crear experiencias increíbles para nuestros fans. Para lograrlo, sin duda se necesita un equipo diverso, por lo que albergamos a todo, desde artistas, ingenieros, diseñadores, administradores e inventores, pero más que eso, estas mismas personas son padres, pilotos, pintores, son activistas, ciclistas y coleccionistas
                </p>
            </div>
            <div className>
                 <img className='' src={logo} alt="MyTems"/>
            </div>
        </div>
    </section>

    <section className='valores--container'>
        <div className='container'>
            <h1>Nuestros valores</h1>
            <div className='valores--container-items'>
                 <div className='item--card'>
                    <span className='blue'></span>
                    <img className='' src={first} alt='jugabilidad primero'/>
                    <div className='card-information'>
                        <h3>Jugabilidad primero</h3>
                        <p>Nuestra Prioridad #1. Obten los juegos  más divertidos, accesibles y gratificantes de la historia.</p>
                    </div>
                </div>

                <div className='item--card'>
                    <span className='fucsia'></span>
                    <img className='' src={second} alt='Innovación'/>
                    <div className='card-information'>
                        <h3>Innovación sorprendente</h3>
                        <p>Empujamos los límites de la tecnología, la creatividad y la imaginación en la búsqueda de crear increíbles experiencias.</p>
                    </div>
                </div>

                <div className='item--card'>
                    <span className='green'></span>
                    <img className='' src={third} alt='Amplificarse'/>
                    <div className='card-information'>
                        <h3>Amplificarse unos a otros</h3>
                        <p>Queremos mejorar juntos. Para hacer eso, buscamos diversas perspectivas, damos retroalimentación constructiva y escuchamos.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section className='aboutas--container-bg'>
        <div className=' container opiniones--container'>
            <div className='opiniones-title'>
                <figure  className='opiniones-logo'>
                    <img src={opinion}/>
                </figure>
                <span>Opiniones </span> de los usuarios
            </div>
            <div className='opiniones--card-items'>
                <div className='card--item'>
                    <div className='card--item-user'>
                    <span></span>
                    @terminator2000
                    </div>
                    <p>Amo mytems, pude lograr conseguir todos los items. Sigan así.</p>
                </div>
                <div className='card--item'>
                    <div className='card--item-user'>
                    <span></span>
                    @terminator2000
                    </div>
                    <p>Amo mytems, pude lograr conseguir todos los items. Sigan así.</p>
                </div>
                <div className='card--item'>
                    <div className='card--item-user'>
                    <span></span>
                    @terminator2000
                    </div>
                    <p>Amo mytems, pude lograr conseguir todos los items. Sigan así.</p>
                </div>
                <div className='card--item'>
                    <div className='card--item-user'>
                    <span></span>
                    @terminator2000
                    </div>
                    <p>Amo mytems, pude lograr conseguir todos los items. Sigan así.</p>
                </div>
            </div>
        </div>
    </section>

    <section>
        <div>
            <div className='unete-content'>
                <h2>Unete a nuestro equipo</h2>
                <p>Buscamos lo mejor de lo mejor para ayudarnos a construir historias heroicas, mundos míticos y experiencias legendarias. Si tiene valor y talento, tenemos el lienzo perfecto para imaginar su futuro. Deja tu información en el siguiente formulario, te estamos esperando.</p>
            </div>
            <figure className='unete-img'>
                <img src={unete} alt=''/>
            </figure>            
        </div>
    </section>

    </React.Fragment>
        );
    }
}