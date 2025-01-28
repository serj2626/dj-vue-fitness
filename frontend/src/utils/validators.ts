import type { IFormReview } from "@/types/types";
import { MESSAGES } from "@/types/messages";

function validateDateReview(formData: IFormReview) {
  if (!formData.message || !formData.rating) {
    throw new Error(MESSAGES.FILL_ALL_FIELDS);
  }
  return formData;
}

function checkDateOrderAbonement(dateStart: string) {
  if (!dateStart) {
    throw new Error(MESSAGES.DATE_START_SELECT);
  }
  if (new Date(dateStart) <= new Date()) {
    throw new Error(MESSAGES.DATE_ERROR);
  }
}

function checkDateOrderTraining(dateStart: string, rate: number) {
  if (!dateStart) {
    throw new Error(MESSAGES.DATE_START_SELECT);
  }
  if (new Date(dateStart) <= new Date()) {
    throw new Error(MESSAGES.DATE_ERROR);
  }
  if (!rate) {
    throw new Error(MESSAGES.RATE_SELECT);
  }
}

function checkLogin(login: string) {
  if (!login) {
    throw new Error(MESSAGES.FILL_FIELD);
  }
  return login;
}

function checkRegistration(registration: string) {
  if (!registration) {
    throw new Error(MESSAGES.FILL_FIELD);
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
