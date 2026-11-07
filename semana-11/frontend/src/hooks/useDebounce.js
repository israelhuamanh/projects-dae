import { useState, useEffect } from 'react';

/**
 * Hook reutilizable useDebounce.
 * Retrasa la actualización de un valor hasta que haya transcurrido un tiempo determinado
 * desde la última vez que dicho valor cambió.
 * 
 * @param {any} value - Valor que se desea retrasar (ej. texto de búsqueda).
 * @param {number} [delay=350] - Tiempo de retardo en milisegundos.
 * @returns {any} El valor retrasado (debouncedValue).
 */
export function useDebounce(value, delay = 350) {
  const [debouncedValue, setDebouncedValue] = useState(value);

  useEffect(() => {
    // Configurar temporizador para actualizar el valor debounced
    const handler = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);

    // Limpieza: si el valor cambia antes de que expire el delay, cancela el timeout
    return () => {
      clearTimeout(handler);
    };
  }, [value, delay]);

  return debouncedValue;
}

export default useDebounce;
