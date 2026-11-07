import React from 'react';
import { Star, Clock, Ticket, PlayCircle, ShieldAlert, Heart, Search } from 'lucide-react';
import Button from '../Button/Button';
import './Hero.css';

/**
 * Componente Hero Banner con película destacada, buscador integrado y botones reutilizables.
 * 
 * @param {Object} props
 * @param {Object} props.movie - Datos de la película destacada.
 * @param {boolean} [props.isFavorite=false] - Indica si la película está en la lista de favoritos.
 * @param {Function} [props.onToggleFavorite] - Función que comunica al padre (App) para alternar favoritos.
 * @param {string} [props.searchValue=''] - Valor actual de búsqueda.
 * @param {Function} [props.onSearchChange] - Manejador de cambio para el buscador integrado.
 */
export const Hero = ({
  movie,
  isFavorite = false,
  onToggleFavorite,
  searchValue = '',
  onSearchChange
}) => {
  if (!movie) return null;

  const handleScrollToCartelera = () => {
    const el = document.getElementById('cartelera');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  };

  return (
    <section className="hero-banner">
      <div 
        className="hero-backdrop"
        style={{ backgroundImage: `url(${movie.backdrop})` }}
      >
        <div className="hero-overlay" />
      </div>

      <div className="container hero-content">
        <div className="hero-badge-group">
          <span className="badge-featured">Película Destacada</span>
          <span className="badge-genre">{movie.genre}</span>
        </div>

        <h1 className="hero-title">{movie.title}</h1>
        <p className="hero-original-title">Título Original: {movie.originalTitle}</p>

        <div className="hero-meta">
          <div className="meta-item rating">
            <Star size={16} fill="var(--color-accent-gold)" color="var(--color-accent-gold)" />
            <span>{movie.rating} / 10</span>
          </div>
          <div className="meta-item">
            <Clock size={16} />
            <span>{movie.duration}</span>
          </div>
          <div className="meta-item classification">
            <ShieldAlert size={16} />
            <span>{movie.classification}</span>
          </div>
        </div>

        <p className="hero-synopsis">{movie.synopsis}</p>

        <div className="hero-schedules">
          <span className="schedules-title">Horarios de hoy:</span>
          <div className="schedules-chips">
            {movie.schedules.map((time, idx) => (
              <span key={idx} className="time-chip">{time}</span>
            ))}
          </div>
        </div>

        {/* Acciones principales con componentes Button reutilizables */}
        <div className="hero-actions">
          <Button
            variant="primary"
            size="lg"
            onClick={handleScrollToCartelera}
            title="Reservar asientos para esta película"
          >
            <Ticket size={18} />
            <span>Reservar Asientos</span>
          </Button>

          <Button
            variant="outline"
            size="lg"
            onClick={() => alert(`Reproduciendo trailer oficial de ${movie.title}`)}
            title="Ver trailer en alta definición"
          >
            <PlayCircle size={18} />
            <span>Ver Trailer</span>
          </Button>

          {/* Botón Reutilizable de Favorita (Comunicación hacia arriba) */}
          <Button
            variant={isFavorite ? 'favorite' : 'secondary'}
            size="lg"
            active={isFavorite}
            onClick={() => onToggleFavorite && onToggleFavorite(movie.id)}
            title={isFavorite ? 'Quitar de mis favoritas' : 'Añadir a mis favoritas'}
            ariaLabel={isFavorite ? 'Quitar de favoritas' : 'Agregar a favoritas'}
          >
            <Heart
              size={18}
              fill={isFavorite ? '#f5c518' : 'none'}
              color={isFavorite ? '#f5c518' : 'currentColor'}
            />
            <span>{isFavorite ? 'En Favoritas' : 'Favorita'}</span>
          </Button>
        </div>

        {/* Paso 9 de la Guía: Integrar llamada a la acción del buscador en el banner */}
        <div className="hero-search-cta">
          <div className="hero-search-box">
            <Search size={18} className="hero-search-icon" />
            <input
              type="text"
              placeholder="¿Qué película buscas hoy? Filtra en tiempo real..."
              value={searchValue}
              onChange={(e) => onSearchChange && onSearchChange(e.target.value)}
              className="hero-search-input"
            />
            {searchValue && (
              <Button
                variant="ghost"
                size="sm"
                onClick={() => onSearchChange && onSearchChange('')}
                className="hero-search-clear"
              >
                Limpiar
              </Button>
            )}
            <Button
              variant="primary"
              size="sm"
              onClick={handleScrollToCartelera}
            >
              Explorar Cartelera
            </Button>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;
