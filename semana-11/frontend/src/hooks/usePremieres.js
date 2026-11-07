import { useState, useEffect, useCallback } from 'react';
import { adaptMovieList } from '../utils/movieAdapter';

// Datos crudos de próximos estrenos (con claves heterogéneas para validar el adaptador)
const RAW_PREMIERES = [
  {
    movie_id: 101,
    titulo: 'Deadpool & Wolverine',
    titulo_original: 'Deadpool & Wolverine',
    genero: ['Acción', 'Comedia', 'Ciencia Ficción'],
    runtime_minutes: 127,
    vote_average: 8.4,
    censura: '+14',
    sinopsis: 'Wade Wilson recibe una oferta de la Autoridad de Variación Temporal que cambiará el destino del universo Marvel. Para salvar su mundo, recluta a un Wolverine reacio.',
    poster_path: 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800',
    backdrop_path: 'https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=1600',
    fecha_estreno: 'Próximo Jueves',
    funciones: ['16:00', '19:00', '22:00']
  },
  {
    movie_id: 102,
    titulo: 'Gladiator II',
    titulo_original: 'Gladiator II',
    genero: ['Acción', 'Drama', 'Aventura'],
    runtime_minutes: 148,
    vote_average: 8.2,
    censura: '+14',
    sinopsis: 'Años después de presenciar la muerte del héroe Máximo a manos de su tío, Lucio debe entrar en el Coliseo tras ser conquistado su hogar por los tiránicos emperadores.',
    poster_path: 'https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800',
    backdrop_path: 'https://images.unsplash.com/photo-1478720568477-152d9b164e26?w=1600',
    fecha_estreno: 'Próximo Mes',
    funciones: ['17:30', '20:45']
  },
  {
    movie_id: 103,
    titulo: 'Joker: Folie à Deux',
    titulo_original: 'Joker: Folie à Deux',
    genero: ['Drama', 'Crimen', 'Suspenso'],
    runtime_minutes: 138,
    vote_average: 7.9,
    censura: '+18',
    sinopsis: 'Arthur Fleck institucionalizado en Arkham esperando juicio por sus crímenes como Guasón mientras descubre el amor y su música interior junto a Lee Quinzel.',
    poster_path: 'https://images.unsplash.com/photo-1563089145-599997674d42?w=800',
    backdrop_path: 'https://images.unsplash.com/photo-1514306191717-452ec28c7814?w=1600',
    fecha_estreno: 'Muy Pronto',
    funciones: ['18:00', '21:30']
  },
  {
    movie_id: 104,
    titulo: 'Moana 2',
    titulo_original: 'Moana 2',
    genero: ['Animación', 'Aventura', 'Familia'],
    runtime_minutes: 100,
    vote_average: 8.1,
    censura: 'Apta para todos',
    sinopsis: 'Tras recibir una llamada inesperada de sus ancestros buscadores de caminos, Moana debe viajar a los mares lejanos de Oceanía para romper una maldición ancestral.',
    poster_path: 'https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800',
    backdrop_path: 'https://images.unsplash.com/photo-1519046904884-53103b34b206?w=1600',
    fecha_estreno: 'En 2 Semanas',
    funciones: ['14:30', '16:45', '19:15']
  }
];

/**
 * Hook propio usePremieres.
 * Simula la petición asíncrona a un servicio externo de cartelera de estrenos.
 * Maneja los tres estados requeridos por el Paso 7 de la guía:
 * 1. loading: booleano mientras se resuelve la consulta.
 * 2. data: lista de estrenos adaptados por el patrón adaptador.
 * 3. error: mensaje descriptivo del fallo con opción a reintentar.
 * 
 * @param {boolean} [initialFail=false] - Permite simular una falla para evaluar el estado de error.
 * @returns {Object} { loading, data, error, refetch, simulateError }
 */
export function usePremieres(initialFail = false) {
  const [loading, setLoading] = useState(true);
  const [data, setData] = useState([]);
  const [error, setError] = useState(null);

  const fetchPremieres = useCallback((shouldFail = false) => {
    setLoading(true);
    setError(null);

    // Simulación de latencia de red (1.2 segundos)
    const timer = setTimeout(() => {
      if (shouldFail) {
        setLoading(false);
        setError('Error al conectar con el servidor de estrenos (503 Service Unavailable). Verifique su conexión.');
        setData([]);
      } else {
        // Pasar los datos crudos por el patrón adaptador
        const adapted = adaptMovieList(RAW_PREMIERES);
        setData(adapted);
        setLoading(false);
        setError(null);
      }
    }, 1200);

    return () => clearTimeout(timer);
  }, []);

  useEffect(() => {
    const cleanup = fetchPremieres(initialFail);
    return cleanup;
  }, [fetchPremieres, initialFail]);

  const refetch = useCallback(() => {
    fetchPremieres(false);
  }, [fetchPremieres]);

  const simulateError = useCallback(() => {
    fetchPremieres(true);
  }, [fetchPremieres]);

  return {
    loading,
    data,
    error,
    refetch,
    simulateError
  };
}

export default usePremieres;
