import React from 'react';
import { Film, Compass, Ticket, Info, Search } from 'lucide-react';
import './Header.css';

export const Header = () => {
  return (
    <header className="main-header">
      <div className="container header-container">
        <div className="logo-brand">
          <Film className="logo-icon" size={28} />
          <div className="logo-text">
            <span className="brand-name">CineStar</span>
            <span className="brand-tag">DAE</span>
          </div>
        </div>

        <nav className="nav-menu">
          <a href="#cartelera" className="nav-link active">
            <Compass size={16} />
            <span>Cartelera</span>
          </a>
          <a href="#estrenos" className="nav-link">
            <Film size={16} />
            <span>Próximos Estrenos</span>
          </a>
          <a href="#promociones" className="nav-link">
            <Ticket size={16} />
            <span>Promociones</span>
          </a>
          <a href="#nosotros" className="nav-link">
            <Info size={16} />
            <span>Nosotros</span>
          </a>
        </nav>

        <div className="header-actions">
          <div className="search-bar">
            <Search size={16} className="search-icon" />
            <input type="text" placeholder="Buscar película..." />
          </div>
          <button className="btn-primary">Comprar Boletos</button>
        </div>
      </div>
    </header>
  );
};
