import React, { useEffect } from 'react';
import { Heart, CheckCircle2, AlertTriangle, X } from 'lucide-react';
import Button from '../Button/Button';
import './Toast.css';

/**
 * Componente Toast emergente desacoplado.
 * Muestra notificaciones breves sin que el componente emisor sepa cómo se renderiza.
 * 
 * @param {Object} props
 * @param {string} props.message - Texto del mensaje emergente.
 * @param {'success'|'danger'|'info'} [props.type='success'] - Tipo de aviso.
 * @param {boolean} props.visible - Control de visibilidad.
 * @param {Function} props.onClose - Callback al cerrarse.
 * @param {number} [props.duration=3200] - Tiempo de auto-cierre en ms.
 */
export default function Toast({
  message,
  type = 'success',
  visible = false,
  onClose,
  duration = 3200
}) {
  useEffect(() => {
    if (!visible) return;

    const timer = setTimeout(() => {
      if (onClose) onClose();
    }, duration);

    return () => clearTimeout(timer);
  }, [visible, duration, onClose]);

  if (!visible || !message) return null;

  return (
    <div className={`toast-notification toast--${type} animate-toast-in`} role="alert">
      <div className="toast-icon">
        {type === 'danger' ? (
          <AlertTriangle size={18} />
        ) : type === 'success' ? (
          <Heart size={18} fill="#f5c518" color="#f5c518" />
        ) : (
          <CheckCircle2 size={18} />
        )}
      </div>

      <div className="toast-content">
        <span className="toast-message">{message}</span>
      </div>

      <Button
        variant="ghost"
        size="sm"
        onClick={onClose}
        className="toast-close-btn"
        title="Cerrar notificación"
        ariaLabel="Cerrar notificación"
      >
        <X size={15} />
      </Button>
    </div>
  );
}
