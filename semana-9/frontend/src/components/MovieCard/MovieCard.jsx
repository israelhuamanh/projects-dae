import React from 'react';
import { Star, Clock, Ticket } from 'lucide-react';
import './MovieCard.css';

export const MovieCard = ({ movie }) => {
  return (
    <article className="movie-card">
      <div className="card-poster-wrapper">
        <img src={movie.poster} alt={movie.title} className="card-poster" loading="lazy" />
        <span className="card-badge-rating">
          <Star size={12} fill="#0b0c10" color="#0b0c10" />
          <span>{movie.rating}</span>
        </span>
        <span className="card-badge-classification">{movie.classification}</span>
      </div>

      <div className="card-body">
        <span className="card-genre">{movie.genre}</span>
        <h3 className="card-title" title={movie.title}>{movie.title}</h3>

        <div className="card-duration">
          <Clock size={14} />
          <span>{movie.duration}</span>
        </div>

        <p className="card-synopsis">{movie.synopsis}</p>

        <div className="card-schedules">
          <span className="schedules-label">Funciones:</span>
          <div className="schedules-grid">
            {movie.schedules.map((time, idx) => (
              <button key={idx} className="btn-time-slot" title={`Comprar para función ${time}`}>
                {time}
              </button>
            ))}
          </div>
        </div>

        <button className="btn-card-ticket">
          <Ticket size={16} />
          <span>Seleccionar Boletos</span>
        </button>
      </div>
    </article>
  );
};
