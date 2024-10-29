import type { IFormReview } from "./types/types";

function validateDateReview(formData: IFormReview) {
  if (!formData.message || !formData.rating) {
    throw new Error("Заполните все поля");
  }
  return formData;
}

function checkDateOrderAbonement(dateStart: string) {
  if (!dateStart) {
    throw new Error("Выберите дату начала абонемента");
  }
  if (new Date(dateStart) <= new Date()) {
    throw new Error("Дата бронирования не может быть меньше текущей");
  }
}

function checkDateOrderTraining(start: string, end: string) {
  if (new Date(start) >= new Date(end)) {
    throw new Error("Начало тренировки не может быть больше времени окончания");
  }
  if (new Date(start) <= new Date()) {
    throw new Error("Начало тренировки не может быть меньше или равно текущему времени");
  }
}

function checkLogin(login: string) {
  if (!login) {
    throw new Error("Заполните поле");
  }
  return login;
}

function checkRegistration(registration: string) {
  if (!registration) {
    throw new Error("Заполните поле");
  }
  return registration;
}

export {
  validateDateReview,
  checkDateOrderAbonement,
  checkLogin,
  checkRegistration,
  checkDateOrderTraining,
};
