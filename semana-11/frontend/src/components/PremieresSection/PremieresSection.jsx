import React from 'react';
import { Sparkles, Calendar, Clock, Star, AlertTriangle, RefreshCw, Bug } from 'lucide-react';
import usePremieres from '../../hooks/usePremieres';
import SkeletonCard from '../SkeletonCard/SkeletonCard';
import Button from '../Button/Button';
import './PremieresSection.css';

/**
 * Sección de Próximos Estrenos.
 * Consume el custom hook usePremieres y resuelve explícitamente los 3 estados:
 * 1. Cargando (Skeletons con shimmer)
 * 2. Datos resueltos (Carrusel/Grid de películas adaptadas)
 * 3. Error (Alerta visual con botón de reintento)
 */
export default function PremieresSection() {
  const { loading, data, error, refetch, simulateError } = usePremieres();

  return (
    <section id="estrenos" className="premieres-section container">
      <div className="premieres-header">
        <div>
          <div className="premieres-badge">
            <Sparkles size={16} />
            <span>Exclusivo CineStar DAE</span>
          </div>
          <h2 className="section-title">Próximos Estrenos</h2>
          <p className="premieres-subtitle">
            Títulos que llegarán muy pronto a nuestras salas. Estado administrado mediante el hook <code>usePremieres</code>.
          </p>
        </div>

        {/* Barra de prueba interactiva para evaluación docente */}
        <div className="premieres-dev-tools">
          <Button
            variant="ghost"
            size="sm"
            onClick={refetch}
            disabled={loading}
            title="Recargar estrenos"
          >
            <RefreshCw size={14} className={loading ? 'animate-spin' : ''} />
            <span>Refrescar</span>
          </Button>

          <Button
            variant="outline"
            size="sm"
            onClick={simulateError}
            disabled={loading || Boolean(error)}
            title="Simular fallo de red 503 para evaluar estado de error"
          >
            <Bug size={14} />
            <span>Simular Error</span>
          </Button>
        </div>
      </div>

      {/* ESTADO 1: CARGANDO (Skeletons con animación Shimmer) */}
      {loading && (
        <div className="premieres-loading-wrapper">
          <div className="loading-indicator">
            <div className="loading-spinner" />
            <span>Consultando cartelera de estrenos con el servidor...</span>
          </div>
          <div className="premieres-grid">
            <SkeletonCard />
            <SkeletonCard />
            <SkeletonCard />
            <SkeletonCard />
          </div>
        </div>
      )}

      {/* ESTADO 2: ERROR (Fallo de servidor resuelto con botón de reintento) */}
      {!loading && error && (
        <div className="premieres-error-card animate-fade-in" role="alert">
          <div className="error-icon-box">
            <AlertTriangle size={36} />
          </div>
          <h3 className="error-title">No fue posible cargar los próximos estrenos</h3>
          <p className="error-description">{error}</p>
          <div className="error-actions">
            <Button
              variant="primary"
              size="md"
              onClick={refetch}
            >
              <RefreshCw size={16} />
              <span>Reintentar Conexión</span>
            </Button>
          </div>
        </div>
      )}

      {/* ESTADO 3: CON DATOS (Grid de estrenos adaptados) */}
      {!loading && !error && data && data.length > 0 && (
        <div className="premieres-grid animate-fade-in">
          {data.map(movie => (
            <article key={movie.id} className="premiere-card">
              <div className="premiere-poster-box">
                <img src={movie.poster} alt={movie.title} className="premiere-poster" loading="lazy" />
                <span className="premiere-date-badge">
                  <Calendar size={12} />
                  <span>{movie.premiereDate || 'Próximamente'}</span>
                </span>
                <span className="premiere-classification">{movie.classification}</span>
              </div>

              <div className="premiere-body">
                <span className="premiere-genre">{movie.genre}</span>
                <h3 className="premiere-title" title={movie.title}>{movie.title}</h3>
                
                <div className="premiere-meta">
                  <span className="premiere-rating">
                    <Star size={13} fill="#f5c518" color="#f5c518" />
                    <span>{movie.rating}</span>
                  </span>
                  <span className="premiere-duration">
                    <Clock size={13} />
                    <span>{movie.duration}</span>
                  </span>
                </div>

                <p className="premiere-synopsis">{movie.synopsis}</p>

                <Button
                  variant="outline"
                  size="sm"
                  className="btn-premiere-notify"
                  onClick={() => alert(`Te notificaremos cuando comience la preventa de "${movie.title}".`)}
                >
                  <Calendar size={14} />
                  <span>Avisarme de Preventa</span>
                </Button>
              </div>
            </article>
          ))}
        </div>
      )}
    </section>
  );
}
