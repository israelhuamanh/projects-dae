import React, { useState, useEffect } from 'react';
import { Search, X } from 'lucide-react';
import useDebounce from '../../hooks/useDebounce';
import Button from '../Button/Button';
import './MovieSearch.css';

/**
 * Componente controlado MovieSearch.
 * Utiliza el custom hook propio useDebounce (Paso 5 de la guía)
 * para separar la lógica con estado del retardo, dejando el componente limpio.
 * 
 * @param {Object} props
 * @param {string} props.value - Término de búsqueda actual sincronizado.
 * @param {Function} props.onSearchChange - Función que notifica al padre cuando el término debounced cambia.
 * @param {number} [props.delay=350] - Retardo en ms para el hook useDebounce.
 * @param {string} [props.placeholder='Buscar películas por título, director o género...'] - Placeholder del input.
 */
export default function MovieSearch({
  value = '',
  onSearchChange,
  delay = 350,
  placeholder = 'Buscar películas por título, director o género...'
}) {
  // Estado local para respuesta inmediata de escritura
  const [inputValue, setInputValue] = useState(value);

  // Sincronizar si el valor externo cambia (ej. al presionar "Limpiar filtros" desde Hero)
  useEffect(() => {
    setInputValue(value);
  }, [value]);

  // Paso 5 de la guía: uso del custom hook useDebounce
  const debouncedSearchTerm = useDebounce(inputValue, delay);

  // Efecto que avisa al componente ancestro cuando el valor del hook debounced cambia
  useEffect(() => {
    console.log(
      `%c[Hook useDebounce]%c Valor retrasado actualizado (${delay}ms): "${debouncedSearchTerm}"`,
      'background: #f5c518; color: #000; font-weight: bold; padding: 2px 6px; border-radius: 4px;',
      'color: #ffffff;'
    );
    if (onSearchChange) {
      onSearchChange(debouncedSearchTerm);
    }
  }, [debouncedSearchTerm, delay, onSearchChange]);

  const handleChange = (e) => {
    const text = e.target.value;
    console.log(
      `%c[Search Input]%c Tecla pulsada: "${text}"`,
      'background: #2563eb; color: #fff; padding: 2px 6px; border-radius: 4px;',
      'color: #94a3b8;'
    );
    setInputValue(text);
  };

  const handleClear = () => {
    console.log('[Search Input] Búsqueda reseteada');
    setInputValue('');
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
          Buscando: <strong>"{inputValue}"</strong> (optimizado mediante el hook <code>useDebounce</code> de {delay}ms)
        </span>
      )}
    </div>
  );
}
