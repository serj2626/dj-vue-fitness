import { MESSAGES } from "@/types/messages";
import axios from "axios";
import { defineStore } from "pinia";
import { ref } from "vue";

export interface IAbonement {
  id: number;
  title: string;
  description: string;
  price: number;
  number_of_months: number;
  start?: Date;
  end?: Date;
  status?: boolean;
}

export const useAbonementsStore = defineStore("abonements", () => {
  const abonements = ref<IAbonement[]>([]);

  const getAbonements = async () => {
    try {
      const { data } = await axios.get("/api/orders/abonements/");
      abonements.value = data;
    } catch {
      throw new Error(MESSAGES.DATA_ERROR);
    }
  };

  return { abonements, getAbonements };
});
