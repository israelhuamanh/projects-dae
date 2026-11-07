import React from 'react';
import { Film, Compass, Ticket, Info, Heart } from 'lucide-react';
import Button from '../Button/Button';
import './Header.css';

/**
 * Header de CineStar DAE con integración de botones reutilizables y contador de favoritas.
 * 
 * @param {Object} props
 * @param {number} [props.favoritesCount=0] - Cantidad de películas marcadas como favoritas.
 * @param {boolean} [props.onlyFavorites=false] - Indica si el filtro de favoritas está activo.
 * @param {Function} [props.onToggleFavoritesFilter] - Alterna la vista de solo favoritas.
 */
export const Header = ({
  favoritesCount = 0,
  onlyFavorites = false,
  onToggleFavoritesFilter
}) => {
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
          {/* Botón Reutilizable de Favoritas con contador dinámico */}
          <Button
            variant={onlyFavorites ? 'favorite' : 'secondary'}
            size="sm"
            active={onlyFavorites}
            onClick={onToggleFavoritesFilter}
            className="header-fav-btn"
            title="Filtrar por películas favoritas"
            ariaLabel="Ver películas favoritas"
          >
            <Heart
              size={16}
              fill={favoritesCount > 0 ? '#f5c518' : 'none'}
              color={favoritesCount > 0 ? '#f5c518' : 'currentColor'}
            />
            <span>Favoritas</span>
            <span className="header-fav-badge">{favoritesCount}</span>
          </Button>

          {/* Botón Reutilizable Principal */}
          <Button
            variant="primary"
            size="sm"
            onClick={() => {
              const el = document.getElementById('cartelera');
              if (el) el.scrollIntoView({ behavior: 'smooth' });
            }}
          >
            Comprar Boletos
          </Button>
        </div>
      </div>
    </header>
  );
};

export default Header;
