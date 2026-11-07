import React, { useState, useEffect } from 'react';
import { Search, X } from 'lucide-react';
import Button from '../Button/Button';
import './MovieSearch.css';

/**
 * Componente controlado MovieSearch con retardo (debounce).
 * 
 * @param {Object} props
 * @param {string} props.value - Término de búsqueda actual sincronizado con el padre.
 * @param {Function} props.onSearchChange - Función callback que avisa al padre con el texto debounced.
 * @param {number} [props.delay=350] - Tiempo de retardo en milisegundos para el debounce.
 * @param {string} [props.placeholder='Buscar películas por título, director o género...'] - Texto del placeholder.
 */
export default function MovieSearch({
  value = '',
  onSearchChange,
  delay = 350,
  placeholder = 'Buscar películas por título, director o género...'
}) {
  // Estado local para respuesta inmediata de la entrada controlada
  const [inputValue, setInputValue] = useState(value);

  // Sincronizar si el valor externo cambia (ej. al presionar "Restablecer filtros")
  useEffect(() => {
    setInputValue(value);
  }, [value]);

  // Manejo del retardo (Debounce) con setTimeout
  useEffect(() => {
    const timer = setTimeout(() => {
      console.log(
        `%c[Search Debounced]%c Filtrado ejecutado con retardo (${delay}ms): "${inputValue}"`,
        'background: #f5c518; color: #000; font-weight: bold; padding: 2px 6px; border-radius: 4px;',
        'color: #ffffff; font-weight: normal;'
      );
      if (onSearchChange) {
        onSearchChange(inputValue);
      }
    }, delay);

    // Limpieza del temporizador en cada pulsación antes de cumplirse el delay
    return () => {
      clearTimeout(timer);
    };
  }, [inputValue, delay, onSearchChange]);

  const handleChange = (e) => {
    const text = e.target.value;
    console.log(
      `%c[Search Input]%c Tecla pulsada (inmediato): "${text}"`,
      'background: #2563eb; color: #fff; padding: 2px 6px; border-radius: 4px;',
      'color: #94a3b8;'
    );
    setInputValue(text);
  };

  const handleClear = () => {
    console.log('[Search Input] Búsqueda limpiada por el usuario');
    setInputValue('');
    if (onSearchChange) {
      onSearchChange('');
    }
  };

  return (
    <div className="movie-search">
      <div className="movie-search__wrapper">
        <Search className="movie-search__icon" size={20} />
        <input
          type="text"
          className="movie-search__input"
          value={inputValue}
          onChange={handleChange}
          placeholder={placeholder}
          aria-label="Buscar películas"
        />
        {inputValue && (
          <Button
            type="button"
            variant="ghost"
            size="sm"
            onClick={handleClear}
            className="movie-search__clear-btn"
            title="Limpiar búsqueda"
            ariaLabel="Limpiar campo de búsqueda"
          >
            <X size={16} />
          </Button>
        )}
      </div>
      {inputValue && (
        <span className="movie-search__hint">
          Buscando: <strong>"{inputValue}"</strong> (filtro optimizado con {delay}ms de retardo)
        </span>
      )}
    </div>
  );
}
