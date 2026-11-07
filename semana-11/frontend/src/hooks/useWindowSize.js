import { useState, useEffect } from 'react';

/**
 * Hook reutilizable useWindowSize.
 * Escucha los cambios de dimensión del navegador y calcula propiedades de diseño adaptativo
 * (columnas recomendadas, banderas booleanas de breakpoints).
 * 
 * @returns {Object} { width, height, isMobile, isTablet, isDesktop, columnsCount }
 */
export function useWindowSize() {
  const [windowSize, setWindowSize] = useState(() => {
    if (typeof window !== 'undefined') {
      return {
        width: window.innerWidth,
        height: window.innerHeight
      };
    }
    return { width: 1200, height: 800 };
  });

  useEffect(() => {
    // Si no estamos en un entorno con DOM (SSR), no hacer nada
    if (typeof window === 'undefined') return;

    let timeoutId = null;

    const handleResize = () => {
      // Optimización ligera para no saturar con demasiados eventos resize
      clearTimeout(timeoutId);
      timeoutId = setTimeout(() => {
        setWindowSize({
          width: window.innerWidth,
          height: window.innerHeight
        });
      }, 50);
    };

    window.addEventListener('resize', handleResize);

    return () => {
      clearTimeout(timeoutId);
      window.removeEventListener('resize', handleResize);
    };
  }, []);

  const width = windowSize.width;
  const isMobile = width < 640;
  const isTablet = width >= 640 && width < 1024;
  const isDesktop = width >= 1024;

  // Paso 6 de la guía: decidir cuántas tarjetas se muestran por fila
  let columnsCount = 4;
  if (width < 640) {
    columnsCount = 1;
  } else if (width < 900) {
    columnsCount = 2;
  } else if (width < 1280) {
    columnsCount = 3;
  } else {
    columnsCount = 4;
  }

  return {
    width,
    height: windowSize.height,
    isMobile,
    isTablet,
    isDesktop,
    columnsCount
  };
}

export default useWindowSize;
