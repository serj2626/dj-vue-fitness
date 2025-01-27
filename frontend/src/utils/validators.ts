import type { IFormReview } from "@/types/types";

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

function checkDateOrderTraining(dateStart: string, rate: number) {
  if (!dateStart) {
    throw new Error("Выберите дату начала абонемента");
  }
  if (new Date(dateStart) <= new Date()) {
    throw new Error("Дата бронирования не может быть меньше текущей");
  }
  if (!rate) {
    throw new Error("Выберите тариф");
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

function validatePhoneNumber(phoneNumber: string) {
  const phoneRegex =
    /^\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$/;
  return phoneRegex.test(phoneNumber);
}

export {
  validateDateReview,
  checkLogin,
  checkRegistration,
  checkDateOrderAbonement,
  checkDateOrderTraining,
  validatePhoneNumber,
};
