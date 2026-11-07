import React from 'react';
import { Film, MapPin, Phone, Mail, GitBranch, Heart } from 'lucide-react';
import Button from '../Button/Button';
import './Footer.css';

export const Footer = () => {
  return (
    <footer id="nosotros" className="main-footer">
      <div className="container footer-grid">
        <div className="footer-col brand-col">
          <div className="footer-logo">
            <Film className="footer-logo-icon" size={24} />
            <span className="brand-name">CineStar</span>
            <span className="brand-tag">DAE</span>
          </div>
          <p className="footer-desc">
            La mejor experiencia cinematográfica con tecnología láser 4K, sonido envolvente Dolby Atmos y salas VIP de última generación.
          </p>
          <div className="student-badge">
            <span>Desarrollado por: <strong>Israel Angel Huaman Huaman</strong></span>
            <span className="course-tag">DAE · Sección 4-C24-A · Tecsup 2026</span>
          </div>
        </div>

        <div className="footer-col">
          <h4 className="footer-heading">Navegación</h4>
          <ul className="footer-links">
            <li><a href="#cartelera">Cartelera</a></li>
            <li><a href="#estrenos">Próximos Estrenos</a></li>
            <li><a href="#promociones">Promociones</a></li>
            <li><a href="#dulceria">Dulcería</a></li>
          </ul>
        </div>

        <div className="footer-col">
          <h4 className="footer-heading">Contacto y Sedes</h4>
          <ul className="footer-contact">
            <li>
              <MapPin size={16} />
              <span>Av. Cascanueces 2221, Santa Anita · Lima</span>
            </li>
            <li>
              <Phone size={16} />
              <span>(01) 317-3900 / 0800-CINESTAR</span>
            </li>
            <li>
              <Mail size={16} />
              <span>atencion@cinestardae.pe</span>
            </li>
          </ul>
        </div>

        <div className="footer-col">
          <h4 className="footer-heading">Repositorio Oficial</h4>
          <p className="footer-repo-text">
            Código fuente del laboratorio de la Semana 10 disponible en GitHub:
          </p>
          <a 
            href="https://github.com/israelhuamanh/projects-dae/tree/main/semana-10" 
            target="_blank" 
            rel="noopener noreferrer"
            className="repo-link-btn"
          >
            <GitBranch size={16} />
            <span>Ver Semana 10 en GitHub</span>
          </a>
        </div>
      </div>

      <div className="footer-bottom container">
        <p>© 2026 CineStar DAE. Todos los derechos reservados. Laboratorio 10 (Componentes y Eventos) — Tecsup.</p>
        <p className="built-with">
          Hecho con <Heart size={14} className="heart-icon" /> utilizando React + Vite
        </p>
      </div>
    </footer>
  );
};

export default Footer;
