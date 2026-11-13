// PART 3 - the hook of the exams screen: the list with its three states, delete and create.
// Run it with:  npm test -- useExams
//
// It must return { status, exams, error, actionError, saving, reload, remove, create }:
//   status       "loading" | "ready" | "error"   (the three states of the request that lists)
//   exams        the array of exams ([] while loading and on error)
//   error        the sentence for the person when the LIST failed (null otherwise); use describeError
//   actionError  the sentence when a delete or a create failed (null otherwise); the list stays as it was
//   saving       true while a create is in flight
//   reload()     asks for the list again (status goes back to "loading")
//   remove(id)   DELETE; when the server confirms, the exam disappears from `exams`; resolves true or false
//   create(title) POST; when the server confirms, the new exam is added; resolves true or false
//
// TODO 1: the state and a useEffect that lists, with the three states. The effect gets an AbortController and a
//         `cancelled` flag, and its cleanup sets the flag and aborts: a late answer must never overwrite a newer one.
// TODO 2: `reload` (a counter that is a dependency of the effect is enough).
// TODO 3: `remove` and `create`. NEVER swallow an error: set `actionError` with describeError. `create` must
//         ignore a second call while the first one is still in flight (use a ref: a state is too late).
// Rule of the course: no hook inside an if, a loop or after a return.
import { useState, useEffect, useCallback, useRef } from "react";
import axios from "axios";
import { createExam, deleteExam, describeError, listExams } from "./api";

export default function useExams() {
  const [status, setStatus] = useState("loading");
  const [exams, setExams] = useState([]);
  const [error, setError] = useState(null);
  const [actionError, setActionError] = useState(null);
  const [saving, setSaving] = useState(false);
  const [reloadVersion, setReloadVersion] = useState(0);

  // Ref para evitar doble envío síncrono en create() mientras hay una petición en vuelo
  const savingRef = useRef(false);

  // Efecto que lista los cuestionarios y administra los tres estados
  useEffect(() => {
    const controller = new AbortController();
    let cancelled = false;

    setStatus("loading");
    setError(null);

    listExams({ signal: controller.signal })
      .then((data) => {
        if (!cancelled) {
          setExams(data);
          setStatus("ready");
          setError(null);
        }
      })
      .catch((err) => {
        if (cancelled) return;
        if (axios.isCancel(err) || err.name === "CanceledError" || err.code === "ERR_CANCELED") {
          return;
        }
        setExams([]);
        setStatus("error");
        setError(describeError(err));
      });

    return () => {
      cancelled = true;
      controller.abort();
    };
  }, [reloadVersion]);

  // Recarga manual de la lista
  const reload = useCallback(() => {
    setActionError(null);
    setReloadVersion((v) => v + 1);
  }, []);

  // Borrar un examen
  const remove = useCallback(async (id) => {
    setActionError(null);
    try {
      await deleteExam(id);
      setExams((prev) => prev.filter((exam) => exam.id !== id));
      return true;
    } catch (err) {
      setActionError(describeError(err));
      return false;
    }
  }, []);

  // Crear un examen
  const create = useCallback(async (title) => {
    if (savingRef.current) {
      return false;
    }
    savingRef.current = true;
    setSaving(true);
    setActionError(null);

    try {
      const created = await createExam(title);
      setExams((prev) => [...prev, created]);
      setActionError(null);
      return true;
    } catch (err) {
      setActionError(describeError(err));
      return false;
    } finally {
      savingRef.current = false;
      setSaving(false);
    }
  }, []);

  return {
    status,
    exams,
    error,
    actionError,
    saving,
    reload,
    remove,
    create,
  };
}
