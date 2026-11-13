// PART 1 - the API client module: the ONLY place that knows the API's address and how its errors look.
// No component writes a URL by hand; they all call these functions.
// Run it with:  npm test -- api
import axios from "axios";

// TODO 1: the base address of the API in one place. `import.meta.env.VITE_API_URL` (a .env.local file) wins when it
//         exists; otherwise use "http://localhost:8000/api" (no trailing slash).
export const API_URL = import.meta.env?.VITE_API_URL || "http://localhost:8000/api";

// TODO 2: create the Axios instance with `axios.create`: the base URL, a timeout of 8000 ms and the header
//         Accept: application/json. Tests and `npm run dev` replace its adapter, so it must be a real Axios instance.
export const api = axios.create({
  baseURL: API_URL,
  timeout: 8000,
  headers: {
    Accept: "application/json",
  },
});

/** TODO 3: GET /exams/ -> the array of exams (response.data, not the whole response). Pass the `signal` to Axios. */
export function listExams({ signal } = {}) {
  const p = api.get("/exams/", { signal }).then((response) => response.data);
  p.catch(() => {});
  return p;
}

/** TODO 4: POST /exams/ with { title } -> the exam the server created (response.data). */
export async function createExam(title) {
  const response = await api.post("/exams/", { title });
  return response.data;
}

/** TODO 5: DELETE /exams/<id>/ -> resolves with undefined. The API's paths end with a slash. */
export async function deleteExam(id) {
  await api.delete(`/exams/${id}/`);
  return undefined;
}

/**
 * TODO 6: turns anything the client can throw into ONE sentence in Spanish for the person.
 *  - no response and error.code "ERR_NETWORK": cannot connect; mention the server and CORS.
 *  - error.code "ECONNABORTED" or "ETIMEDOUT": it took too long.
 *  - status 400: show the API's message for each field ({ title: ["Este campo ..."] }).
 *  - status 404: the resource no longer exists.
 *  - status 500 or more: the API failed; include the status number.
 *  - anything else: a generic sentence (never an empty string).
 */
export function describeError(error) {
  if (!error) {
    return "Ocurrió un error inesperado al procesar la solicitud.";
  }

  // Tiempo agotado (timeout)
  if (error.code === "ECONNABORTED" || error.code === "ETIMEDOUT") {
    return "La petición tardó demasiado tiempo en responder (tiempo de espera agotado).";
  }

  // Sin respuesta del servidor o bloqueo de CORS (ERR_NETWORK)
  if (error.code === "ERR_NETWORK" || (!error.response && error.message)) {
    return "No se pudo conectar con el servidor. Verifique que el servidor esté activo y la política de CORS configurada.";
  }

  // Respuestas HTTP con código de estado
  if (error.response) {
    const status = error.response.status;
    const data = error.response.data;

    // Error 400: Validación de campos
    if (status === 400) {
      if (typeof data === "object" && data !== null) {
        const parts = Object.entries(data).map(([field, errs]) => {
          const detail = Array.isArray(errs) ? errs.join(", ") : String(errs);
          return `${field}: ${detail}`;
        });
        if (parts.length > 0) {
          return parts.join("; ");
        }
      }
      return "Datos no válidos para la operación (error 400).";
    }

    // Error 404: Recurso no encontrado
    if (status === 404) {
      return "El recurso solicitado ya no existe en el servidor.";
    }

    // Error 500+: Error interno del servidor
    if (status >= 500) {
      return `Error interno del servidor (código ${status}). Intente nuevamente más tarde.`;
    }
  }

  // Cualquier otro error
  if (typeof error.message === "string" && error.message.trim().length > 10) {
    return error.message;
  }

  return "Ocurrió un error inesperado al comunicarse con el servicio web.";
}
