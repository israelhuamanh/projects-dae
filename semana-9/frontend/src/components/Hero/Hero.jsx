import React from 'react';
import { Star, Clock, Ticket, PlayCircle, ShieldAlert } from 'lucide-react';
import './Hero.css';

export const Hero = ({ movie }) => {
  if (!movie) return null;

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

        <div className="hero-actions">
          <button className="btn-hero-primary">
            <Ticket size={18} />
            <span>Reservar Asientos</span>
          </button>
          <button className="btn-hero-secondary">
            <PlayCircle size={18} />
            <span>Ver Trailer</span>
          </button>
        </div>
      </div>
    </section>
  );
};
