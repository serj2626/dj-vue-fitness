import type { IFormReview } from "./types/types"


export function validateDateReview(formData: IFormReview) {
    if (!formData.message || !formData.rating) {
      throw new Error("Заполните все поля");
    }
    return formData;
  }