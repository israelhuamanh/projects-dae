import axios from "axios";

export const API_URL = import.meta.env?.VITE_API_URL ?? "http://localhost:8000/api";

export const api = axios.create({
  baseURL: API_URL,
  timeout: 8000,
  headers: { Accept: "application/json" },
});

export function listExams() {
  return api.get("/exams/").then((response) => response.data);
}

export function createExam(title) {
  return api.post("/exams/", { title }).then((response) => response.data);
}

export function deleteExam(id) {
  return api.delete(`/exams/${id}/`).then(() => undefined);
}

export function describeError(error) {
  if (error?.code === "ECONNABORTED" || error?.code === "ETIMEDOUT") {
    return "La API tardó demasiado en responder. Intenta de nuevo.";
  }
  if (!error?.response) {
    if (error?.code === "ERR_NETWORK") {
      return "No se pudo conectar con la API. Revisa que el servidor esté encendido y que el origen esté autorizado en CORS.";
    }
    return "Error inesperado al llamar a la API.";
  }
  const { status, data } = error.response;
  if (status === 400 && data && typeof data === "object") {
    const lines = Object.entries(data).map(([field, messages]) => `${field}: ${[].concat(messages).join(" ")}`);
    return `Datos no válidos. ${lines.join(" ")}`;
  }
  if (status === 404) return "El recurso ya no existe en el servidor.";
  if (status >= 500) return `La API falló (error ${status}). Intenta de nuevo en unos minutos.`;
  return `La API respondió con el estado ${status}.`;
}
