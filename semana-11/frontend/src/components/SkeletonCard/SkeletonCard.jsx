import React from 'react';
import './SkeletonCard.css';

/**
 * Componente SkeletonCard para representar el estado de carga (loading)
 * con animación shimmer de placeholder.
 */
export default function SkeletonCard() {
  return (
    <div className="skeleton-card" aria-hidden="true">
      <div className="skeleton-poster shimmer" />
      <div className="skeleton-body">
        <div className="skeleton-line skeleton-line--tag shimmer" />
        <div className="skeleton-line skeleton-line--title shimmer" />
        <div className="skeleton-line skeleton-line--subtitle shimmer" />
        <div className="skeleton-line skeleton-line--text shimmer" />
        <div className="skeleton-line skeleton-line--text shimmer" style={{ width: '80%' }} />
        <div className="skeleton-button shimmer" />
      </div>
    </div>
  );
}
