import React from 'react';
import './Button.css';

/**
 * Componente reutilizable Button.
 * 
 * @param {Object} props
 * @param {React.ReactNode} props.children - Contenido renderizado dentro del botón.
 * @param {'primary'|'secondary'|'outline'|'danger'|'ghost'|'icon'|'favorite'} [props.variant='primary'] - Aspecto visual del botón.
 * @param {'sm'|'md'|'lg'} [props.size='md'] - Dimensiones del botón.
 * @param {Function} [props.onClick] - Manejador de evento click.
 * @param {boolean} [props.disabled=false] - Estado deshabilitado.
 * @param {boolean} [props.active=false] - Indica si el botón está en estado activo/seleccionado.
 * @param {'button'|'submit'|'reset'} [props.type='button'] - Tipo de botón HTML.
 * @param {string} [props.className=''] - Clases adicionales de estilo.
 * @param {string} [props.title] - Tooltip informativo.
 * @param {string} [props.ariaLabel] - Etiqueta de accesibilidad.
 */
export default function Button({
  children,
  variant = 'primary',
  size = 'md',
  onClick,
  disabled = false,
  active = false,
  type = 'button',
  className = '',
  title,
  ariaLabel,
  ...rest
}) {
  const classes = [
    'btn',
    `btn--${variant}`,
    `btn--${size}`,
    active ? 'btn--active' : '',
    className
  ].filter(Boolean).join(' ');

  return (
    <button
      type={type}
      className={classes}
      onClick={onClick}
      disabled={disabled}
      title={title}
      aria-label={ariaLabel || title}
      {...rest}
    >
      {children}
    </button>
  );
}
