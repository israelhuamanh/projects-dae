import React from 'react';
import { Star, Clock, Ticket, Heart } from 'lucide-react';
import Button from '../Button/Button';
import './MovieCard.css';

/**
 * Componente MovieCard con paso de funciones hacia arriba (comunicación hijo-padre)
 * y componentes Button reutilizables.
 * 
 * @param {Object} props
 * @param {Object} props.movie - Objeto de película con sus propiedades.
 * @param {boolean} [props.isFavorite=false] - Indica si la película está marcada como favorita.
 * @param {Function} [props.onToggleFavorite] - Función del padre que se invoca al pulsar el botón de favorita.
 */
export const MovieCard = ({
  movie,
  isFavorite = false,
  onToggleFavorite
}) => {
  const handleFavoriteClick = (e) => {
    e.stopPropagation();
    // Comunicación hacia arriba: el hijo avisa al padre invocando la función recibida por props
    if (onToggleFavorite) {
      onToggleFavorite(movie.id);
    }
  };

  return (
    <article className={`movie-card ${isFavorite ? 'movie-card--favorite' : ''}`}>
      <div className="card-poster-wrapper">
        <img src={movie.poster} alt={movie.title} className="card-poster" loading="lazy" />
        
        {/* Insignia de calificación */}
        <span className="card-badge-rating">
          <Star size={12} fill="#0b0c10" color="#0b0c10" />
          <span>{movie.rating}</span>
        </span>
        
        {/* Insignia de clasificación */}
        <span className="card-badge-classification">{movie.classification}</span>

        {/* Botón Reutilizable de Favorita posicionado sobre el póster */}
        <Button
          variant={isFavorite ? 'favorite' : 'icon'}
          size="sm"
          active={isFavorite}
          onClick={handleFavoriteClick}
          className="card-favorite-btn"
          title={isFavorite ? 'Quitar de favoritas' : 'Marcar como favorita'}
          ariaLabel={isFavorite ? `Quitar ${movie.title} de favoritas` : `Agregar ${movie.title} a favoritas`}
        >
          <Heart
            size={16}
            fill={isFavorite ? '#f5c518' : 'none'}
            color={isFavorite ? '#f5c518' : '#ffffff'}
          />
        </Button>
      </div>

      <div className="card-body">
        <div className="card-header-meta">
          <span className="card-genre">{movie.genre}</span>
          {isFavorite && <span className="card-favorite-tag">★ Favorita</span>}
        </div>

        <h3 className="card-title" title={movie.title}>{movie.title}</h3>

        <div className="card-duration">
          <Clock size={14} />
          <span>{movie.duration}</span>
        </div>

        <p className="card-synopsis">{movie.synopsis}</p>

        <div className="card-schedules">
          <span className="schedules-label">Funciones de hoy:</span>
          <div className="schedules-grid">
            {movie.schedules.map((time, idx) => (
              <Button
                key={idx}
                variant="secondary"
                size="sm"
                className="btn-time-slot"
                onClick={() => alert(`Seleccionada función de las ${time} para ${movie.title}`)}
                title={`Comprar para función ${time}`}
              >
                {time}
              </Button>
            ))}
          </div>
        </div>

        {/* Botón Reutilizable Principal para compra */}
        <Button
          variant="primary"
          size="md"
          className="btn-card-ticket"
          onClick={() => alert(`Iniciando reserva de boletos para: ${movie.title}`)}
        >
          <Ticket size={16} />
          <span>Seleccionar Boletos</span>
        </Button>
      </div>
    </article>
  );
};

export default MovieCard;
