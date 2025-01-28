import type { ITrainerImage } from "@/types/workout";
import { MESSAGES } from "@/types/messages";
import axios from "axios";
import { defineStore } from "pinia";
import { ref } from "vue";

export interface iRate {
  id: string;
  title: string;
  count_minutes: number;
  price: number;
  description: string;
}

export interface ITrainer {
  id: string | number;
  first_name: string;
  last_name: string;
  position: string;
  phone: string;
  email: string;
  bio: string;
  avatar: string;
  trainer_reviews: [];
  count_reviews?: number;
  total_rating?: number;
  images?: ITrainerImage[];
}

export const useCoachStore = defineStore("coach", () => {
  const coach = ref<ITrainer>({} as ITrainer);
  const rates = ref<iRate[]>([]);

  const responsiveOptions = ref([
    {
      breakpoint: "1500px",
      numVisible: 5,
    },
    {
      breakpoint: "1024px",
      numVisible: 3,
    },
    {
      breakpoint: "768px",
      numVisible: 2,
    },
    {
      breakpoint: "560px",
      numVisible: 1,
    },
  ]);

  
  const getCoach = async (id: string) => {
    try {
      const { data } = await axios.get(`/api/workout/trainers/${id}`);
      coach.value = data;
    } catch {
      throw new Error(MESSAGES.COACH_ERROR);
    }
  };

  const getRates = async () => {
    try {
      const res = await axios.get("/api/workout/rates/");
      rates.value = res.data;
    } catch {
      throw new Error(MESSAGES.DATA_ERROR);
    }
  };

  return { coach, getCoach, rates, getRates, responsiveOptions };
});
