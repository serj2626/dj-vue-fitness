import type { IFormReview } from "./types/types";

function validateDateReview(formData: IFormReview) {
  if (!formData.message || !formData.rating) {
    throw new Error("Заполните все поля");
  }
  return formData;
}

function checkDateOrderAbonement(date: Date) {
  if (date <= new Date()) {
    throw new Error("Дата бронирования не может быть меньше текущей");
  }
  return date;
}

function checkDateOrderTraining(start: Date, end: Date) {
  if (start >= end) {
    throw new Error("Начало тренировки не может быть больше времени окончания");
  }
  if (start <= new Date()) {
    throw new Error("Начало тренировки не может быть меньше текущего времени");
  }
  return { start, end };
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
